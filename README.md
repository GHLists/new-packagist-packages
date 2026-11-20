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

## Latest list — 2026-11-20 15:18 UTC

New packages created between 2026-11-20 14:20 UTC and 2026-11-20 15:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T15-18-46-407071Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 14:25:04 | [meetmage/module-advanced-seo](https://www.nuget.org/packages/meetmage%2Fmodule-advanced-seo) | v1.0.0 | Meet Shekhat | Smart meta templates, structured data and canonical URL control for Magento 2,… |
| 2026-11-20 14:34:36 | [salable/sdk](https://www.nuget.org/packages/salable%2Fsdk) | v1.0.0-beta.1 | Salable | Official PHP SDK for the Salable API |
| 2026-11-20 15:07:12 | [jonatasfenske/router](https://www.nuget.org/packages/jonatasfenske%2Frouter) | v1.0.0 | Robson V. Leite; Jonatas Fens… | Roteamento MVC PHP 8.5 com atributos #[Route], Rate Limiting, CORS automático,… |
| 2026-11-20 15:07:57 | [script-development/laravel-retention](https://www.nuget.org/packages/script-development%2Flaravel-retention) | v0.1.0 |  | Retention kernel for Laravel territories: a prune for append-only, hash-chained… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
