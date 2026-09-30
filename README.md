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

## Latest list — 2026-09-30 00:20 UTC

New packages created between 2026-09-29 23:19 UTC and 2026-09-30 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T00-20-54-458841Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 23:28:50 | [upturnstudio/module-smart-categories](https://www.nuget.org/packages/upturnstudio%2Fmodule-smart-categories) | 1.0.0 | Brideo | Smart categories for Magento 2 — rule-driven category membership, recomputed on… |
| 2026-09-29 23:29:29 | [connectmedia/laravel](https://www.nuget.org/packages/connectmedia%2Flaravel) | v1.0.0 | Connect Media | Laravel integration for the Connect Media SMS API: send bulk and transactional… |
| 2026-09-29 23:30:52 | [mage2kishan/module-hero-slider](https://www.nuget.org/packages/mage2kishan%2Fmodule-hero-slider) | 1.0.11 | Kishan Savaliya | Hero / homepage carousel for Magento 2 (Hyva + Luma). Center-focused 3-up Splid… |
| 2026-09-29 23:49:49 | [mage2kishan/module-hreflang](https://www.nuget.org/packages/mage2kishan%2Fmodule-hreflang) | 1.0.19 | Kishan Savaliya | Panth Hreflang — multi-language/multi-region hreflang link tags for Magento 2 w… |
| 2026-09-30 00:07:12 | [mage2kishan/module-html-sitemap](https://www.nuget.org/packages/mage2kishan%2Fmodule-html-sitemap) | 1.0.13 |  | Theme-agnostic HTML sitemap page for Magento 2 (Hyva + Luma). Renders categorie… |
| 2026-09-30 00:18:14 | [mage2kishan/module-imageoptimizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-imageoptimizer) | 1.0.9 | Kishan Savaliya | Frontend image performance: lazy loading (Native/IntersectionObserver/Hybrid),… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
