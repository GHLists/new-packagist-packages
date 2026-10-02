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

## Latest list — 2026-10-02 11:21 UTC

New packages created between 2026-10-02 10:21 UTC and 2026-10-02 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T11-21-59-115616Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 10:33:41 | [smartassert/symfony-remote-event-request-factory](https://www.nuget.org/packages/smartassert%2Fsymfony-remote-event-request-factory) | 0.1 | Jon Cram |  |
| 2026-10-02 10:46:24 | [yatmo/typo3-yatmo-map](https://www.nuget.org/packages/yatmo%2Ftypo3-yatmo-map) | 1.0.0 | Yatmo | Real estate map, points of interest with travel times and an indexable neighbou… |
| 2026-10-02 11:03:57 | [mage2kishan/module-redirects](https://www.nuget.org/packages/mage2kishan%2Fmodule-redirects) | 1.2.4 |  | Redirects and 404 management for Magento 2 (Hyva + Luma). Manual + auto redirec… |
| 2026-10-02 11:05:17 | [sympress/cli](https://www.nuget.org/packages/sympress%2Fcli) | v0.1.0 | Brian Schaffner | Standalone Symfony Console CLI for creating configured SymPress projects from s… |
| 2026-10-02 11:09:12 | [mage2kishan/module-advanced-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-seo) | 1.8.7 | Kishan Savaliya | Panth Advanced SEO — enterprise-grade SEO suite for Magento 2: SEO dashboard, m… |
| 2026-10-02 11:10:35 | [statamic-addon/upload-video](https://www.nuget.org/packages/statamic-addon%2Fupload-video) | v1.0.1 |  | Vizuall Upload Video fieldtype |
| 2026-10-02 11:13:05 | [mage2kishan/module-pagebuilder-ai](https://www.nuget.org/packages/mage2kishan%2Fmodule-pagebuilder-ai) | 1.2.26 | Kishan Savaliya | Adds an AI Content button to the Magento PageBuilder toolbar and inline AI butt… |
| 2026-10-02 11:14:36 | [sympress/mailer](https://www.nuget.org/packages/sympress%2Fmailer) | v0.1.0 | Brian Schäffner | Core Symfony Mailer powered WordPress mail plugin for the SymPress kernel. |
| 2026-10-02 11:16:45 | [mage2kishan/module-extra-fee](https://www.nuget.org/packages/mage2kishan%2Fmodule-extra-fee) | 1.1.5 | Kishan Savaliya | Panth Extra Fee — add configurable extra fees and surcharges to Magento 2 check… |
| 2026-10-02 11:20:22 | [mage2kishan/module-filter-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-filter-seo) | 1.1.4 | Kishan Savaliya | Panth Filter SEO — clean path-based URLs for layered navigation filters + dynam… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
