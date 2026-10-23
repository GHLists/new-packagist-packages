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

## Latest list — 2026-10-23 17:21 UTC

New packages created between 2026-10-23 16:22 UTC and 2026-10-23 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T17-21-45-457883Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 16:23:49 | [amjadiqbal/laravel-first-party-analytics](https://www.nuget.org/packages/amjadiqbal%2Flaravel-first-party-analytics) | v0.1.0 | Amjad Iqbal | Self-hosted, privacy-friendly web analytics for Laravel, stored in your own dat… |
| 2026-10-23 16:37:05 | [rapttor/yii2-themes](https://www.nuget.org/packages/rapttor%2Fyii2-themes) | v1.0.0 |  | Per-user themes for Yii2: complete light, dark and soft (neumorphic) colour set… |
| 2026-10-23 16:52:00 | [amjadiqbal/laravel-sql-dashboard](https://www.nuget.org/packages/amjadiqbal%2Flaravel-sql-dashboard) | v0.1.0 | Amjad Iqbal | Read-only SQL dashboard for Laravel (Blazer for Laravel): saved SQL queries wit… |
| 2026-10-23 16:55:41 | [rapttor/legal](https://www.nuget.org/packages/rapttor%2Flegal) | v0.1.0 | Rapttor | Legal page templates (terms, privacy, cookies, acceptable use, imprint, refunds… |
| 2026-10-23 16:55:41 | [rapttor/yii2-legal](https://www.nuget.org/packages/rapttor%2Fyii2-legal) | v0.1.0 | Rapttor | Yii2 extension that publishes legal pages from one company config: terms, priva… |
| 2026-10-23 17:01:51 | [hellocloud/php-resque](https://www.nuget.org/packages/hellocloud%2Fphp-resque) | v3.5.0 | Daniel Mason | Redis backed library for creating background jobs and processing them later. Ba… |
| 2026-10-23 17:05:20 | [rivalex/clearance](https://www.nuget.org/packages/rivalex%2Fclearance) | v1.3.2 | Alessandro Rivolta | A complete admin panel (Livewire 4 + Flux UI) for managing permissions, roles,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
