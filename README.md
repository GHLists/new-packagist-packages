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

## Latest list — 2026-11-17 06:19 UTC

New packages created between 2026-11-17 05:20 UTC and 2026-11-17 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T06-19-51-038737Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 05:25:06 | [dakotajune/seeders](https://www.nuget.org/packages/dakotajune%2Fseeders) | v1.0.0 |  | Factories and seeders for Laravel Blueprint that are worth keeping: values from… |
| 2026-11-17 05:31:17 | [muhdaimans/laravel-openapi-studio](https://www.nuget.org/packages/muhdaimans%2Flaravel-openapi-studio) | v0.1.0 |  | A local-only visual editor for creating, editing and deleting OpenAPI 3 (.yaml/… |
| 2026-11-17 05:33:40 | [starbug/notifications](https://www.nuget.org/packages/starbug%2Fnotifications) | v0.9.0 | Ali Gangji | Notifications, delivered through channels and handlers. |
| 2026-11-17 05:33:40 | [starbug/notifications-admin](https://www.nuget.org/packages/starbug%2Fnotifications-admin) | v0.9.2 | Ali Gangji | Admin screens for notifications. |
| 2026-11-17 05:37:06 | [fiachehr/laravel-logger](https://www.nuget.org/packages/fiachehr%2Flaravel-logger) | v0.1.0 |  | Privacy-first structured JSON logging and an authorized, bounded log explorer f… |
| 2026-11-17 05:37:07 | [itmosoft/laravel-marketplace](https://www.nuget.org/packages/itmosoft%2Flaravel-marketplace) | v1.0.1 |  | Marketplace order orchestration and vendor order attribution for Laravel applic… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
