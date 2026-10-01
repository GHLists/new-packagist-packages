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

## Latest list — 2026-10-01 07:21 UTC

New packages created between 2026-10-01 06:19 UTC and 2026-10-01 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T07-21-55-743411Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 06:20:20 | [mage2kishan/module-structured-data](https://www.nuget.org/packages/mage2kishan%2Fmodule-structured-data) | 1.3.1 | Kishan Savaliya | Panth Structured Data — JSON-LD schemas for Magento 2: Product, Breadcrumb, Org… |
| 2026-10-01 06:26:07 | [mage2kishan/module-testimonials](https://www.nuget.org/packages/mage2kishan%2Fmodule-testimonials) | 1.2.1 |  | Advanced Testimonials module with slider, individual pages, categories, SEO, an… |
| 2026-10-01 06:30:50 | [mage2kishan/module-whatsapp](https://www.nuget.org/packages/mage2kishan%2Fmodule-whatsapp) | 1.0.11 | Kishan Savaliya | WhatsApp Integration for Magento 2 — floating chat button, product page inquiry… |
| 2026-10-01 06:36:53 | [mage2kishan/module-xml-sitemap](https://www.nuget.org/packages/mage2kishan%2Fmodule-xml-sitemap) | 1.2.1 | Kishan Savaliya | Panth XML Sitemap — sharded XML sitemap generator for Magento 2: per-store prof… |
| 2026-10-01 06:37:08 | [cognesy/instructor-retrieval](https://www.nuget.org/packages/cognesy%2Finstructor-retrieval) | v2.12.0 |  | Vector storage, indexing, and retrieval for InstructorPHP |
| 2026-10-01 06:42:39 | [mage2kishan/module-producttabs](https://www.nuget.org/packages/mage2kishan%2Fmodule-producttabs) | 1.1.1 | Kishan Savaliya | Product detail page tab customization for Magento 2. Supports horizontal/vertic… |
| 2026-10-01 06:48:11 | [mage2kishan/module-blog](https://www.nuget.org/packages/mage2kishan%2Fmodule-blog) | 1.3.0 | Kishan Savaliya | Panth_Blog - SEO-grade blog module for Magento 2 with first-class AEO/AIO suppo… |
| 2026-10-01 06:52:01 | [mage2kishan/module-search-autocomplete](https://www.nuget.org/packages/mage2kishan%2Fmodule-search-autocomplete) | 1.1.1 | Kishan Savaliya | Engine-agnostic, bot-hardened, cached search autocomplete for Magento 2 and Hyv… |
| 2026-10-01 07:14:39 | [synergizeflow/laravel-onboarding](https://www.nuget.org/packages/synergizeflow%2Flaravel-onboarding) | v1.0.0 |  | SynergizeFlow core client and onboarding package for Laravel |
| 2026-10-01 07:17:03 | [synergizeflow/laravel-onboarding-blog](https://www.nuget.org/packages/synergizeflow%2Flaravel-onboarding-blog) | v1.0.0 |  | Headless blog addon package for SynergizeFlow Laravel integration |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
