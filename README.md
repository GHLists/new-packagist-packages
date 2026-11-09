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

## Latest list — 2026-11-09 04:21 UTC

New packages created between 2026-11-09 03:20 UTC and 2026-11-09 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T04-21-24-56804Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 03:35:41 | [riders-agency/pulse-sdk](https://www.nuget.org/packages/riders-agency%2Fpulse-sdk) | 0.1.0 | Riders Agency | Reviewed JSON subset of Pulse API v1: authentication, tasks and AI proposals. C… |
| 2026-11-09 03:41:47 | [mahmudabbas0/laravel-demo-mode](https://www.nuget.org/packages/mahmudabbas0%2Flaravel-demo-mode) | v1.0.0 |  | Read-only portfolio demos and one-click demo accounts for Laravel 10 through 13. |
| 2026-11-09 03:58:34 | [starbug/importer-spreadsheet](https://www.nuget.org/packages/starbug%2Fimporter-spreadsheet) | v0.9.0 | Ali Gangji | Spreadsheet read strategies for the Starbug import pipeline. |
| 2026-11-09 04:19:38 | [ulsyairil/sqlite-auto-cloud-sync](https://www.nuget.org/packages/ulsyairil%2Fsqlite-auto-cloud-sync) | v1.0.0 |  | Row-level SQLite cloud sync core with Laravel, CodeIgniter and Symfony adapters. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
