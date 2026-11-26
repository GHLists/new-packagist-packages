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

## Latest list — 2026-11-26 08:21 UTC

New packages created between 2026-11-26 07:22 UTC and 2026-11-26 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T08-21-23-743357Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 07:22:26 | [klsoft/yii3-cms](https://www.nuget.org/packages/klsoft%2Fyii3-cms) | 1.0.0 |  | A content management system based on the Yii 3 framework and uses the Doctrine… |
| 2026-11-26 07:31:02 | [proudnerds/pn-search-suggestions](https://www.nuget.org/packages/proudnerds%2Fpn-search-suggestions) | 14.3.1 | Netcreators; Proud Nerds | Show customized results on search form |
| 2026-11-26 07:41:36 | [newgeode/webguard](https://www.nuget.org/packages/newgeode%2Fwebguard) | v1.0.0 | New Geode | Lightweight Laravel security middleware for IP restrictions, trusted proxies, H… |
| 2026-11-26 08:01:46 | [arkhan0072-dev/laravel-ledger](https://www.nuget.org/packages/arkhan0072-dev%2Flaravel-ledger) | v0.1.0 | Abdulrehman Khan | Double-entry accounting ledger for Laravel: balanced journal entries, integer m… |
| 2026-11-26 08:12:17 | [tracewick/laravel](https://www.nuget.org/packages/tracewick%2Flaravel) | v1.0.0-rc.1 |  | Tracewick sampling profiler integration for Laravel |
| 2026-11-26 08:13:03 | [nesravomigarbi/examen-civique-france](https://www.nuget.org/packages/nesravomigarbi%2Fexamen-civique-france) | v1.0.0 | Nesra Vomigarbi | Official French civic exam (examen civique) 2026 question lists and nationality… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
