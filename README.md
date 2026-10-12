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

## Latest list — 2026-10-12 22:19 UTC

New packages created between 2026-10-12 21:19 UTC and 2026-10-12 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T22-19-30-606576Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 21:26:36 | [wilycode/logger-file](https://www.nuget.org/packages/wilycode%2Flogger-file) | v0.1.0 | Simon Piter | Lightweight PSR-3 file logger with channels, level filtering, structured contex… |
| 2026-10-12 21:40:38 | [wilycode/database-driver](https://www.nuget.org/packages/wilycode%2Fdatabase-driver) | v0.1.0 | Simon Piter | Database-agnostic connection, query, and transaction contracts for WilyCode PHP… |
| 2026-10-12 21:43:05 | [besmartand-pro/bsap-sensor-client](https://www.nuget.org/packages/besmartand-pro%2Fbsap-sensor-client) | 1.0.0 | BeSmartAnd.Pro | Framework-independent PHP client for the BeSmartAnd.Pro Sensor API. |
| 2026-10-12 22:02:31 | [besmartand-pro/bsap-sensor-bundle](https://www.nuget.org/packages/besmartand-pro%2Fbsap-sensor-bundle) | 1.0.0 | BeSmartAnd.Pro | Symfony integration for the BeSmartAnd.Pro Sensor PHP client. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
