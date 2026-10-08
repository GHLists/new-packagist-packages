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

## Latest list — 2026-10-08 20:22 UTC

New packages created between 2026-10-08 19:19 UTC and 2026-10-08 20:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T20-22-52-636773Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 19:24:30 | [jsonficator/jsonficator](https://www.nuget.org/packages/jsonficator%2Fjsonficator) | v1.0.0 | geckon01 | Framework-agnostic PHP library that converts natural language into structured d… |
| 2026-10-08 19:53:18 | [4oh3/drupal-dev-live-files](https://www.nuget.org/packages/4oh3%2Fdrupal-dev-live-files) | 1.0.1 |  | Serves images (and optionally other public files) from the live site instead of… |
| 2026-10-08 19:57:31 | [sereny/postgrest](https://www.nuget.org/packages/sereny%2Fpostgrest) | v0.1.0 | Sereny | A PostgREST connection driver that lets Laravel Eloquent models talk to a Postg… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
