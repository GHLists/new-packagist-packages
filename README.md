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

## Latest list — 2026-10-14 18:20 UTC

New packages created between 2026-10-14 17:21 UTC and 2026-10-14 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T18-20-09-989409Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 17:35:15 | [cecil/theme-leon](https://www.nuget.org/packages/cecil%2Ftheme-leon) | 1.0.0 |  | Cecil Léon theme: a documentation theme with a warm and editorial look |
| 2026-10-14 17:47:18 | [mikhailmelnikov/filament-jobs-monitor](https://www.nuget.org/packages/mikhailmelnikov%2Ffilament-jobs-monitor) | v1.0.0 | Mikhail Melnikov | Filament add-on: scheduler tasks and database queue jobs in the admin panel — l… |
| 2026-10-14 17:51:12 | [x-laravel/sluggable](https://www.nuget.org/packages/x-laravel%2Fsluggable) | v1.0.0 | Mehmet ÖĞMEN | Slugs for Eloquent models with Turkish-aware generation, race-safe uniqueness a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
