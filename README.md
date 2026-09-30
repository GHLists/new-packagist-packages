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

## Latest list — 2026-09-30 05:21 UTC

New packages created between 2026-09-30 04:19 UTC and 2026-09-30 05:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T05-21-46-269152Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 04:21:32 | [mage2kishan/module-performance-optimizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-performance-optimizer) | 1.0.9 | Kishan Savaliya | Frontend performance optimizations for Magento 2 — script deferral, font-displa… |
| 2026-09-30 04:34:06 | [mage2kishan/module-product-slider](https://www.nuget.org/packages/mage2kishan%2Fmodule-product-slider) | 1.0.10 |  | Advanced Product Slider widget with extensive customization options for Magento… |
| 2026-09-30 04:38:54 | [mage2kishan/module-producttabs](https://www.nuget.org/packages/mage2kishan%2Fmodule-producttabs) | 1.0.10 | Kishan Savaliya | Product detail page tab customization for Magento 2. Supports horizontal/vertic… |
| 2026-09-30 04:44:59 | [mage2kishan/module-productgallery](https://www.nuget.org/packages/mage2kishan%2Fmodule-productgallery) | 1.0.10 | Kishan Savaliya | Custom product image gallery for Magento 2 product detail pages. Features confi… |
| 2026-09-30 04:53:44 | [mage2kishan/module-robots-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-robots-seo) | 1.2.3 | Kishan Savaliya | Panth Robots SEO — dedicated robots.txt, X-Robots-Tag, and LLM-bot (GPTBot, Cla… |
| 2026-09-30 04:59:27 | [mercanpay/mercanpay-php](https://www.nuget.org/packages/mercanpay%2Fmercanpay-php) | v1.0.0 | MercanPay | Official PHP client for the MercanPay crypto payment gateway (TRX & USDT-TRC20) |
| 2026-09-30 04:59:44 | [mage2kishan/module-search-autocomplete](https://www.nuget.org/packages/mage2kishan%2Fmodule-search-autocomplete) | 1.0.10 | Kishan Savaliya | Engine-agnostic, bot-hardened, cached search autocomplete for Magento 2 and Hyv… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
