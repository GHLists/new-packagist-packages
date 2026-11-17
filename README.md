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

## Latest list — 2026-11-17 03:21 UTC

New packages created between 2026-11-17 02:21 UTC and 2026-11-17 03:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T03-21-25-65969Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 02:32:09 | [xiaoh0o/queue](https://www.nuget.org/packages/xiaoh0o%2Fqueue) | 1.0.1 |  | PHP queue |
| 2026-11-17 02:42:17 | [thesis/source-location](https://www.nuget.org/packages/thesis%2Fsource-location) | v0.1.0 | Vadim Zanfir; Valentin Udalts… | Where in the source code: a file and a line, the caller outside a library, the… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
