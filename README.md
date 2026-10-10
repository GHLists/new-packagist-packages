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

## Latest list — 2026-10-10 12:19 UTC

New packages created between 2026-10-10 11:21 UTC and 2026-10-10 12:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T12-19-15-225658Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 11:53:22 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.5.2 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-10 12:00:45 | [cecil/theme-docsearch](https://www.nuget.org/packages/cecil%2Ftheme-docsearch) | 1.0.0 |  | Cecil component theme DocSearch |
| 2026-10-10 12:09:36 | [manzadey/larasentry-client](https://www.nuget.org/packages/manzadey%2Flarasentry-client) | v0.1.0 |  | A lightweight exception tracker client for Laravel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
