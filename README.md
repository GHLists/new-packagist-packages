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

## Latest list — 2026-11-10 03:20 UTC

New packages created between 2026-11-10 02:21 UTC and 2026-11-10 03:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T03-20-52-370192Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 02:35:32 | [elcreator/adataforseo](https://www.nuget.org/packages/elcreator%2Fadataforseo) | 0.1.0 |  | aDataForSeo — gets your Evolution CMS site found in search: DataForSEO index co… |
| 2026-11-10 02:50:24 | [atannex/laravel-flutter-bridge](https://www.nuget.org/packages/atannex%2Flaravel-flutter-bridge) | v2.0.0 | Atannex Enterprise | Enterprise-grade Laravel bridge for Flutter applications: Sanctum auth with rot… |
| 2026-11-10 02:58:39 | [kenprz/laravel-custom-fields](https://www.nuget.org/packages/kenprz%2Flaravel-custom-fields) | v1.0.0 | Ken Perez | User-defined custom fields for Eloquent models, without touching your schema. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
