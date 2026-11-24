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

## Latest list — 2026-11-24 17:20 UTC

New packages created between 2026-11-24 16:21 UTC and 2026-11-24 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T17-20-53-763122Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 16:36:06 | [emmanpbarrameda/filament-scaffold2](https://www.nuget.org/packages/emmanpbarrameda%2Ffilament-scaffold2) | v1.0.0 | Emmanuel P. Barrameda; Soluti… | Scaffold Manager for Filament v4/v5: generate migrations, models, resources, po… |
| 2026-11-24 16:40:57 | [leadveyor/leadveyor-php](https://www.nuget.org/packages/leadveyor%2Fleadveyor-php) | v0.1.0 | Leadveyor | Official PHP client for the Leadveyor API: lead scoring, sources, webhooks. |
| 2026-11-24 16:42:02 | [jostar/savedate-wordpress](https://www.nuget.org/packages/jostar%2Fsavedate-wordpress) | v0.2.0 |  | WordPress-Plugin für SaveDate-Events: Termine verwalten, Listen, Kalender und F… |
| 2026-11-24 16:44:17 | [jostar/savedate-client](https://www.nuget.org/packages/jostar%2Fsavedate-client) | v0.1.2 |  | PHP-Client für die SaveDate-Event-API mit Validierung, Admin-Oberfläche und Ans… |
| 2026-11-24 16:47:24 | [eshimischi/vendor-cleanup](https://www.nuget.org/packages/eshimischi%2Fvendor-cleanup) | v2.0.3 | eshimischi | Global CLI tool & Composer plugin to strip tests, docs, and dev files from vend… |
| 2026-11-24 16:50:36 | [shoplygg/shoply-php](https://www.nuget.org/packages/shoplygg%2Fshoply-php) | v0.11.5 |  | Shoply's API from your own server: every route as a method, safe retries, pages… |
| 2026-11-24 17:09:24 | [ray/fake-query](https://www.nuget.org/packages/ray%2Ffake-query) | 0.1.0 | Akihito Koriyama | Fakes Ray.MediaQuery query interfaces by returning JSON fixture data instead of… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
