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

## Latest list — 2026-10-19 00:19 UTC

New packages created between 2026-10-18 23:20 UTC and 2026-10-19 00:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T00-19-39-462277Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 23:28:20 | [usamamuneerchaudhary/billboard](https://www.nuget.org/packages/usamamuneerchaudhary%2Fbillboard) | 1.0 | Usama Muneer | Ad management for Statamic: placements, weighted rotation, scheduling, targetin… |
| 2026-10-18 23:41:44 | [silassena/full-pay](https://www.nuget.org/packages/silassena%2Ffull-pay) | v1.0.1 | Silas Sena | integration with payment portals |
| 2026-10-18 23:57:59 | [wilycode/migration](https://www.nuget.org/packages/wilycode%2Fmigration) | v0.1.0 | Simon Piter | Small, driver-independent PHP database migration runner with CLI, version track… |
| 2026-10-19 00:01:09 | [zerodev/kora](https://www.nuget.org/packages/zerodev%2Fkora) | v3.1.1 |  | Official PHP SDK for Kora licensing |
| 2026-10-19 00:02:57 | [djouamaah/laravel-algeria](https://www.nuget.org/packages/djouamaah%2Flaravel-algeria) | v1.1.0 | Djouamaa | All Algerian wilayas, dairas, communes and postal codes (69 wilayas / 1541 comm… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
