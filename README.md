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

## Latest list — 2026-11-17 10:21 UTC

New packages created between 2026-11-17 09:20 UTC and 2026-11-17 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T10-21-30-030093Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 09:31:52 | [vectorbross/vb_bulk_translate](https://www.nuget.org/packages/vectorbross%2Fvb_bulk_translate) | 1.0.2 | Stijn Stroobants | Queue translatable entities and translate them on cron with a TMGMT translator. |
| 2026-11-17 09:35:37 | [smepay/smepay-php](https://www.nuget.org/packages/smepay%2Fsmepay-php) | v0.1.0 |  | Official PHP SDK for the SMEPay External API (UPI payments). |
| 2026-11-17 09:39:22 | [vytux/vytux_menu2](https://www.nuget.org/packages/vytux%2Fvytux_menu2) | v2.2.0 | Vytautas Krivickas | A webtrees custom module that adds a configurable menu of links, with optional… |
| 2026-11-17 09:40:34 | [hachitechs/hideguard-m2](https://www.nuget.org/packages/hachitechs%2Fhideguard-m2) | v1.0.0 |  | HideGuard Bot & Checkout Guard for Magento 2: browser verification and server-s… |
| 2026-11-17 09:41:30 | [fayne/laravel-ocr](https://www.nuget.org/packages/fayne%2Flaravel-ocr) | v0.1.0 |  | Laravel OCR with built-in cloud drivers |
| 2026-11-17 09:44:33 | [cable8mm/laravel-locale-timezone](https://www.nuget.org/packages/cable8mm%2Flaravel-locale-timezone) | v1.0.0 | Samgu Lee | Per-request locale and timezone context for Laravel: Accept-Language and X-Time… |
| 2026-11-17 09:49:47 | [artack/fixtures-guard](https://www.nuget.org/packages/artack%2Ffixtures-guard) | 1.0.0 | ARTACK WebLab GmbH | Symfony bundle that stops Doctrine fixtures and Foundry from wiping a database… |
| 2026-11-17 09:55:21 | [atlasaidev/atlasvoice-sdk](https://www.nuget.org/packages/atlasaidev%2Fatlasvoice-sdk) | v0.4.0 | AtlasAiDev | PHP client for AtlasVoice Cloud text-to-speech: speech, audio jobs for long tex… |
| 2026-11-17 10:01:56 | [jeffersongoncalves/laravel-lgpd-minors](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-lgpd-minors) | 1.0.0 | Jefferson Gonçalves | ECA Digital (Lei 15.211/2025) toolkit for Laravel: age assurance results withou… |
| 2026-11-17 10:10:54 | [jeffersongoncalves/filament-lgpd-minors](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-lgpd-minors) | 2.0.0 |  |  |
| 2026-11-17 10:11:23 | [itmosoft/laravel-activity-timeline](https://www.nuget.org/packages/itmosoft%2Flaravel-activity-timeline) | v1.0.0 |  | Polymorphic activity feed and chronological event timeline for Laravel models,… |
| 2026-11-17 10:15:57 | [itmosoft/laravel-affiliate-marketing](https://www.nuget.org/packages/itmosoft%2Flaravel-affiliate-marketing) | v1.0.0 |  | Affiliate program management, conversion attribution, and commission calculatio… |
| 2026-11-17 10:19:45 | [itmosoft/laravel-approvals](https://www.nuget.org/packages/itmosoft%2Flaravel-approvals) | v1.0.0 |  | Sequential, multi-step approval workflows for Laravel models and business proce… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
