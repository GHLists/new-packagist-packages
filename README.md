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

## Latest list — 2026-10-07 06:22 UTC

New packages created between 2026-10-07 05:21 UTC and 2026-10-07 06:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T06-22-21-216177Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 05:36:15 | [mage2kishan/module-search-autocomplete](https://www.nuget.org/packages/mage2kishan%2Fmodule-search-autocomplete) | 1.1.7 | Kishan Savaliya | Engine-agnostic, bot-hardened, cached search autocomplete for Magento 2 and Hyv… |
| 2026-10-07 05:40:02 | [mage2kishan/module-checkout-extended](https://www.nuget.org/packages/mage2kishan%2Fmodule-checkout-extended) | 1.1.10 | Kishan Savaliya | Enhanced one-page checkout for Magento 2 with configurable multi-column layouts… |
| 2026-10-07 05:43:29 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.17 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |
| 2026-10-07 05:46:27 | [medigital-dev/excel-handler](https://www.nuget.org/packages/medigital-dev%2Fexcel-handler) | v1.0.0 | Muhammad Said Latif Ghofari | Library untuk menulis dan membaca excel |
| 2026-10-07 05:47:02 | [mage2kishan/module-sale-filter](https://www.nuget.org/packages/mage2kishan%2Fmodule-sale-filter) | 1.1.6 | Kishan Savaliya | Panth Sale Filter — "On Sale" layered navigation filter for Magento 2, backed b… |
| 2026-10-07 05:49:32 | [bfocus/monitor](https://www.nuget.org/packages/bfocus%2Fmonitor) | v0.1.0 | Berni Software | Monitoramento de erros do bFocus para PHP: captura os erros não tratados e mand… |
| 2026-10-07 05:50:02 | [cipi/sdk](https://www.nuget.org/packages/cipi%2Fsdk) | 1.0 |  | PHP SDK for the Cipi panel API. Call every cipi.sh REST endpoint from PHP, Lara… |
| 2026-10-07 05:51:02 | [mage2kishan/module-mega-menu](https://www.nuget.org/packages/mage2kishan%2Fmodule-mega-menu) | 1.0.22 | Kishan Savaliya | Advanced mega menu for Magento 2 — works on Hyva and Luma. Drag-and-drop tree b… |
| 2026-10-07 05:56:55 | [mage2kishan/module-advanced-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-seo) | 1.8.10 | Kishan Savaliya | Panth Advanced SEO — enterprise-grade SEO suite for Magento 2: SEO dashboard, m… |
| 2026-10-07 06:01:06 | [mage2kishan/module-product-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-product-attachments) | 1.1.8 |  | Product Attachments module for Magento 2 - attach files, links, and documents t… |
| 2026-10-07 06:04:30 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.19 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
