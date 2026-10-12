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

## Latest list — 2026-10-12 21:19 UTC

New packages created between 2026-10-12 20:21 UTC and 2026-10-12 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T21-19-52-475015Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 20:24:48 | [publicala/laravel-resilient-redis](https://www.nuget.org/packages/publicala%2Flaravel-resilient-redis) | v1.0.0 | publica.la | Retry transient phpredis connect failures in Laravel, and give Laravel 11 and 1… |
| 2026-10-12 20:32:04 | [laranex/laravel-schema-viewer](https://www.nuget.org/packages/laranex%2Flaravel-schema-viewer) | v1.0.0 | Nay Thu Khant | Schema viewer for Laravel: an interactive diagram of your database tables and E… |
| 2026-10-12 20:32:22 | [xproapi/xproapi-php](https://www.nuget.org/packages/xproapi%2Fxproapi-php) | v1.0.0.0 |  | PHP client for the Xproapi X (Twitter) data API: profiles, followers, following… |
| 2026-10-12 20:46:21 | [wilycode/dotenv](https://www.nuget.org/packages/wilycode%2Fdotenv) | v0.1.0 | Simon Piter | Strict, lightweight .env file reader and loader for PHP. |
| 2026-10-12 20:48:02 | [specia1z/points](https://www.nuget.org/packages/specia1z%2Fpoints) | 2.0.0 | Specia1z | A configurable points and rewards system for Flarum. |
| 2026-10-12 20:50:14 | [alien1225/basisu](https://www.nuget.org/packages/alien1225%2Fbasisu) | v0.1.0 |  |  |
| 2026-10-12 20:57:00 | [wilycode/session](https://www.nuget.org/packages/wilycode%2Fsession) | v0.1.0 | Simon Piter | Storage-agnostic session contract with namespace-scoped key/value access for PH… |
| 2026-10-12 21:12:35 | [wilycode/session-php](https://www.nuget.org/packages/wilycode%2Fsession-php) | v0.1.0 | Simon Piter | Native PHP session adapter with namespaced storage for wilycode/session. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
