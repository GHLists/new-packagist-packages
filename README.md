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

## Latest list — 2026-10-22 14:20 UTC

New packages created between 2026-10-22 13:19 UTC and 2026-10-22 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T14-20-17-454449Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 13:21:46 | [psbits/scanner](https://www.nuget.org/packages/psbits%2Fscanner) | 0.1.0-alpha | Daniel Ablass | Reusable scanner API and frontend component for barcode scanning |
| 2026-10-22 13:27:26 | [agrekom/filter-url-alias-module](https://www.nuget.org/packages/agrekom%2Ffilter-url-alias-module) | v1.1.0 |  | Agrekom Filter URL Alias Module - translatable layered navigation filter URL pa… |
| 2026-10-22 13:28:22 | [nafiur/laravel-web-analytics](https://www.nuget.org/packages/nafiur%2Flaravel-web-analytics) | v1.0.1 | Nafiur Rahman | High-performance Web Traffic & Visitor Analytics Dashboard for Laravel with rea… |
| 2026-10-22 13:28:32 | [considbrs-webdev/modularity-latest-events](https://www.nuget.org/packages/considbrs-webdev%2Fmodularity-latest-events) | v1.0.0 | Considbrs-Webdev | Modularity Latest Events Module |
| 2026-10-22 13:33:25 | [pharaonic/livewire-assistant](https://www.nuget.org/packages/pharaonic%2Flivewire-assistant) | 1.0.0 |  | Shared Blade and JavaScript foundation that binds JavaScript widgets to Livewir… |
| 2026-10-22 13:43:18 | [rflex-spa/analytics-laravel](https://www.nuget.org/packages/rflex-spa%2Fanalytics-laravel) | 0.3.0 | rFlex | Server-side product analytics (PostHog) for rFlex Laravel systems: events, iden… |
| 2026-10-22 13:52:36 | [rekhu/laravel-dev](https://www.nuget.org/packages/rekhu%2Flaravel-dev) | v1.0.0 | Rekhu, a product of Charisma… | Rekhu Builder for Laravel: connects a Laravel app to its agent in a Rekhu accou… |
| 2026-10-22 13:55:40 | [hryvinskyi/magento2-admin-action-log-inventory](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-admin-action-log-inventory) | 1.0.0 | Volodymyr Hryvinskyi | Records per-source stock (quantity and status of each source item) as product c… |
| 2026-10-22 13:58:58 | [blkdem/filament-queue-monitor](https://www.nuget.org/packages/blkdem%2Ffilament-queue-monitor) | v0.1.1 | BlkDem | A lightweight queue monitoring plugin for Filament. Not a replacement for Larav… |
| 2026-10-22 14:11:50 | [ledgehq/ledge-laravel](https://www.nuget.org/packages/ledgehq%2Fledge-laravel) | 1.0.0 |  | Health, uptime, and compliance monitoring for your Laravel applications. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
