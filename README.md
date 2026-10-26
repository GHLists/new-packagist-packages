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

## Latest list — 2026-10-26 17:22 UTC

New packages created between 2026-10-26 16:20 UTC and 2026-10-26 17:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T17-22-18-694697Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 16:23:03 | [usman-ahmed/laravel-import-export](https://www.nuget.org/packages/usman-ahmed%2Flaravel-import-export) | v1.0.0 | Usman Ahmed | Enterprise-grade metadata-driven Laravel imports, exports, and spreadsheet temp… |
| 2026-10-26 16:25:39 | [valtzu/symfony-websocket-client](https://www.nuget.org/packages/valtzu%2Fsymfony-websocket-client) | 0.1.1 |  | WebSocket client implementing Symfony HttpClientInterface |
| 2026-10-26 16:49:07 | [bbwdadfg/aimetadatacleaner-url-tools](https://www.nuget.org/packages/bbwdadfg%2Faimetadatacleaner-url-tools) | v0.1.0 |  | Offline URL builder for AI Metadata Cleaner image, video, and PDF metadata page… |
| 2026-10-26 16:57:31 | [ggoitea/laravel-argidreader](https://www.nuget.org/packages/ggoitea%2Flaravel-argidreader) | v1.0.0 |  | Laravel package to read Argentine DNI cards from front/back images or PDFs usin… |
| 2026-10-26 17:14:20 | [nyumbani/ui](https://www.nuget.org/packages/nyumbani%2Fui) | v1.0.0 | Alvin Kaburu | The Nyumbani look: layouts, sign-in pages, error pages, components, scripts and… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
