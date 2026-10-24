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

## Latest list — 2026-10-24 17:27 UTC

New packages created between 2026-10-24 16:22 UTC and 2026-10-24 17:27 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T17-27-35-205314Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 16:23:52 | [io/charts](https://www.nuget.org/packages/io%2Fcharts) | v0.1.0 |  | Server-rendered SVG charts for Io: bar and line charts with a data table, legen… |
| 2026-10-24 16:23:52 | [io/discord](https://www.nuget.org/packages/io%2Fdiscord) | v0.1.0 |  | Discord bots in Io apps: slash commands, buttons, modals and events as attribut… |
| 2026-10-24 16:23:52 | [io/export](https://www.nuget.org/packages/io%2Fexport) | v0.1.0 |  | Table downloads for Io: return a Sheet from a route and get CSV, JSON Lines, HT… |
| 2026-10-24 16:23:52 | [io/export-fixed](https://www.nuget.org/packages/io%2Fexport-fixed) | v0.1.0 |  | Fixed-width record files for io-export: #[Fixed] column layouts, Windows-1252 o… |
| 2026-10-24 16:23:52 | [io/flash](https://www.nuget.org/packages/io%2Fflash) | v0.1.0 |  | Flash messages for Io: queue a message, redirect, show it once on the next page… |
| 2026-10-24 16:23:52 | [io/framework](https://www.nuget.org/packages/io%2Fframework) | v0.1.0 | Lento Leisenfeld | A lightweight PHP framework for building APIs and server-rendered UIs, with att… |
| 2026-10-24 16:23:52 | [io/i18n](https://www.nuget.org/packages/io%2Fi18n) | v0.1.0 |  | Translations and per-request locale for Io: catalogs, {placeholder} and plural… |
| 2026-10-24 16:23:52 | [io/live](https://www.nuget.org/packages/io%2Flive) | v0.1.0 |  | Live components for Io under Tenma: server-side PHP components, events and rend… |
| 2026-10-24 16:33:33 | [kdpika/license-sdk](https://www.nuget.org/packages/kdpika%2Flicense-sdk) | v1.0.1 |  | Official KDPika Licensing SDK for PHP |
| 2026-10-24 16:33:47 | [mercadons/zf1](https://www.nuget.org/packages/mercadons%2Fzf1) | 2.0.0-RC1 |  | Maintained fork of Zend Framework 1 for modern PHP (7.4 – 8.4). |
| 2026-10-24 16:37:47 | [specrig/laravel](https://www.nuget.org/packages/specrig%2Flaravel) | v0.1.0 |  | specrig for a Laravel service: the application booted per case, its HTTP client… |
| 2026-10-24 16:43:44 | [specrig/symfony](https://www.nuget.org/packages/specrig%2Fsymfony) | v0.1.0 |  | specrig for a Symfony service: the kernel booted per case, its HTTP client, tra… |
| 2026-10-24 16:44:55 | [habeuk/habeuk_base_symfony](https://www.nuget.org/packages/habeuk%2Fhabeuk_base_symfony) | 1.0.0 | kouwa stephane | contient les classes de bases permettant d'avoir une base commune pour les proj… |
| 2026-10-24 16:45:17 | [drupal/varbase_ai_vdb_mariadb](https://www.nuget.org/packages/drupal%2Fvarbase_ai_vdb_mariadb) | 1.0.0-alpha1 | Vardot | Uses MariaDB 11.7 or later as the vector database for Varbase AI Search, in the… |
| 2026-10-24 17:03:46 | [specrig/specrig](https://www.nuget.org/packages/specrig%2Fspecrig) | v0.1.0 |  | The core of specrig for PHP: the harness, the stand-ins, the contract check, th… |
| 2026-10-24 17:07:32 | [phoenix1331/filament-jev-moderation](https://www.nuget.org/packages/phoenix1331%2Ffilament-jev-moderation) | v0.1.0 | Darren Williams | A Filament review queue for Jev Moderation: approve, reject and reclassify flag… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
