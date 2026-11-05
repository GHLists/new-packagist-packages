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

## Latest list — 2026-11-05 10:22 UTC

New packages created between 2026-11-05 09:21 UTC and 2026-11-05 10:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T10-22-00-742646Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 09:24:25 | [andreybolonin/modernorm-bundle](https://www.nuget.org/packages/andreybolonin%2Fmodernorm-bundle) | v0.1.0-beta.1 |  | Symfony integration and Profiler for ModernORM, the PostgreSQL-first ORM. |
| 2026-11-05 09:27:31 | [djthossi/shippy-pro-sdk](https://www.nuget.org/packages/djthossi%2Fshippy-pro-sdk) | 1.0.0 | Sebastian Thoss | Typed, object-oriented PHP SDK for the ShippyPro API |
| 2026-11-05 09:29:16 | [fayne/shopping-cart](https://www.nuget.org/packages/fayne%2Fshopping-cart) | v1.0.0 | Fayne Guo | This is a custom shopping cart package for Laravel projects |
| 2026-11-05 09:32:44 | [fayne/laravel-filament-promotion](https://www.nuget.org/packages/fayne%2Flaravel-filament-promotion) | v1.0.0 |  | Promotion rules and discount calculation for Laravel and Filament. |
| 2026-11-05 09:36:47 | [fayne/laravel-filament-commerce](https://www.nuget.org/packages/fayne%2Flaravel-filament-commerce) | v1.0.0 |  | Multi-tenant commerce domain for Laravel and Filament. |
| 2026-11-05 09:44:19 | [xakki/log-symfony](https://www.nuget.org/packages/xakki%2Flog-symfony) | 0.4.0 |  | Symfony/Monolog log enrichment, redaction and formatters |
| 2026-11-05 09:46:30 | [n445/easy-admin-messenger-manager](https://www.nuget.org/packages/n445%2Feasy-admin-messenger-manager) | v0.1.1 |  | Symfony Messenger manager for EasyAdmin: queues overview, failed messages, sing… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
