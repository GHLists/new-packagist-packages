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

## Latest list — 2026-11-05 16:20 UTC

New packages created between 2026-11-05 15:21 UTC and 2026-11-05 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T16-20-53-951338Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 15:33:37 | [sevaske/laravel-taqnyat](https://www.nuget.org/packages/sevaske%2Flaravel-taqnyat) | 1.0.0 | sevaske | Laravel integration for the Taqnyat SMS API (taqnyat.sa): facade, notification… |
| 2026-11-05 15:34:13 | [todu-io/lar-extend](https://www.nuget.org/packages/todu-io%2Flar-extend) | 1.0.3 |  | Laravel 插件式开发支持器 |
| 2026-11-05 15:47:21 | [nickdekruijk/laravel-bot-noise](https://www.nuget.org/packages/nickdekruijk%2Flaravel-bot-noise) | 1.0.0 | Nick de Kruijk | Keeps bot traffic out of your Laravel error tracking: filters Livewire probe ex… |
| 2026-11-05 16:15:48 | [doi6doi/asmtabify](https://www.nuget.org/packages/doi6doi%2Fasmtabify) | v0.1 | Zoltán Várnagy | Tabulates assembly source by its jumps, so loops and ifs become visible |
| 2026-11-05 16:16:07 | [liberusoftware/webhooks-api](https://www.nuget.org/packages/liberusoftware%2Fwebhooks-api) | 1.0.2 |  | Webhooks api presentation adapter. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
