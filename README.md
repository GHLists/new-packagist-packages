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

## Latest list — 2026-11-26 17:22 UTC

New packages created between 2026-11-26 16:19 UTC and 2026-11-26 17:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T17-22-04-322508Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 16:49:13 | [backsystem/base](https://www.nuget.org/packages/backsystem%2Fbase) | v1.0.95 |  |  |
| 2026-11-26 17:06:29 | [cart-recovery/module-abandoned-cart](https://www.nuget.org/packages/cart-recovery%2Fmodule-abandoned-cart) | v1.0.0 |  | Configurable abandoned cart recovery emails for Magento Open Source and Adobe C… |
| 2026-11-26 17:16:38 | [considbrs-webdev/revisionary-municipio-frontend](https://www.nuget.org/packages/considbrs-webdev%2Frevisionary-municipio-frontend) | 1.0.2 |  | Simplified front-end experience for the revisor role (Revisionary) on Municipio… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
