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

## Latest list — 2026-10-17 22:21 UTC

New packages created between 2026-10-17 21:20 UTC and 2026-10-17 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T22-21-32-539704Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 21:28:34 | [openpx/sdk](https://www.nuget.org/packages/openpx%2Fsdk) | v0.0.1 | OpenPX | OpenPX SDK (early release): the OpenPX schema for describing products once and… |
| 2026-10-17 21:28:37 | [openpx/cli](https://www.nuget.org/packages/openpx%2Fcli) | v0.0.1 | OpenPX | OpenPX command line (early release). |
| 2026-10-17 21:33:43 | [brocode/magento-patches](https://www.nuget.org/packages/brocode%2Fmagento-patches) | 1.0.0 | Benjamin Rosenberger | Composer commands to add Magento 2 security, quality and custom patches safely:… |
| 2026-10-17 21:34:22 | [mmhospedagem/mvo-whats-php](https://www.nuget.org/packages/mmhospedagem%2Fmvo-whats-php) | v1.0.1 | MVO | Biblioteca PHP nativa para WhatsApp: QR Code, sessões persistentes, mensagens,… |
| 2026-10-17 22:01:09 | [nickwelsh/zero-for-laravel](https://www.nuget.org/packages/nickwelsh%2Fzero-for-laravel) | v0.1.0 |  | Laravel-owned model contracts, queries and CRUD for Rocicorp Zero. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
