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

## Latest list — 2026-09-28 13:21 UTC

New packages created between 2026-09-28 12:20 UTC and 2026-09-28 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T13-21-13-990079Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 12:21:03 | [niangpro/niangpro](https://www.nuget.org/packages/niangpro%2Fniangpro) | v2.0.0 |  | Squelette d'application NiangPro : composer create-project niangpro/niangpro mo… |
| 2026-09-28 12:26:04 | [christianjbrown/ebay-sell-fulfillment-api-sdk](https://www.nuget.org/packages/christianjbrown%2Febay-sell-fulfillment-api-sdk) | v1.0.0 | Christian Brown | A strongly-typed PHP 8.5+ client for the eBay Sell Fulfillment API that returns… |
| 2026-09-28 12:44:55 | [hei/laravel-scarlett-player](https://www.nuget.org/packages/hei%2Flaravel-scarlett-player) | v0.1.0 | Hackney Enterprises Inc | The server side of Scarlett Player for Laravel: analytics beacon ingest, clip g… |
| 2026-09-28 12:49:03 | [marshmallow/laravel-odoo](https://www.nuget.org/packages/marshmallow%2Flaravel-odoo) | v0.1.0 | Marshmallow | Laravel client for the Odoo 19+ External JSON-2 API, with per-model resources f… |
| 2026-09-28 12:56:41 | [clearcut/clearcut-laravel](https://www.nuget.org/packages/clearcut%2Fclearcut-laravel) | v1.0.1 |  | Laravel client for a clearcut-video service: watermarking and PII redaction for… |
| 2026-09-28 13:13:09 | [webx-ui/module-tariffs](https://www.nuget.org/packages/webx-ui%2Fmodule-tariffs) | v0.48.0 | WebX UI | Tariffs for the WebX UI admin panel: price cards with a badge, a price in a cur… |
| 2026-09-28 13:13:21 | [webx-ui/module-vacancies](https://www.nuget.org/packages/webx-ui%2Fmodule-vacancies) | v0.48.0 | WebX UI | Vacancies for the WebX UI admin panel: open positions with the place, the kind… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
