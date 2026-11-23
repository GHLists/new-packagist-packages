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

## Latest list — 2026-11-23 12:21 UTC

New packages created between 2026-11-23 11:21 UTC and 2026-11-23 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T12-21-39-3725Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 11:21:41 | [schorsch3000/tick](https://www.nuget.org/packages/schorsch3000%2Ftick) | v1.0.0 | schorsch3000 | Tiny helper to run loops at a fixed interval without drift |
| 2026-11-23 11:41:40 | [mertaydin/laravel-backup-manager](https://www.nuget.org/packages/mertaydin%2Flaravel-backup-manager) | v0.3.0 |  | Database and application file backups for Laravel with pluggable cloud storage. |
| 2026-11-23 11:55:19 | [buildwithsmk/laravel-tenancy](https://www.nuget.org/packages/buildwithsmk%2Flaravel-tenancy) | v1.0.0 |  | Lightweight multi-tenancy for Laravel: shared database by default, and upgrade… |
| 2026-11-23 12:12:16 | [tomgould/apple-news-api](https://www.nuget.org/packages/tomgould%2Fapple-news-api) | v2.3.0 | TomGould | PHP client for the Apple News Publisher API that builds Apple News Format docum… |
| 2026-11-23 12:12:22 | [tomgould/puzzlerphpsdk](https://www.nuget.org/packages/tomgould%2Fpuzzlerphpsdk) | v1.1.2 | Tom Gould | PHP SDK for Puzzler Media REST API |
| 2026-11-23 12:12:29 | [tomgould/turbopush](https://www.nuget.org/packages/tomgould%2Fturbopush) | v2.2.0 | Tom Gould | PHP endpoint for TurboPush chunked uploads: validates, stores and safely reasse… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
