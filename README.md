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

## Latest list — 2026-10-04 06:22 UTC

New packages created between 2026-10-04 05:19 UTC and 2026-10-04 06:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T06-22-40-535941Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 05:34:51 | [mage2kishan/module-html-sitemap](https://www.nuget.org/packages/mage2kishan%2Fmodule-html-sitemap) | 1.0.18 |  | Theme-agnostic HTML sitemap page for Magento 2 (Hyva + Luma). Renders categorie… |
| 2026-10-04 05:53:05 | [sendertr/sendertr-php](https://www.nuget.org/packages/sendertr%2Fsendertr-php) | v1.0.0 |  | SenderTR işlemsel e-posta ve pazarlama API istemcisi (resmî PHP SDK) |
| 2026-10-04 05:56:55 | [mage2kishan/module-order-cleanup](https://www.nuget.org/packages/mage2kishan%2Fmodule-order-cleanup) | 1.0.13 | Kishan Savaliya | Panth Order Cleanup — safely delete test orders, invoices, shipments, and credi… |
| 2026-10-04 06:19:31 | [mage2kishan/module-imageoptimizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-imageoptimizer) | 1.0.11 | Kishan Savaliya | Frontend image performance: lazy loading (Native/IntersectionObserver/Hybrid),… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
