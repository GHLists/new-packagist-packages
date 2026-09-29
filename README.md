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

## Latest list — 2026-09-29 20:20 UTC

New packages created between 2026-09-29 19:21 UTC and 2026-09-29 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T20-20-18-953569Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 19:35:11 | [mage2kishan/module-advancedcart](https://www.nuget.org/packages/mage2kishan%2Fmodule-advancedcart) | 1.0.9 |  | Advanced Cart Page Enhancements - Free shipping bar, qty buttons, trust badges,… |
| 2026-09-29 19:37:50 | [youmad/endurance-activity-fit](https://www.nuget.org/packages/youmad%2Fendurance-activity-fit) | v0.1.1 |  | Streaming FIT-to-activity mapping and import coordination |
| 2026-09-29 19:48:20 | [jgawlik/laravel-journal](https://www.nuget.org/packages/jgawlik%2Flaravel-journal) | v1.0.0 | Jakub Gawlik | A Laravel package providing a multi-user journal API with CRUD operations. |
| 2026-09-29 19:50:11 | [mage2kishan/module-banner-slider](https://www.nuget.org/packages/mage2kishan%2Fmodule-banner-slider) | 1.0.11 | Kishan Savaliya | Panth Banner Slider Module - Responsive banner slider widget with Luma and Hyva… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
