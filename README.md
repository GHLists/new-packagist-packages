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

## Latest list — 2026-11-05 09:21 UTC

New packages created between 2026-11-05 08:19 UTC and 2026-11-05 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T09-21-47-120615Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 08:22:08 | [fayne/laravel-filament-audit](https://www.nuget.org/packages/fayne%2Flaravel-filament-audit) | v1.0.0 | Fayne Guo | Optional queued operation auditing for CMS and Filament. |
| 2026-11-05 08:25:41 | [fayne/laravel-filament-sso](https://www.nuget.org/packages/fayne%2Flaravel-filament-sso) | v1.0.0 | Fayne Guo | Single sign-on integrations for Laravel and Filament. |
| 2026-11-05 08:26:04 | [doctrine/orm-plugin-second-level-cache](https://www.nuget.org/packages/doctrine%2Form-plugin-second-level-cache) | 1.0.1 | Benjamin Eberlei | Required package to make second level cache working on doctrine/orm from versio… |
| 2026-11-05 08:34:24 | [rishi-raj-jain/flysystem-neon](https://www.nuget.org/packages/rishi-raj-jain%2Fflysystem-neon) | v1.0.0 | Rishi Raj Jain | Flysystem adapter for Neon Object Storage (branchable, S3-compatible storage on… |
| 2026-11-05 08:46:45 | [fayne/laravel-filament-qrcode](https://www.nuget.org/packages/fayne%2Flaravel-filament-qrcode) | v1.0.0 |  | QR code generation for Laravel and Filament. |
| 2026-11-05 08:51:31 | [jyim/laravel-schema-extend](https://www.nuget.org/packages/jyim%2Flaravel-schema-extend) | 1.0.0 | augustdai | Laravel 10.x 适配版：为迁移提供表注释 / 自增起始值 / 带长度的整型列（源自 zedisdog/laravel-schema-extend） |
| 2026-11-05 09:01:14 | [sting_bo/php-gome](https://www.nuget.org/packages/sting_bo%2Fphp-gome) | v1.0.0 | Sting Bo | Calling Match Engine Of Go Service |
| 2026-11-05 09:04:55 | [actself/role-permission](https://www.nuget.org/packages/actself%2Frole-permission) | v1.0 |  | Flexible role and permission management package for Laravel |
| 2026-11-05 09:09:59 | [fayne/laravel-filament-store-locator](https://www.nuget.org/packages/fayne%2Flaravel-filament-store-locator) | v1.0.0 |  | Store locator for Laravel and Filament. |
| 2026-11-05 09:12:57 | [pnscripts/sheafgate-lite](https://www.nuget.org/packages/pnscripts%2Fsheafgate-lite) | v1.0.0 | PN Scripts | Sheafgate Lite: import XLSX, ODS and CSV files through Filament's own importer,… |
| 2026-11-05 09:16:39 | [fayne/laravel-filament-event](https://www.nuget.org/packages/fayne%2Flaravel-filament-event) | v1.0.0 | Fayne Guo | Event management for Laravel and Filament. |
| 2026-11-05 09:19:18 | [fayne/laravel-filament-page](https://www.nuget.org/packages/fayne%2Flaravel-filament-page) | v1.0.0 |  | Page management for Filament CMS. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
