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

## Latest list — 2026-11-03 02:21 UTC

New packages created between 2026-11-03 01:20 UTC and 2026-11-03 02:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T02-21-37-43403Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 01:50:25 | [roayapay/platform-core](https://www.nuget.org/packages/roayapay%2Fplatform-core) | v1.0.0 | RoayaPay Engineering | RoayaPay Platform Core: the official RoayaPay engineering standard for Laravel… |
| 2026-11-03 01:51:43 | [hibira-io/craft-hibira](https://www.nuget.org/packages/hibira-io%2Fcraft-hibira) | v0.1.0 | Hibira | Realtime for Craft CMS on Hibira: editing presence and saved warnings in the co… |
| 2026-11-03 01:57:53 | [lowelllab/dpop-core](https://www.nuget.org/packages/lowelllab%2Fdpop-core) | v0.1.0-beta.1 |  | Framework-independent strict RFC 9449 DPoP verification and authentication coor… |
| 2026-11-03 01:58:29 | [lowelllab/hyperf-dpop](https://www.nuget.org/packages/lowelllab%2Fhyperf-dpop) | v0.1.0-beta.1 |  | Hyperf integration for strict DPoP authentication, nonce and atomic replay prot… |
| 2026-11-03 01:58:43 | [ashraftalha/laravel-opconsole](https://www.nuget.org/packages/ashraftalha%2Flaravel-opconsole) | v1.2.2 | Ashraf Talha | Monitor. Diagnose. Maintain. An administrative operations console for Laravel a… |
| 2026-11-03 02:05:36 | [noone-silent/data-transfer-object](https://www.nuget.org/packages/noone-silent%2Fdata-transfer-object) | v1.0.0 | Brent Roose | Data transfer objects with batteries included |
| 2026-11-03 02:07:24 | [abduns/laravel-db-backup](https://www.nuget.org/packages/abduns%2Flaravel-db-backup) | v1.0.0 | Abduns | Back up a Laravel database (PostgreSQL, MySQL/MariaDB or SQLite) to any filesys… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
