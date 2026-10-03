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

## Latest list — 2026-10-03 09:21 UTC

New packages created between 2026-10-03 08:21 UTC and 2026-10-03 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T09-21-11-713414Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 08:43:28 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.7 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |
| 2026-10-03 08:43:44 | [yasser-elgammal/tabby-php](https://www.nuget.org/packages/yasser-elgammal%2Ftabby-php) | v1.0.0 |  | A production-ready, framework-agnostic PHP SDK for Tabby. |
| 2026-10-03 09:03:34 | [mage2kishan/module-smart-badge](https://www.nuget.org/packages/mage2kishan%2Fmodule-smart-badge) | 1.1.5 |  | Smart Product Badge & Label System - Automatically displays beautiful badges on… |
| 2026-10-03 09:07:00 | [mage2kishan/module-advancedcart](https://www.nuget.org/packages/mage2kishan%2Fmodule-advancedcart) | 1.0.14 |  | Advanced Cart Page Enhancements - Free shipping bar, qty buttons, trust badges,… |
| 2026-10-03 09:13:19 | [debug404/laravel-ranker](https://www.nuget.org/packages/debug404%2Flaravel-ranker) | v1.0.0 | debug404 | High-performance Eloquent drag-and-drop item sorting and reordering package for… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
