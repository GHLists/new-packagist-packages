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

## Latest list — 2026-10-18 23:20 UTC

New packages created between 2026-10-18 22:21 UTC and 2026-10-18 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T23-20-42-86119Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 22:23:54 | [claviron/laravel](https://www.nuget.org/packages/claviron%2Flaravel) | v0.1.0 |  | Claviron drivers and adapters for Laravel: cache, sessions, database, broadcast… |
| 2026-10-18 22:23:54 | [claviron/sapi](https://www.nuget.org/packages/claviron%2Fsapi) | v0.1.0 |  | PHP declarations, fail-fast native API fallbacks and a Monolog handler for Clav… |
| 2026-10-18 22:30:20 | [anun333/oe-module-migration](https://www.nuget.org/packages/anun333%2Foe-module-migration) | v0.1.0 | anun333 | Migration into OpenEMR from other EHRs: reads the FHIR R4 export every certifie… |
| 2026-10-18 22:33:46 | [itdarkarts/html-table](https://www.nuget.org/packages/itdarkarts%2Fhtml-table) | 1.0.0 | Peter Bailie | Simple API to create tables as HTML. |
| 2026-10-18 22:42:40 | [ronu/rest-permissions](https://www.nuget.org/packages/ronu%2Frest-permissions) | v1.0.0 | charlietyn | Route-based permissions for ronu/rest-generic-class: route permission catalog,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
