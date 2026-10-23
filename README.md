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

## Latest list — 2026-10-23 22:19 UTC

New packages created between 2026-10-23 21:21 UTC and 2026-10-23 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T22-19-47-643235Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 21:42:41 | [vanta/meminfo](https://www.nuget.org/packages/vanta%2Fmeminfo) | 0.1.0 | Benoit Jacquemont; Vlad Shash… | PHP extension that dumps the content of PHP memory as JSON, to hunt down memory… |
| 2026-10-23 21:46:04 | [preflow/members](https://www.nuget.org/packages/preflow%2Fmembers) | v0.26.0 |  | Preflow members — member accounts for a Preflow + Folio site: the member type,… |
| 2026-10-23 21:54:30 | [vanta/dump-meminfo](https://www.nuget.org/packages/vanta%2Fdump-meminfo) | 0.1 | Benoit Jacquemont; Vlad Shash… | dump-meminfo command: dump the memory of a running PHP process with the meminfo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
