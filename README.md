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

## Latest list — 2026-10-22 09:19 UTC

New packages created between 2026-10-22 08:21 UTC and 2026-10-22 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T09-19-25-966152Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 08:42:12 | [xiaoyjayus/change-env-laravel](https://www.nuget.org/packages/xiaoyjayus%2Fchange-env-laravel) | v1.0.0 | xiaoyJayUs |  |
| 2026-10-22 08:46:49 | [dyongjun/ojt-sdk](https://www.nuget.org/packages/dyongjun%2Fojt-sdk) | v1.0.1 |  | 新智慧TMS API v5 SDK |
| 2026-10-22 08:51:48 | [alexisgeneau/laravel-belvedere](https://www.nuget.org/packages/alexisgeneau%2Flaravel-belvedere) | v0.1.0 | Alexis Geneau | Horizon-style queue dashboard for Laravel's database queue driver. |
| 2026-10-22 08:53:44 | [open-dxp/mate-extension](https://www.nuget.org/packages/open-dxp%2Fmate-extension) | v1.0.0 | DACHCOM.DIGITAL Stefan Hagspi… | Symfony AI Mate extension for OpenDXP. Gives coding agents the facts of the ins… |
| 2026-10-22 09:14:00 | [doska/symfony-bundle](https://www.nuget.org/packages/doska%2Fsymfony-bundle) | v0.1.0 |  | Dev-only toolbar that turns a clicked element into a Symfony-aware prompt: cont… |
| 2026-10-22 09:14:06 | [m2collective/filament-leaflet-map](https://www.nuget.org/packages/m2collective%2Ffilament-leaflet-map) | 0.1.0 | bu0nq |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
