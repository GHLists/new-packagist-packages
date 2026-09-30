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

## Latest list — 2026-09-30 11:18 UTC

New packages created between 2026-09-30 10:21 UTC and 2026-09-30 11:18 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T11-18-55-30433Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 10:24:06 | [eekes/sulu-image-optimizer-bundle](https://www.nuget.org/packages/eekes%2Fsulu-image-optimizer-bundle) | v1.0.0 | Ewald Vanderveken | Optimizes and resizes images before they are stored in the Sulu media library,… |
| 2026-09-30 10:24:30 | [kaveraa/api-gouv-publique-fr](https://www.nuget.org/packages/kaveraa%2Fapi-gouv-publique-fr) | v0.1.0 | Augustin Kavera | Typed PHP client for French public APIs (company search and address) with a Lar… |
| 2026-09-30 10:52:34 | [mage2kishan/module-error-monitor](https://www.nuget.org/packages/mage2kishan%2Fmodule-error-monitor) | 1.6.0 | Kishan Savaliya | Panth Error Monitor - smart, secure error management for Magento 2. Captures PH… |
| 2026-09-30 10:56:44 | [mage2kishan/module-admin-menu-manager](https://www.nuget.org/packages/mage2kishan%2Fmodule-admin-menu-manager) | 1.0.12 | Kishan Savaliya | Customises the Magento 2 backend menu — hide, rename, re-icon, recolor, reorder… |
| 2026-09-30 11:00:03 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.0 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |
| 2026-09-30 11:01:50 | [ffans/paste-link](https://www.nuget.org/packages/ffans%2Fpaste-link) | v1.0.0 | Golden; FFans | Turn selected text into a Markdown link by pasting a URL in Flarum's default co… |
| 2026-09-30 11:05:37 | [mage2kishan/module-blog](https://www.nuget.org/packages/mage2kishan%2Fmodule-blog) | 1.2.0 | Kishan Savaliya | Panth_Blog - SEO-grade blog module for Magento 2 with first-class AEO/AIO suppo… |
| 2026-09-30 11:07:30 | [curly-deni/laravel-maintenance](https://www.nuget.org/packages/curly-deni%2Flaravel-maintenance) | 1.0 | Danila Mikhalev | Maintenance windows and runtime availability for Laravel applications. |
| 2026-09-30 11:12:14 | [mage2kishan/module-xml-sitemap](https://www.nuget.org/packages/mage2kishan%2Fmodule-xml-sitemap) | 1.2.0 | Kishan Savaliya | Panth XML Sitemap — sharded XML sitemap generator for Magento 2: per-store prof… |
| 2026-09-30 11:18:12 | [mage2kishan/module-product-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-product-attachments) | 1.1.0 |  | Product Attachments module for Magento 2 - attach files, links, and documents t… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
