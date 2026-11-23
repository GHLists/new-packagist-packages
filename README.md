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

## Latest list — 2026-11-23 11:21 UTC

New packages created between 2026-11-23 10:20 UTC and 2026-11-23 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T11-21-39-157298Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 10:25:12 | [fisharebest/collection](https://www.nuget.org/packages/fisharebest%2Fcollection) | 1.0.0 | Greg Roach | Collection objects for PHP arrays |
| 2026-11-23 10:30:57 | [shoplygg/shoply-php](https://www.nuget.org/packages/shoplygg%2Fshoply-php) | v0.11.3 |  | Shoply's API from your own server: every route as a method, safe retries, pages… |
| 2026-11-23 10:45:42 | [cofa/php-issues-checker](https://www.nuget.org/packages/cofa%2Fphp-issues-checker) | v0.1.0 | Mahmoud Gamal | Checks your PHP runtime against officially reported PHP security issues (php.ne… |
| 2026-11-23 10:46:04 | [upigateways/sdk](https://www.nuget.org/packages/upigateways%2Fsdk) | v1.0.1 | UPI Gateways | Official PHP SDK for UPI Gateways - Zero Transaction Fee (0% MDR) UPI Payment G… |
| 2026-11-23 10:51:20 | [buildwithsmk/laravel-tenant-permission](https://www.nuget.org/packages/buildwithsmk%2Flaravel-tenant-permission) | v1.0.0 |  | Roles and permissions for Laravel. Works as plain RBAC in a single app, or tena… |
| 2026-11-23 10:55:36 | [filefabrik/rfc9421](https://www.nuget.org/packages/filefabrik%2Frfc9421) | v1.9.0 | RT Filefabrik | Create and validate RFC 9421 HTTP Signatures for ActivityPub. |
| 2026-11-23 11:00:23 | [ahwet-sen/asset-files](https://www.nuget.org/packages/ahwet-sen%2Fasset-files) | v1.18.0 | Ahwet Şen | Asset Files. |
| 2026-11-23 11:14:59 | [mcdennem/bolt-translations](https://www.nuget.org/packages/mcdennem%2Fbolt-translations) | v0.1.0 |  | Craft-like translations manager for Bolt CMS |
| 2026-11-23 11:17:14 | [islesurlasorguetourisme/sulu-qrcode-bundle](https://www.nuget.org/packages/islesurlasorguetourisme%2Fsulu-qrcode-bundle) | v0.1.0 | Enzo Brigati | Dynamic QR codes for Sulu 3: stable short URLs, editable targets, scan statisti… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
