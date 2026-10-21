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

## Latest list — 2026-10-21 04:19 UTC

New packages created between 2026-10-21 03:19 UTC and 2026-10-21 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T04-19-15-803896Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 03:34:59 | [studeo/check](https://www.nuget.org/packages/studeo%2Fcheck) | v0.1.0 |  | Static-analysis engine for Laravel projects. |
| 2026-10-21 03:40:05 | [sammy-boy/laravel-reporting](https://www.nuget.org/packages/sammy-boy%2Flaravel-reporting) | v1.0.0 | Sammy Orondo | Reporting publication layer for Laravel microservices. Owns HOW reporting messa… |
| 2026-10-21 03:53:34 | [kallookoo/wp-stubs](https://www.nuget.org/packages/kallookoo%2Fwp-stubs) | 1.0.0 |  | WordPress and WooCommerce stubs for PHP |
| 2026-10-21 03:55:31 | [studeo/modular](https://www.nuget.org/packages/studeo%2Fmodular) | v0.1.0 |  | Modular architecture and code generators for Laravel. |
| 2026-10-21 04:11:19 | [putuwahyu29/backup-bridge](https://www.nuget.org/packages/putuwahyu29%2Fbackup-bridge) | v1.0.0 | Putu Wahyu | A secure bridge, visual control dashboard, and multi-database backup agent for… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
