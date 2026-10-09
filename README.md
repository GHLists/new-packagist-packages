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

## Latest list — 2026-10-09 12:20 UTC

New packages created between 2026-10-09 11:21 UTC and 2026-10-09 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T12-20-37-871549Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 11:35:29 | [wckd123/us-postal-codes](https://www.nuget.org/packages/wckd123%2Fus-postal-codes) | v1.0.0 |  | Offline US ZIP code lookup (ZIP to state and city) plus US state and territory… |
| 2026-10-09 11:41:50 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.4.6 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
