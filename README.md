# New Packagist packages

Hourly lists of packages newly created on
[Packagist.org](https://packagist.org/), the default package registry for
[Composer](https://getcomposer.org/). New packages are discovered through
Packagist's [metadata changes feed](
https://packagist.org/metadata/changes.json), which lists every package
updated since a cursor timestamp; because the feed does not distinguish new
packages from updates, each touched package is checked against its p2
metadata, whose earliest version release date decides whether the package was
created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-packagist-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-17 16:18 UTC

New packages created between 2026-10-17 15:19 UTC and 2026-10-17 16:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T16-18-42-236919Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 15:27:36 | [alantiller/utilities](https://www.nuget.org/packages/alantiller%2Futilities) | v1.0.0 | Alan Tiller | Framework-independent PHP helpers for dates, strings, UUIDs, encoding and valid… |
| 2026-10-17 16:01:59 | [0x15f/liquid](https://www.nuget.org/packages/0x15f%2Fliquid) | v0.1.0 | Fabio Capucci | Liquid templates for PHP and Laravel with compiled rendering, Redis caching and… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
