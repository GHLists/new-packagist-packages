#!/usr/bin/env python3
"""Fetch packages newly created on Packagist.org.

New packages are discovered through Packagist's
[metadata changes feed](https://packagist.org/metadata/changes.json), which
lists every package updated since a cursor timestamp. Because the feed does
not distinguish new packages from updates, each touched package is checked
against its p2 metadata, whose earliest version release date decides whether
the package was created inside the requested window.

The changes feed only retains a limited history, so the manifest records
``source_truncated`` whenever the cursor had to be moved forward to a window
start that is no longer covered.

The end of the last list and the feed cursor are stored in the manifest so
the next run resumes where the previous one stopped.
"""

import argparse
import csv
import datetime as dt
import http.client
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CHANGES_URL = "https://packagist.org/metadata/changes.json"
P2_URL = "https://repo.packagist.org/p2/{package}.json"
DEFAULT_USER_AGENT = (
    "new-packagist-packages/1.0 (https://github.com/GHLists/new-packagist-packages)"
)

MAX_HOURS = 24.0
MAX_PACKAGES = 1500
WORKERS = 8
DESCRIPTION_LIMIT = 300
CSV_HEADER = (
    "created_at",
    "package",
    "version",
    "author",
    "description",
)

TRANSIENT_ERRORS = (
    urllib.error.URLError,
    TimeoutError,
    json.JSONDecodeError,
    http.client.HTTPException,
    OSError,
)


class NotFound(Exception):
    pass


def iso(moment):
    moment = moment.astimezone(dt.timezone.utc)
    if moment.microsecond:
        fraction = f"{moment.microsecond:06d}".rstrip("0")
        return moment.strftime("%Y-%m-%dT%H:%M:%S") + f".{fraction}Z"
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_timestamp(value):
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    moment = dt.datetime.fromisoformat(text)
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=dt.timezone.utc)
    return moment.astimezone(dt.timezone.utc)


def feed_cursor(moment):
    """Packagist changes-feed cursor: epoch seconds followed by 4 decimals."""
    return f"{int(moment.timestamp()) * 10000 + (moment.microsecond // 100):09d}"


def timestamp_filename(moment):
    moment = moment.astimezone(dt.timezone.utc)
    stamp = moment.strftime("%Y-%m-%dT%H-%M-%S")
    if moment.microsecond:
        stamp += "-" + f"{moment.microsecond:06d}".rstrip("0")
    return stamp + "Z"


def fetch_json(url, user_agent, retries=3, backoff=5.0):
    last_error = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            url,
            headers={"User-Agent": user_agent, "Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code == 404:
                raise NotFound(url) from error
            last_error = error
        except TRANSIENT_ERRORS as error:
            last_error = error
        if attempt < retries:
            print(f"attempt {attempt} failed ({last_error}), retrying", file=sys.stderr)
            time.sleep(backoff * attempt)
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def clean_text(value, limit=DESCRIPTION_LIMIT):
    text = " ".join(str(value or "").split())
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "\u2026"
    return text


def collect_changed_packages(user_agent, retries, since):
    """Return the packages touched since ``since`` and whether it is covered."""
    cursor = feed_cursor(since)
    data = fetch_json(f"{CHANGES_URL}?since={cursor}", user_agent, retries=retries)
    actions = data.get("actions")
    if not isinstance(actions, list):
        raise RuntimeError("changes feed response does not contain actions")
    packages = set()
    for action in actions:
        if not isinstance(action, dict):
            continue
        name = action.get("package")
        if not isinstance(name, str) or not name:
            continue
        packages.add(name.split("~")[0])
    return packages


def package_row(package, user_agent, retries, since, until):
    """Check p2 metadata and build a row, or return a status.

    Statuses: ``ok`` (package created inside the window), ``old`` (package
    existed before the window), ``empty`` (no usable timestamps), ``missing``
    (no p2 metadata).
    """
    url = P2_URL.format(package=urllib.parse.quote(package, safe="/"))
    try:
        metadata = fetch_json(url, user_agent, retries=retries)
    except NotFound:
        return "missing", None
    versions = (metadata.get("packages") or {}).get(package)
    if not isinstance(versions, list) or not versions:
        return "empty", None
    times = []
    for version in versions:
        if not isinstance(version, dict):
            continue
        value = version.get("time")
        if value:
            try:
                times.append(parse_timestamp(value))
            except (TypeError, ValueError):
                continue
    if not times:
        return "empty", None
    first = min(times)
    if not (since < first <= until):
        return "old", None
    latest = max(
        (version for version in versions if isinstance(version, dict)),
        key=lambda version: version.get("time") or "",
    )
    authors = latest.get("authors")
    if isinstance(authors, list):
        names = [
            str(author.get("name") or "")
            for author in authors
            if isinstance(author, dict)
        ]
        authors_text = "; ".join(name for name in names if name)
    else:
        authors_text = ""
    row = {
        "created_at": iso(first),
        "package": package,
        "version": clean_text(latest.get("version"), 20),
        "author": clean_text(authors_text, 100),
        "description": clean_text(latest.get("description")),
    }
    return "ok", row


def write_csv(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_HEADER)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


def read_manifest_text(path):
    """Read the manifest from disk, or fall back to the committed copy.

    The workflow checks out only ``scripts`` from the repository, so the
    manifest can be missing from the working tree even though it is committed.
    """
    manifest_path = Path(path)
    try:
        return manifest_path.read_text(encoding="utf-8")
    except OSError:
        pass
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{manifest_path.as_posix()}"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout


def load_manifest(path):
    text = read_manifest_text(path)
    if text is None:
        return {}
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"manifest {path} is not valid JSON") from error
    if not isinstance(data, dict):
        raise RuntimeError(f"manifest {path} must contain a JSON object")
    version = data.get("state_version", 1)
    if version != 1:
        raise RuntimeError(f"manifest {path} has an unsupported state version")
    return data


def save_manifest(path, manifest):
    manifest_path = Path(path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = manifest_path.with_name(f".{manifest_path.name}.tmp")
    text = json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, manifest_path)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since",
        help="UTC start timestamp as ISO 8601 (default: end of the last list)",
    )
    parser.add_argument(
        "--until",
        help="UTC end timestamp as ISO 8601 (default: now)",
    )
    parser.add_argument("--output-dir", default="data")
    parser.add_argument("--manifest", default="latest.json")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument(
        "--lookback-hours",
        type=float,
        default=1.0,
        help="window length when no previous list exists (default: 1)",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    now = dt.datetime.now(dt.timezone.utc)
    until = parse_timestamp(args.until) if args.until else now
    manifest = load_manifest(args.manifest)

    if args.since:
        since = parse_timestamp(args.since)
        if "window" in manifest:
            stored_window = parse_timestamp(manifest["window"])
            if since < stored_window:
                raise RuntimeError(
                    "backfill would move the window backwards; "
                    f"the manifest window is {iso(stored_window)}"
                )
    elif "window" in manifest:
        since = parse_timestamp(manifest["window"])
    else:
        since = until - dt.timedelta(hours=args.lookback_hours)

    truncated = False
    if (until - since).total_seconds() > MAX_HOURS * 3600:
        print(
            f"window longer than {MAX_HOURS:.0f} hours; the changes feed "
            "likely does not cover it, moving the window start forward",
            file=sys.stderr,
        )
        since = until - dt.timedelta(hours=MAX_HOURS)
        truncated = True

    packages = collect_changed_packages(args.user_agent, args.retries, since)
    if len(packages) > MAX_PACKAGES:
        print(
            f"changes feed returned {len(packages)} packages, above the "
            f"cap of {MAX_PACKAGES}; coverage of this window is incomplete",
            file=sys.stderr,
        )
        truncated = True
        packages = set(sorted(packages)[:MAX_PACKAGES])

    rows = []
    skipped = 0
    statuses = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {
            package: pool.submit(
                package_row, package, args.user_agent, args.retries, since, until
            )
            for package in sorted(packages)
        }
        for package, future in futures.items():
            try:
                status, row = future.result()
            except RuntimeError as error:
                print(f"failed to check {package}: {error}", file=sys.stderr)
                statuses[package] = "error"
                skipped += 1
                continue
            statuses[package] = status
            if status == "ok":
                rows.append(row)
            else:
                skipped += 1
    counts = {}
    for status in statuses.values():
        counts[status] = counts.get(status, 0) + 1
    print(f"checked {len(statuses)} packages: {counts}", file=sys.stderr)

    rows.sort(key=lambda row: row["created_at"])
    manifest["window"] = iso(until)
    manifest["source_truncated"] = bool(truncated)
    if rows:
        output = (
            Path(args.output_dir)
            / f"new-packagist-packages-{timestamp_filename(until)}.csv"
        )
        write_csv(output, rows)
        manifest["list"] = {
            "path": output.as_posix(),
            "from": iso(since),
            "to": iso(until),
            "count": len(rows),
        }
        print(
            f"wrote {len(rows)} packages created between {iso(since)} "
            f"and {iso(until)} to {output}"
        )
    else:
        print(f"no new packages between {iso(since)} and {iso(until)}")
    save_manifest(args.manifest, manifest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
