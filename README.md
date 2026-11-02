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

## Latest list — 2026-11-02 13:21 UTC

New packages created between 2026-11-02 12:21 UTC and 2026-11-02 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T13-21-56-414469Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 12:24:40 | [evo-mark/laravel-actions-ide-helper](https://www.nuget.org/packages/evo-mark%2Flaravel-actions-ide-helper) | v2.0.0 | Craig Riley; Alexander Wulf | Generate a new IDE Helper file for Laravel Actions. |
| 2026-11-02 12:37:55 | [krafsys/vercy-storage](https://www.nuget.org/packages/krafsys%2Fvercy-storage) | v1.0.2 |  | Laravel SDK for Vercy Cloud Storage: upload files and get public URLs with thum… |
| 2026-11-02 12:39:07 | [aaix/laravel-islands-gallery](https://www.nuget.org/packages/aaix%2Flaravel-islands-gallery) | v1.0.0 | Jonas Gnioui | An image gallery for Laravel Islands: an inline carousel with thumbnails and a… |
| 2026-11-02 12:48:23 | [aaix/laravel-archipelago](https://www.nuget.org/packages/aaix%2Flaravel-archipelago) | v1.0.1 | Jonas Gnioui | The whole Laravel Islands set in one install: islands, data grid, search, galle… |
| 2026-11-02 12:50:19 | [sorge-it/cdp-browser-installer](https://www.nuget.org/packages/sorge-it%2Fcdp-browser-installer) | v1.0.0 | Stefan Sorge | Installs a pinned, SHA-256-checked chrome-headless-shell from Chrome for Testin… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
