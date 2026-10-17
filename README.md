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

## Latest list — 2026-10-17 05:19 UTC

New packages created between 2026-10-17 04:20 UTC and 2026-10-17 05:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T05-19-41-436302Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 04:31:08 | [oluokunkabiru/api-call-logger](https://www.nuget.org/packages/oluokunkabiru%2Fapi-call-logger) | v0.1.1 | OLUOKUN KABIRU ADESINA | Provider-agnostic Laravel logger for third-party API calls and incoming webhook… |
| 2026-10-17 05:10:21 | [x-multibyte/blatui-admin](https://www.nuget.org/packages/x-multibyte%2Fblatui-admin) | v0.0.1 | Roy Thia | An administration panel built using BlatUI. |
| 2026-10-17 05:13:40 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.6.2 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
