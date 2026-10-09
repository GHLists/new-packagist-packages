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

## Latest list — 2026-10-09 13:18 UTC

New packages created between 2026-10-09 12:20 UTC and 2026-10-09 13:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T13-18-55-511583Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 12:31:11 | [wexample/symfony-payment-ds](https://www.nuget.org/packages/wexample%2Fsymfony-payment-ds) | 1.0.1 |  |  |
| 2026-10-09 12:32:03 | [wexample/symfony-payment-demo](https://www.nuget.org/packages/wexample%2Fsymfony-payment-demo) | 1.0.1 |  |  |
| 2026-10-09 12:35:51 | [mazdel/dayravel](https://www.nuget.org/packages/mazdel%2Fdayravel) | v1.0.0 |  | Laravel module scaffolding commands with automatic module route discovery. |
| 2026-10-09 12:36:01 | [iyzico/kolai-php](https://www.nuget.org/packages/iyzico%2Fkolai-php) | v1.0.0 | iyzico and contributors | Kolai e-ticaret entegrasyonlari icin platformdan bagimsiz cekirdek: HMAC auth,… |
| 2026-10-09 12:42:35 | [jengo/pesa](https://www.nuget.org/packages/jengo%2Fpesa) | v0.1.0 | Ian Ochieng | Unified multi-gateway payment processing subsystem for CodeIgniter 4 and the Je… |
| 2026-10-09 12:47:09 | [pollora/debugbar](https://www.nuget.org/packages/pollora%2Fdebugbar) | v1.0.0 | Amphibee | Laravel Debugbar for Pollora: WordPress queries, hooks, the template hierarchy… |
| 2026-10-09 12:51:55 | [zofe/theme-desk](https://www.nuget.org/packages/zofe%2Ftheme-desk) | v0.1.0 |  | Desk theme for rapyd-admin: the classic admin look (blue sidebar, off-white con… |
| 2026-10-09 13:02:36 | [semitexa/laravel-ai-verify](https://www.nuget.org/packages/semitexa%2Flaravel-ai-verify) | v0.2.0 | Semitexa | Diff-aware verification for AI coding agents in Laravel: one Artisan command pl… |
| 2026-10-09 13:06:38 | [erfanvahabpour/laravel-jalali-schedule](https://www.nuget.org/packages/erfanvahabpour%2Flaravel-jalali-schedule) | v1.0.0 | Erfan Vahabpour | Seamless Jalali (Solar Hijri) scheduling macros for Laravel tasks and console c… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
