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

## Latest list — 2026-09-30 02:18 UTC

New packages created between 2026-09-30 01:19 UTC and 2026-09-30 02:18 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T02-18-45-240922Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 01:40:59 | [mage2kishan/module-llms-txt](https://www.nuget.org/packages/mage2kishan%2Fmodule-llms-txt) | 1.5.2 | Kishan Savaliya | Panth LLMs.txt — AI Indexing Engine for Magento 2. Serves structured /llms.txt,… |
| 2026-09-30 01:56:48 | [survos/bookmark-bundle](https://www.nuget.org/packages/survos%2Fbookmark-bundle) | 2.34.16 |  | Local bookmarks for arbitrary resources with optional peer sharing. |
| 2026-09-30 02:00:34 | [mage2kishan/module-low-stock-notification](https://www.nuget.org/packages/mage2kishan%2Fmodule-low-stock-notification) | 1.0.11 |  | Magento 2 Low Stock Notification module - allows customers to subscribe for bac… |
| 2026-09-30 02:09:05 | [controleonline/legacy](https://www.nuget.org/packages/controleonline%2Flegacy) | v1.0.2 | Controle Online |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
