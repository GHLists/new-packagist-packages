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

## Latest list — 2026-10-13 18:21 UTC

New packages created between 2026-10-13 17:21 UTC and 2026-10-13 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T18-21-25-431803Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 17:56:01 | [kodegrenade/mygra](https://www.nuget.org/packages/kodegrenade%2Fmygra) | v0.1.0 | Temitope Ayotunde | Config-driven data migration between MySQL, PostgreSQL, SQLite and SQL Server:… |
| 2026-10-13 18:14:51 | [dotswan/eagle-eye](https://www.nuget.org/packages/dotswan%2Feagle-eye) | v1.0.0-beta.1 | Dotswan | Driver-agnostic activity and audit logging for Laravel with automatic capture,… |
| 2026-10-13 18:14:55 | [dotswan/eagle-eye-filament](https://www.nuget.org/packages/dotswan%2Feagle-eye-filament) | v1.0.0-beta.1 | Dotswan | Filament 5 admin UI for dotswan/eagle-eye: activity explorer, trace timeline, o… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
