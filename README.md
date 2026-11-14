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

## Latest list — 2026-11-14 09:20 UTC

New packages created between 2026-11-14 08:19 UTC and 2026-11-14 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T09-20-12-714172Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 08:24:52 | [itmosoft/laravel-product-variants](https://www.nuget.org/packages/itmosoft%2Flaravel-product-variants) | v1.0.0 |  | Product variants, SKUs, option values and price overrides for Laravel eCommerce… |
| 2026-11-14 08:28:36 | [musqet/vendor-reservation](https://www.nuget.org/packages/musqet%2Fvendor-reservation) | v1.0.0 | Musqet Limited | Reserves the musqet vendor name on Packagist. Musqet's Magento modules are not… |
| 2026-11-14 09:02:00 | [pharaonic/laravel-reacts](https://www.nuget.org/packages/pharaonic%2Flaravel-reacts) | 13.0.0 | Moamen Eltouny (Raggi) | Polymorphic emoji reactions for Laravel Eloquent models, with registered types,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
