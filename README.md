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

## Latest list — 2026-10-07 23:20 UTC

New packages created between 2026-10-07 22:21 UTC and 2026-10-07 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T23-20-06-16127Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 22:46:16 | [soft-tech-mx/laravel-made](https://www.nuget.org/packages/soft-tech-mx%2Flaravel-made) | v1.0.2 | Bayron Vazquez | Conjunto base de dependencias y configuración inicial que SoftTechMX usa en tod… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
