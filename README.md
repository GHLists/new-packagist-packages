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

## Latest list — 2026-10-01 19:20 UTC

New packages created between 2026-10-01 18:19 UTC and 2026-10-01 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T19-20-39-416851Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 18:24:08 | [mage2kishan/module-xml-sitemap](https://www.nuget.org/packages/mage2kishan%2Fmodule-xml-sitemap) | 1.2.2 | Kishan Savaliya | Panth XML Sitemap — sharded XML sitemap generator for Magento 2: per-store prof… |
| 2026-10-01 18:27:22 | [mage2kishan/module-pagebuilder-ai](https://www.nuget.org/packages/mage2kishan%2Fmodule-pagebuilder-ai) | 1.2.23 | Kishan Savaliya | Adds an AI Content button to the Magento PageBuilder toolbar and inline AI butt… |
| 2026-10-01 18:30:26 | [mage2kishan/module-error-monitor](https://www.nuget.org/packages/mage2kishan%2Fmodule-error-monitor) | 1.6.1 | Kishan Savaliya | Panth Error Monitor - smart, secure error management for Magento 2. Captures PH… |
| 2026-10-01 18:31:03 | [olorunda/laravel-zoho-cpaas](https://www.nuget.org/packages/olorunda%2Flaravel-zoho-cpaas) | v1.0.1 | Olorunda | Comprehensive Laravel package for Zoho CPaaS & ZeptoMail: Transactional Email A… |
| 2026-10-01 18:33:37 | [mage2kishan/module-indexer-manager](https://www.nuget.org/packages/mage2kishan%2Fmodule-indexer-manager) | 1.2.1 | Kishan Savaliya | Panth Indexer Manager — reindex Magento 2 from the admin with strategy options… |
| 2026-10-01 18:36:33 | [mage2kishan/module-performance-debugger](https://www.nuget.org/packages/mage2kishan%2Fmodule-performance-debugger) | 1.1.1 | Kishan Savaliya | Production-grade Magento 2 frontend performance debugger and profiler. Tracks b… |
| 2026-10-01 18:39:47 | [mage2kishan/module-malware-scanner](https://www.nuget.org/packages/mage2kishan%2Fmodule-malware-scanner) | 1.3.2 | Kishan Savaliya | Active malware prevention + on-disk scanner for Magento 2. Three real-time guar… |
| 2026-10-01 18:40:47 | [fundrik/core](https://www.nuget.org/packages/fundrik%2Fcore) | v1.0.0 | Denis Yanchevskiy | Core library for the Fundrik fundraising solution |
| 2026-10-01 18:42:49 | [mage2kishan/module-order-cleanup](https://www.nuget.org/packages/mage2kishan%2Fmodule-order-cleanup) | 1.0.11 | Kishan Savaliya | Panth Order Cleanup — safely delete test orders, invoices, shipments, and credi… |
| 2026-10-01 18:46:05 | [mage2kishan/module-mega-menu](https://www.nuget.org/packages/mage2kishan%2Fmodule-mega-menu) | 1.0.16 | Kishan Savaliya | Advanced mega menu for Magento 2 — works on Hyva and Luma. Drag-and-drop tree b… |
| 2026-10-01 18:49:38 | [mage2kishan/module-blog](https://www.nuget.org/packages/mage2kishan%2Fmodule-blog) | 1.3.5 | Kishan Savaliya | Panth_Blog - SEO-grade blog module for Magento 2 with first-class AEO/AIO suppo… |
| 2026-10-01 19:14:25 | [mike-bronner/flux-fontawesome-icons](https://www.nuget.org/packages/mike-bronner%2Fflux-fontawesome-icons) | 0.1.0 | Mike Bronner | Convert FontAwesome SVG icons to Flux Blade icon components for Laravel apps. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
