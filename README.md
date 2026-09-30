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

## Latest list — 2026-09-30 04:19 UTC

New packages created between 2026-09-30 03:19 UTC and 2026-09-30 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T04-19-59-410965Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 03:30:25 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.1 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |
| 2026-09-30 04:02:03 | [mage2kishan/module-performance-debugger](https://www.nuget.org/packages/mage2kishan%2Fmodule-performance-debugger) | 1.0.11 | Kishan Savaliya | Production-grade Magento 2 frontend performance debugger and profiler. Tracks b… |
| 2026-09-30 04:07:07 | [tualo/timetracker](https://www.nuget.org/packages/tualo%2Ftimetracker) | 1.0.2 |  | Timetracker package for Tualo Office package structure and example implementati… |
| 2026-09-30 04:16:29 | [mage2kishan/module-order-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-order-attachments) | 1.0.12 |  | Allows customers to attach files to order items |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
