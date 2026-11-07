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

## Latest list — 2026-11-07 04:20 UTC

New packages created between 2026-11-07 03:21 UTC and 2026-11-07 04:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T04-20-36-897703Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 03:29:23 | [itmosoft/laravel-subscriptions](https://www.nuget.org/packages/itmosoft%2Flaravel-subscriptions) | v1.0.1 |  | Plan and subscription lifecycle management for Laravel applications. |
| 2026-11-07 03:35:27 | [fflch/fixfflch](https://www.nuget.org/packages/fflch%2Ffixfflch) | 1.0.0 | Thiago Gomes Verissimo | Ajustes e correções customizadas para os sites da FFLCH USP. |
| 2026-11-07 04:04:25 | [withvisionstack/performatic-framework](https://www.nuget.org/packages/withvisionstack%2Fperformatic-framework) | v1.1.0 |  | Framework PHP procedural com motor Rust — API sem Laravel, validação declarativ… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
