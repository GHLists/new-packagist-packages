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

## Latest list — 2026-11-05 13:21 UTC

New packages created between 2026-11-05 12:20 UTC and 2026-11-05 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T13-21-55-351583Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 12:21:27 | [intragile/laravel-nav-online-szamla](https://www.nuget.org/packages/intragile%2Flaravel-nav-online-szamla) | v1.0.1 | IntrAgile Kft. | Complete, Laravel-native client for the Hungarian NAV Online Számla (Online Inv… |
| 2026-11-05 12:21:58 | [osmanov/pecl-eio](https://www.nuget.org/packages/osmanov%2Fpecl-eio) | 4.0.0 |  | Provides interface to libeio library. |
| 2026-11-05 12:31:10 | [sevaske/taqnyat-api](https://www.nuget.org/packages/sevaske%2Ftaqnyat-api) | 1.0.0 | sevaske | Framework-agnostic PHP client for the Taqnyat SMS API (taqnyat.sa): send plain… |
| 2026-11-05 13:01:40 | [mlocati/install-php-extensions](https://www.nuget.org/packages/mlocati%2Finstall-php-extensions) | 0.0.1 | Michele Locati | Easily install PHP extensions |
| 2026-11-05 13:08:33 | [kopexa/mautic-preferences-center](https://www.nuget.org/packages/kopexa%2Fmautic-preferences-center) | v0.1.0 | Kopexa | Preference center for Mautic: choose which categories appear as topics, in whic… |
| 2026-11-05 13:12:55 | [crabphp/runs](https://www.nuget.org/packages/crabphp%2Fruns) | v0.1.0 |  | Durable runs for the Crab framework: work of many steps that goes on from where… |
| 2026-11-05 13:13:05 | [crabphp/actors](https://www.nuget.org/packages/crabphp%2Factors) | v0.1.0 |  | Actors for the Crab framework: one for each key, taking its messages one at a t… |
| 2026-11-05 13:13:16 | [crabphp/redis](https://www.nuget.org/packages/crabphp%2Fredis) | v0.1.0 |  | Redis for the Crab framework: a cache store and a queue store that wait without… |
| 2026-11-05 13:13:27 | [crabphp/s3](https://www.nuget.org/packages/crabphp%2Fs3) | v0.1.0 |  | S3 for the Crab framework: a disk on Amazon S3, Cloudflare R2, MinIO or any ser… |
| 2026-11-05 13:13:37 | [crabphp/openapi](https://www.nuget.org/packages/crabphp%2Fopenapi) | v0.1.0 |  | OpenAPI documents generated from Crab routes and action signatures |
| 2026-11-05 13:13:48 | [crabphp/clockwerk](https://www.nuget.org/packages/crabphp%2Fclockwerk) | v0.1.0 |  | A dashboard for an application on the Crab framework: requests, the queue, sche… |
| 2026-11-05 13:14:39 | [slimfony/core](https://www.nuget.org/packages/slimfony%2Fcore) | v0.1.0 |  | Ultra-lightweight, secure Symfony-component based microservice core for Franken… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
