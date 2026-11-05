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

## Latest list — 2026-11-05 22:20 UTC

New packages created between 2026-11-05 21:18 UTC and 2026-11-05 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T22-20-23-948005Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 21:39:14 | [evapanel/smm-api-client](https://www.nuget.org/packages/evapanel%2Fsmm-api-client) | v1.0.1 | Eva Panel | A small PHP client for the standard SMM panel API (v2): services, orders, statu… |
| 2026-11-05 21:45:48 | [alfonsobries/laravel-grok-bot](https://www.nuget.org/packages/alfonsobries%2Flaravel-grok-bot) | v1.0.0 | Alfonso Bribiesca | Laravel notification channel for Grok Bot: send any notification to a Grok Bot… |
| 2026-11-05 21:59:24 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.18.0 |  | The skeleton application for the Laravel framework. |
| 2026-11-05 22:06:27 | [shipit-software/csv-validator](https://www.nuget.org/packages/shipit-software%2Fcsv-validator) | v0.1.0 |  | Validate UTF-8 CSV structure and report precise diagnostic positions. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
