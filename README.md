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

## Latest list — 2026-11-16 23:19 UTC

New packages created between 2026-11-16 22:19 UTC and 2026-11-16 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T23-19-27-777384Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 22:23:01 | [jeffersongoncalves/filament-lgpd](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-lgpd) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-lgpd: a personal data inventory page (LGPD) listing… |
| 2026-11-16 22:31:46 | [sloukapetr/eet-laravel-package](https://www.nuget.org/packages/sloukapetr%2Feet-laravel-package) | v1.0.0 | Petr Slouka | Laravel package for the Czech EET 2.0 SOAP interface and CA EET certificate ren… |
| 2026-11-16 22:38:04 | [universeitgroup/kurdish-sorani](https://www.nuget.org/packages/universeitgroup%2Fkurdish-sorani) | v0.1.0 | Universe IT Group | Kurdish (Sorani) toolkit for Laravel: text normalization, Kurdish digits, IQD f… |
| 2026-11-16 22:38:16 | [jeffersongoncalves/filament-lgpd-consent](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-lgpd-consent) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-lgpd-consent: browse the append-only LGPD consent l… |
| 2026-11-16 22:38:16 | [ktulchu/php-webhook-inbox](https://www.nuget.org/packages/ktulchu%2Fphp-webhook-inbox) | v0.2.0 |  | Framework-independent transactional PostgreSQL webhook inbox for PHP |
| 2026-11-16 22:40:49 | [jacekkow/enable-banking-api](https://www.nuget.org/packages/jacekkow%2Fenable-banking-api) | v1.0.0 |  | PSR-18 client for the Enable Banking API (Account Information Service) |
| 2026-11-16 22:49:33 | [jeffersongoncalves/filament-lgpd-retention](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-lgpd-retention) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-lgpd-retention: preview and run LGPD data retention… |
| 2026-11-16 22:51:28 | [triploide/toolbox](https://www.nuget.org/packages/triploide%2Ftoolbox) | 2.0.0 | Maximiliano Yañez | A Laravel CRUD toolkit that auto-resolves controllers, dataproviders, repositor… |
| 2026-11-16 23:01:14 | [yellow-three/omnipay-iyzico](https://www.nuget.org/packages/yellow-three%2Fomnipay-iyzico) | v0.1.0 |  | Iyzico gateway for Omnipay v3 payment processing library |
| 2026-11-16 23:05:34 | [jeffersongoncalves/laravel-lgpd-audit-log](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-lgpd-audit-log) | 1.0.0 | Jefferson Gonçalves | LGPD audit trail for Laravel: an append-only, hash-chained log of who accessed,… |
| 2026-11-16 23:12:00 | [jeffersongoncalves/laravel-lgpd-incidents](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-lgpd-incidents) | 1.0.0 | Jefferson Gonçalves | LGPD security incident register for Laravel: track incidents, risk assessment a… |
| 2026-11-16 23:18:18 | [jeffersongoncalves/laravel-lgpd-records](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-lgpd-records) | 1.0.0 | Jefferson Gonçalves | LGPD records of processing activities (ROPA) for Laravel: purposes, legal bases… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
