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

## Latest list — 2026-11-04 12:20 UTC

New packages created between 2026-11-04 10:20 UTC and 2026-11-04 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T12-20-37-868943Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 10:21:00 | [adamb/blocking](https://www.nuget.org/packages/adamb%2Fblocking) | 1.1.7 | Adam Binnersley | Block IP by either IP or range and check to see if string contains blocked word… |
| 2026-11-04 10:21:58 | [netgen/remote-media-ibexa](https://www.nuget.org/packages/netgen%2Fremote-media-ibexa) | 1.0.0 | Netgen | Netgen Remote Media & Ibexa CMS integration |
| 2026-11-04 10:22:40 | [adamb/user](https://www.nuget.org/packages/adamb%2Fuser) | 1.4.3 | Adam Binnersley | A user class |
| 2026-11-04 10:39:12 | [mtorromeo/fpm-proctitle](https://www.nuget.org/packages/mtorromeo%2Ffpm-proctitle) | 1.0.0 | Massimiliano Torromeo | Automatic, configurable process titles for php-fpm workers while they serve a r… |
| 2026-11-04 10:56:08 | [kumulo/symfony-ux-dsfr](https://www.nuget.org/packages/kumulo%2Fsymfony-ux-dsfr) | v0.1-alpha |  | Symfony UX DSFR bundle |
| 2026-11-04 11:15:19 | [ecomalo/ecomalo-php](https://www.nuget.org/packages/ecomalo%2Fecomalo-php) | v1.0.0 |  | Connect a Laravel or plain PHP shop to EcomAlo: send orders, receive signed sta… |
| 2026-11-04 11:43:28 | [itmosoft/laravel-inventory](https://www.nuget.org/packages/itmosoft%2Flaravel-inventory) | v1.0.0 |  | A reusable Laravel inventory package for stock locations, stock levels, movemen… |
| 2026-11-04 11:51:22 | [itmosoft/laravel-pricing](https://www.nuget.org/packages/itmosoft%2Flaravel-pricing) | v1.0.0 |  | A reusable Laravel pricing package with polymorphic prices, currency support, s… |
| 2026-11-04 12:08:59 | [itmosoft/laravel-promotions](https://www.nuget.org/packages/itmosoft%2Flaravel-promotions) | v1.0.0 |  | A reusable Laravel promotions package with coupons, discount campaigns, eligibi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
