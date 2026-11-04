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

## Latest list — 2026-11-04 07:21 UTC

New packages created between 2026-11-04 06:21 UTC and 2026-11-04 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T07-21-09-457881Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 06:30:57 | [itmosoft/laravel-api-response](https://www.nuget.org/packages/itmosoft%2Flaravel-api-response) | v1.0.1 |  | Consistent, configurable JSON API responses for Laravel applications. |
| 2026-11-04 06:49:13 | [zcoders/zauth](https://www.nuget.org/packages/zcoders%2Fzauth) | 1.0.0 |  |  |
| 2026-11-04 06:51:49 | [nouxwell/cipher-layer](https://www.nuget.org/packages/nouxwell%2Fcipher-layer) | v0.1.0 | Hüseyin Balın | Field-level encryption, blind-index search, streaming file encryption and key l… |
| 2026-11-04 06:57:46 | [jurager/eav](https://www.nuget.org/packages/jurager%2Feav) | 1.0.0 | Yuri Gerassimov | Flexible Entity-Attribute-Value (EAV) system for Laravel with typed storage, lo… |
| 2026-11-04 07:04:50 | [webx-ui/module-delivery](https://www.nuget.org/packages/webx-ui%2Fmodule-delivery) | v0.92.0 | WebX UI | Delivery for a WebX UI shop: the registry of method types and carriers, the sho… |
| 2026-11-04 07:05:02 | [webx-ui/delivery-novaposhta](https://www.nuget.org/packages/webx-ui%2Fdelivery-novaposhta) | v0.92.0 | WebX UI | Nova Poshta for WebX UI delivery: the carrier, its key and sender settings, a t… |
| 2026-11-04 07:05:06 | [webx-ui/geography](https://www.nuget.org/packages/webx-ui%2Fgeography) | v0.92.0 | WebX UI | The shared geography of a WebX UI site: countries, regions and localities in th… |
| 2026-11-04 07:05:11 | [webx-ui/module-payments](https://www.nuget.org/packages/webx-ui%2Fmodule-payments) | v0.92.0 | WebX UI | Payments for a WebX UI shop: the methods of the site, the attempts to pay an or… |
| 2026-11-04 07:11:45 | [itmosoft/laravel-query-filters](https://www.nuget.org/packages/itmosoft%2Flaravel-query-filters) | v1.0.0 |  | A lightweight, allowlist-based query filtering, searching, and sorting package… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
