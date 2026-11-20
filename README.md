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

## Latest list — 2026-11-20 09:21 UTC

New packages created between 2026-11-20 08:20 UTC and 2026-11-20 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T09-21-51-472006Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 08:32:47 | [byteworks/sonata-theme-bundle](https://www.nuget.org/packages/byteworks%2Fsonata-theme-bundle) | 1.0.0 |  | AdminLTE 4 (Bootstrap 5, no jQuery) theme for SonataAdminBundle 4.x |
| 2026-11-20 08:40:45 | [nirogilanka/medical-calculators](https://www.nuget.org/packages/nirogilanka%2Fmedical-calculators) | v1.0.0 | Dr. Priya Sammani (MBBS, PG D… | Free multilingual WordPress plugin providing 76 doctor-reviewed interactive med… |
| 2026-11-20 08:45:35 | [nickdekruijk/laravel-beacon](https://www.nuget.org/packages/nickdekruijk%2Flaravel-beacon) | 1.1.0 | Nick de Kruijk | Reports the exceptions of a Laravel site to your own dashboard, without a key:… |
| 2026-11-20 09:03:20 | [nickaguilarh/laravel-readiness](https://www.nuget.org/packages/nickaguilarh%2Flaravel-readiness) | v0.1.0 | Nick Aguilar H | Readiness probe toolkit for Laravel: per-instance drain mode, bounded database/… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
