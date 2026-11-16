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

## Latest list — 2026-11-16 19:19 UTC

New packages created between 2026-11-16 18:20 UTC and 2026-11-16 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T19-19-17-626896Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 18:21:31 | [jeffersongoncalves/laravel-lgpd-consent](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-lgpd-consent) | 1.0.0 | Jefferson Gonçalves | LGPD consent ledger for Laravel: append-only consent records per purpose and te… |
| 2026-11-16 18:25:57 | [xddesigners/silverstripe-event-tickets](https://www.nuget.org/packages/xddesigners%2Fsilverstripe-event-tickets) | 6.0.0 | Remy Vaartjes | Event tickets for SilverStripe Event Calendar |
| 2026-11-16 18:31:36 | [geeklab/glroute](https://www.nuget.org/packages/geeklab%2Fglroute) | v1.0.1 |  | Yet another PHP Router |
| 2026-11-16 18:33:17 | [starbug/menus-admin](https://www.nuget.org/packages/starbug%2Fmenus-admin) | v0.9.0 | Ali Gangji | Admin screens for menu management. |
| 2026-11-16 18:41:30 | [xddesigners/dashboard](https://www.nuget.org/packages/xddesigners%2Fdashboard) | 6.0.0 | Remy Vaartjes | Adds dashboard interface to the Silverstripe CMS |
| 2026-11-16 18:51:47 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.28.1 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-16 18:52:42 | [starbug/users-admin](https://www.nuget.org/packages/starbug%2Fusers-admin) | v0.9.1 | Ali Gangji | Admin screens for user management. |
| 2026-11-16 18:59:04 | [mertaydin/laravel-queue-monitor](https://www.nuget.org/packages/mertaydin%2Flaravel-queue-monitor) | v0.1.0 |  | Monitor and manage Laravel queue connections with a driver-aware dashboard. |
| 2026-11-16 19:09:28 | [starbug/content-admin](https://www.nuget.org/packages/starbug%2Fcontent-admin) | v0.9.2 | Ali Gangji | Admin screens for pages, categories and tags. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
