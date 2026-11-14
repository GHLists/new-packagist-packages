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

## Latest list — 2026-11-14 20:19 UTC

New packages created between 2026-11-14 19:21 UTC and 2026-11-14 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T20-19-30-92475Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 19:26:51 | [seva-code/php-click-house-client](https://www.nuget.org/packages/seva-code%2Fphp-click-house-client) | 2.0.0 | SevaCode | PHP Client for ClickHouse HTTP interface |
| 2026-11-14 19:37:43 | [liberusoftware/module-maintenance-documents-api](https://www.nuget.org/packages/liberusoftware%2Fmodule-maintenance-documents-api) | 0.1.0 |  | Maintenance documents API presentation adapter. |
| 2026-11-14 19:37:51 | [liberusoftware/module-maintenance-documents](https://www.nuget.org/packages/liberusoftware%2Fmodule-maintenance-documents) | 0.1.0 |  | Tenant-scoped maintenance document management. |
| 2026-11-14 19:38:21 | [liberusoftware/module-maintenance-notes](https://www.nuget.org/packages/liberusoftware%2Fmodule-maintenance-notes) | 0.1.0 |  | Tenant-scoped notes for maintenance customer and commercial workflows. |
| 2026-11-14 19:38:28 | [liberusoftware/module-maintenance-notes-api](https://www.nuget.org/packages/liberusoftware%2Fmodule-maintenance-notes-api) | 0.1.0 |  | Maintenance notes API presentation adapter. |
| 2026-11-14 19:39:07 | [liberusoftware/module-maintenance-tasks](https://www.nuget.org/packages/liberusoftware%2Fmodule-maintenance-tasks) | 0.1.0 |  | Tenant-scoped maintenance tasks and assignments. |
| 2026-11-14 19:39:10 | [liberusoftware/module-maintenance-tasks-api](https://www.nuget.org/packages/liberusoftware%2Fmodule-maintenance-tasks-api) | 0.1.0 |  | Maintenance tasks API presentation adapter. |
| 2026-11-14 19:57:29 | [callismart/smliser-update-client](https://www.nuget.org/packages/callismart%2Fsmliser-update-client) | v1.0.0 | Callistus Nwachukwu | Update client for apps hosted on a Smart License Server: checks the release rou… |
| 2026-11-14 20:02:30 | [jumphp/notification](https://www.nuget.org/packages/jumphp%2Fnotification) | v0.5.62 |  | Push notifications for JumPHP applications: the people who use your browser gam… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
