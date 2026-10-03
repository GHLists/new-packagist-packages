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

## Latest list — 2026-10-03 08:21 UTC

New packages created between 2026-10-03 07:21 UTC and 2026-10-03 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T08-21-54-043032Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 07:21:54 | [php-bug-catcher/perf-collector-bundle](https://www.nuget.org/packages/php-bug-catcher%2Fperf-collector-bundle) | v2.0.0-RC2 |  | Symfony integration for the Bug Catcher performance collector: the aggregator a… |
| 2026-10-03 07:29:58 | [tilscn/laravel](https://www.nuget.org/packages/tilscn%2Flaravel) | 1.0.0 | tilscn | A Laravel package for various utilities. |
| 2026-10-03 07:31:31 | [corvus-dotnet/corvus-json-schema](https://www.nuget.org/packages/corvus-dotnet%2Fcorvus-json-schema) | 0.1.0 | endjin | A high-performance JSON Schema evaluator (draft 4, 6, 7, 2019-09 and 2020-12) a… |
| 2026-10-03 07:59:17 | [mage2kishan/module-mega-menu](https://www.nuget.org/packages/mage2kishan%2Fmodule-mega-menu) | 1.0.18 | Kishan Savaliya | Advanced mega menu for Magento 2 — works on Hyva and Luma. Drag-and-drop tree b… |
| 2026-10-03 07:59:57 | [missbach/shape-cms](https://www.nuget.org/packages/missbach%2Fshape-cms) | 2.0.0 | Michael Missbach | Shape CMS based on Shape Application Framework |
| 2026-10-03 08:02:42 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.8 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |
| 2026-10-03 08:04:12 | [adt/log-mover](https://www.nuget.org/packages/adt%2Flog-mover) | v1.0 | Apps Dev Team | Moves log tables from the application database into a separate log storage (typ… |
| 2026-10-03 08:06:24 | [missbach/shape](https://www.nuget.org/packages/missbach%2Fshape) | 2.0.0 | Michael Missbach | Symfony application framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
