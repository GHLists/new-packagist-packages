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

## Latest list — 2026-10-23 16:22 UTC

New packages created between 2026-10-23 15:20 UTC and 2026-10-23 16:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T16-22-49-680483Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 15:25:31 | [nguyenduytan/php-totp](https://www.nuget.org/packages/nguyenduytan%2Fphp-totp) | v2.1.0 | Tony Nguyễn | Lightweight single-file TOTP library (RFC 6238) compatible with Google Authenti… |
| 2026-10-23 15:37:37 | [astral-php/astral-paypal](https://www.nuget.org/packages/astral-php%2Fastral-paypal) | 0.1.0 | astral-php | Paiement PayPal pour Astral — Orders API v2, capture, webhooks, remboursements |
| 2026-10-23 15:40:23 | [hymns/disposable-email](https://www.nuget.org/packages/hymns%2Fdisposable-email) | v0.1.0 | Muhammad Hamizi Jaminan | Refuse sign-ups from disposable (throwaway) email providers. Offline check, no… |
| 2026-10-23 15:48:50 | [givanov95/laravel-activity-log](https://www.nuget.org/packages/givanov95%2Flaravel-activity-log) | v1.0.0 | Georgi Ivanov | Who did what in a Laravel app: an append-only activity log with explicit actors… |
| 2026-10-23 16:03:56 | [teamones/dingtalk](https://www.nuget.org/packages/teamones%2Fdingtalk) | 3.0.0 | 张铭阳 | Teamones maintained EasyDingTalk 2.3.1 compatibility fork for PHP 8.5 |
| 2026-10-23 16:12:48 | [drivkraft/interlock](https://www.nuget.org/packages/drivkraft%2Finterlock) | v1.0.0 | Kim Eric Helle | Lightweight architecture manager for structuring Laravel apps with modules. |
| 2026-10-23 16:17:22 | [b3it/ais-client](https://www.nuget.org/packages/b3it%2Fais-client) | 1.0.0 |  | A lightweight PHP client that receives raw **AIS** (Automatic Identification Sy… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
