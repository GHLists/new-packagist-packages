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

## Latest list — 2026-10-05 21:20 UTC

New packages created between 2026-10-05 20:20 UTC and 2026-10-05 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T21-20-17-697124Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 20:25:00 | [mage2kishan/module-xml-sitemap](https://www.nuget.org/packages/mage2kishan%2Fmodule-xml-sitemap) | 1.2.8 | Kishan Savaliya | Panth XML Sitemap — sharded XML sitemap generator for Magento 2: per-store prof… |
| 2026-10-05 20:28:33 | [mage2kishan/module-robots-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-robots-seo) | 1.3.6 | Kishan Savaliya | Panth Robots SEO — dedicated robots.txt, X-Robots-Tag, and LLM-bot (GPTBot, Cla… |
| 2026-10-05 20:32:01 | [mage2kishan/module-llms-txt](https://www.nuget.org/packages/mage2kishan%2Fmodule-llms-txt) | 1.5.6 | Kishan Savaliya | Panth LLMs.txt — AI Indexing Engine for Magento 2. Serves structured /llms.txt,… |
| 2026-10-05 20:35:33 | [mage2kishan/module-filter-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-filter-seo) | 1.1.7 | Kishan Savaliya | Panth Filter SEO — clean path-based URLs for layered navigation filters + dynam… |
| 2026-10-05 20:44:34 | [mage2kishan/module-redirects](https://www.nuget.org/packages/mage2kishan%2Fmodule-redirects) | 1.2.7 |  | Redirects and 404 management for Magento 2 (Hyva + Luma). Manual + auto redirec… |
| 2026-10-05 20:48:35 | [mage2kishan/module-mage-pos](https://www.nuget.org/packages/mage2kishan%2Fmodule-mage-pos) | 1.0.15 | Kishan Savaliya | Panth MagePos - a full point of sale (POS) for Magento 2. Standalone touch-frie… |
| 2026-10-05 20:52:04 | [mage2kishan/module-eu-withdrawal](https://www.nuget.org/packages/mage2kishan%2Fmodule-eu-withdrawal) | 1.1.10 | Kishan Savaliya | Panth EU Withdrawal Button - a clear, accessible digital withdrawal (cancellati… |
| 2026-10-05 20:55:27 | [mage2kishan/module-checkout-extended](https://www.nuget.org/packages/mage2kishan%2Fmodule-checkout-extended) | 1.1.9 | Kishan Savaliya | Enhanced one-page checkout for Magento 2 with configurable multi-column layouts… |
| 2026-10-05 20:58:45 | [mage2kishan/module-productgallery](https://www.nuget.org/packages/mage2kishan%2Fmodule-productgallery) | 1.0.15 | Kishan Savaliya | Custom product image gallery for Magento 2 product detail pages. Features confi… |
| 2026-10-05 21:02:09 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.14 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |
| 2026-10-05 21:04:14 | [akanyuk/chromephp](https://www.nuget.org/packages/akanyuk%2Fchromephp) | v1.0.0 | Andrey Marinov | Fork of ccampbell/chromephp with PHP >=8.2 supported. Log variables to the Chro… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
