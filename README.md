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

## Latest list — 2026-11-12 20:21 UTC

New packages created between 2026-11-12 19:21 UTC and 2026-11-12 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T20-21-07-509144Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 19:30:28 | [core23/composer-size-limit](https://www.nuget.org/packages/core23%2Fcomposer-size-limit) | 1.0.0 |  | Composer plugin to enforce size limits for files, vendor and build artifacts, l… |
| 2026-11-12 19:40:37 | [telescope-monitor/telescope-monitor](https://www.nuget.org/packages/telescope-monitor%2Ftelescope-monitor) | v1.0.0-rc.1 |  | Complete error investigation and operations for Laravel Telescope. |
| 2026-11-12 19:40:51 | [szabrob/laravel-szamlazz](https://www.nuget.org/packages/szabrob%2Flaravel-szamlazz) | v1.0.0 | Szabó Róbert | Laravel integration for the Számlázz.hu Számla Agent API. |
| 2026-11-12 19:42:26 | [immachakata/ci4-facades](https://www.nuget.org/packages/immachakata%2Fci4-facades) | v1.0.0 | Isaac Machakata | Use laravel like facades and functions for creating migration files, among othe… |
| 2026-11-12 19:47:39 | [coolpie/util](https://www.nuget.org/packages/coolpie%2Futil) | v0.1.0 | Coolpie | PHP utility classes made by yours truly |
| 2026-11-12 20:00:24 | [alianet/holiday](https://www.nuget.org/packages/alianet%2Fholiday) | 0.12.0 | Stefan Kruppa; Mariusz Kaczan… | A PHP library to compute holidays. It's something :-) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
