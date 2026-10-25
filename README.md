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

## Latest list — 2026-10-25 14:20 UTC

New packages created between 2026-10-25 13:20 UTC and 2026-10-25 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T14-20-42-901035Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 13:25:47 | [survos/document-processing](https://www.nuget.org/packages/survos%2Fdocument-processing) | 2.43.18 |  | Typed Files and OCR client for Mistral-compatible document services. |
| 2026-10-25 13:25:51 | [survos/document-processing-bundle](https://www.nuget.org/packages/survos%2Fdocument-processing-bundle) | 2.43.18 |  | Named document-processing clients and credentials for Symfony. |
| 2026-10-25 13:28:09 | [marcosmarcolin/socket.io-server](https://www.nuget.org/packages/marcosmarcolin%2Fsocket.io-server) | v0.2.0 | Marcos Marcolin | Socket.IO v4 server for PHP, built on Workerman |
| 2026-10-25 13:45:38 | [renfire/tbp](https://www.nuget.org/packages/renfire%2Ftbp) | v1.1.1 | Marc Clausell; Bitendian S.L. | Light component-oriented PHP framework for small and medium websites |
| 2026-10-25 13:48:53 | [machinjiri/advocate](https://www.nuget.org/packages/machinjiri%2Fadvocate) | 1.0.0 | Precious Lyson; Mlangeni Group | Testing Suite for Machinjiri Framework |
| 2026-10-25 14:01:23 | [lunixi/php-sdk](https://www.nuget.org/packages/lunixi%2Fphp-sdk) | v0.28.1 | Lunixi | Lunixi payment gateway PHP SDK — framework-agnostic client for payments, webhoo… |
| 2026-10-25 14:02:58 | [tacraft-sociality/flarum-scroll-buttons](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-scroll-buttons) | 1.0.0 | TaCraft Sociality | Add scroll up and scroll down buttons. |
| 2026-10-25 14:14:36 | [lunixi/laravel](https://www.nuget.org/packages/lunixi%2Flaravel) | v0.1.0 | Lunixi | Laravel integration for the Lunixi PHP SDK — configuration, container bindings,… |
| 2026-10-25 14:17:04 | [tacraft-sociality/flarum-id-slug](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-id-slug) | 1.0.0 | TaCraft-Sociality | Use id as slug in discussion URL. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
