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

## Latest list — 2026-11-17 05:20 UTC

New packages created between 2026-11-17 04:19 UTC and 2026-11-17 05:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T05-20-00-299552Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 04:37:08 | [current/current](https://www.nuget.org/packages/current%2Fcurrent) | v0.3.0 |  | One description of a Laravel application's experience: pages, breadcrumbs, and… |
| 2026-11-17 04:37:08 | [current/inertia](https://www.nuget.org/packages/current%2Finertia) | v0.2.0 |  | Share Current pages, breadcrumbs, and menus with Inertia, with TypeScript types. |
| 2026-11-17 04:44:51 | [starbug/shipping-boxes](https://www.nuget.org/packages/starbug%2Fshipping-boxes) | v0.9.0 | Ali Gangji | Shipping box dimensions. |
| 2026-11-17 04:45:14 | [starbug/box-packer](https://www.nuget.org/packages/starbug%2Fbox-packer) | v0.9.0 | Ali Gangji | Box packing for products. |
| 2026-11-17 04:45:21 | [starbug/box-packer-admin](https://www.nuget.org/packages/starbug%2Fbox-packer-admin) | v0.9.1 | Ali Gangji | Admin screen for packing shipments. |
| 2026-11-17 05:01:19 | [starbug/cart](https://www.nuget.org/packages/starbug%2Fcart) | v0.9.1 | Ali Gangji | Shopping cart built on orders. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
