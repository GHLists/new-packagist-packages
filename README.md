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

## Latest list — 2026-10-20 13:21 UTC

New packages created between 2026-10-20 12:19 UTC and 2026-10-20 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T13-21-51-183669Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 12:21:13 | [gingerminds/symfony-cms](https://www.nuget.org/packages/gingerminds%2Fsymfony-cms) | 0.1.0 | Gingerminds | Menus, pages, content blocks and search for Gingerminds Symfony projects |
| 2026-10-20 12:22:24 | [survos/bagit](https://www.nuget.org/packages/survos%2Fbagit) | 2.43.8 |  | Framework-independent BagIt directory creation and integrity verification |
| 2026-10-20 12:39:03 | [mycomm/mycomm-php](https://www.nuget.org/packages/mycomm%2Fmycomm-php) | v0.1.0 | Cogneer | Official PHP SDK for the MyComm messaging API: messages, contacts, conversation… |
| 2026-10-20 12:53:31 | [jeffersongoncalves/filament-skeleton](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-skeleton) | 2.0.0 |  |  |
| 2026-10-20 12:55:50 | [stefaminator/php-cli-cmd](https://www.nuget.org/packages/stefaminator%2Fphp-cli-cmd) | 1.0.0 |  | The PHP CLI CMD library |
| 2026-10-20 13:00:20 | [avisaas/ti-ext-connector](https://www.nuget.org/packages/avisaas%2Fti-ext-connector) | 1.3.0 |  | AviSaaS storefront connector extension for TastyIgniter admin. |
| 2026-10-20 13:01:44 | [shasha1589/laravel-razorpay-billing](https://www.nuget.org/packages/shasha1589%2Flaravel-razorpay-billing) | v0.1.0 | shasha1589 | Cashier-style subscription billing for Laravel on Razorpay: plans, subscription… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
