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

## Latest list — 2026-11-11 07:20 UTC

New packages created between 2026-11-11 06:19 UTC and 2026-11-11 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T07-20-49-412552Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 06:38:09 | [omnisense/contracts](https://www.nuget.org/packages/omnisense%2Fcontracts) | v1.0.0-rc.1 | Marco Meyer | The contracts every omnisense provider family builds on, under any PHP host: a… |
| 2026-11-11 06:59:07 | [zenepay/laravel-infobip](https://www.nuget.org/packages/zenepay%2Flaravel-infobip) | 1.0.0 | Zenepay | Laravel client for the Infobip People API: profiles, batch updates, and people… |
| 2026-11-11 07:03:49 | [jbmm/db-table-manager](https://www.nuget.org/packages/jbmm%2Fdb-table-manager) | v1.0.0 | Jbmm | Local-only Laravel UI for browsing and managing database tables |
| 2026-11-11 07:03:49 | [jbmm/table-record-manager](https://www.nuget.org/packages/jbmm%2Ftable-record-manager) | v1.0.0 | Jbmm | Local-only Laravel UI for browsing and managing database tables |
| 2026-11-11 07:04:51 | [youvision/think-auth](https://www.nuget.org/packages/youvision%2Fthink-auth) | v1.0.0 |  | Role based access control (RBAC) authentication package for ThinkPHP 8. |
| 2026-11-11 07:10:46 | [rkov/view-model](https://www.nuget.org/packages/rkov%2Fview-model) | v1.0.0 | Rochev Yakov | View models for REST API — create model representations using dependency inject… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
