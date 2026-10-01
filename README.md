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

## Latest list — 2026-10-01 22:22 UTC

New packages created between 2026-10-01 21:19 UTC and 2026-10-01 22:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T22-22-40-538989Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 21:52:06 | [kevinpirnie/kpt-cache](https://www.nuget.org/packages/kevinpirnie%2Fkpt-cache) | v1.1.32 | Kevin Pirnie | Modern Multi-Tier PHP Caching System with automatic tier discovery, connection… |
| 2026-10-01 21:58:06 | [mage2kishan/module-pagebuilder-ai](https://www.nuget.org/packages/mage2kishan%2Fmodule-pagebuilder-ai) | 1.2.24 | Kishan Savaliya | Adds an AI Content button to the Magento PageBuilder toolbar and inline AI butt… |
| 2026-10-01 22:01:25 | [mage2kishan/module-sale-filter](https://www.nuget.org/packages/mage2kishan%2Fmodule-sale-filter) | 1.1.3 | Kishan Savaliya | Panth Sale Filter — "On Sale" layered navigation filter for Magento 2, backed b… |
| 2026-10-01 22:04:25 | [mage2kishan/module-extra-fee](https://www.nuget.org/packages/mage2kishan%2Fmodule-extra-fee) | 1.1.4 | Kishan Savaliya | Panth Extra Fee — add configurable extra fees and surcharges to Magento 2 check… |
| 2026-10-01 22:07:17 | [mage2kishan/module-advanced-contact-us](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-contact-us) | 1.1.5 |  | Advanced Contact Us Page - Custom fields, bot protection, submission management… |
| 2026-10-01 22:09:07 | [focalcrm/core](https://www.nuget.org/packages/focalcrm%2Fcore) | v0.1.0 | CaskStack, LLC | Headless CRM Core Engine for Focal (Contacts, Companies, Custom Properties, Ass… |
| 2026-10-01 22:09:07 | [focalcrm/filament](https://www.nuget.org/packages/focalcrm%2Ffilament) | v0.1.0 | CaskStack, LLC | Unified Filament CRM Panel & UI Plugin for Focal |
| 2026-10-01 22:09:07 | [focalcrm/marketing](https://www.nuget.org/packages/focalcrm%2Fmarketing) | v0.1.0 | CaskStack, LLC | Email Marketing, Lead Capture Forms, Drip Campaigns, and Analytics for Focal CRM |
| 2026-10-01 22:09:07 | [focalcrm/sales](https://www.nuget.org/packages/focalcrm%2Fsales) | v0.1.0 | CaskStack, LLC | Sales, Deals, and Pipeline Management for Focal CRM |
| 2026-10-01 22:09:07 | [focalcrm/service](https://www.nuget.org/packages/focalcrm%2Fservice) | v0.1.0 | CaskStack, LLC | Customer Service, Help Desk, Tickets, SLAs, and Knowledge Base for Focal CRM |
| 2026-10-01 22:10:11 | [mage2kishan/module-malware-scanner](https://www.nuget.org/packages/mage2kishan%2Fmodule-malware-scanner) | 1.3.3 | Kishan Savaliya | Active malware prevention + on-disk scanner for Magento 2. Three real-time guar… |
| 2026-10-01 22:13:33 | [mage2kishan/module-mage-pos](https://www.nuget.org/packages/mage2kishan%2Fmodule-mage-pos) | 1.0.9 | Kishan Savaliya | Panth MagePos - a full point of sale (POS) for Magento 2. Standalone touch-frie… |
| 2026-10-01 22:18:23 | [mage2kishan/module-advanced-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-seo) | 1.8.5 | Kishan Savaliya | Panth Advanced SEO — enterprise-grade SEO suite for Magento 2: SEO dashboard, m… |
| 2026-10-01 22:21:27 | [mage2kishan/module-xml-sitemap](https://www.nuget.org/packages/mage2kishan%2Fmodule-xml-sitemap) | 1.2.3 | Kishan Savaliya | Panth XML Sitemap — sharded XML sitemap generator for Magento 2: per-store prof… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
