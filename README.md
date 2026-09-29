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

## Latest list — 2026-09-29 08:25 UTC

New packages created between 2026-09-29 07:21 UTC and 2026-09-29 08:25 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T08-25-44-82245Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 07:25:50 | [vuthaihoc/laravel-xtdb2](https://www.nuget.org/packages/vuthaihoc%2Flaravel-xtdb2) | v0.1.0-beta2 | vuthaihoc | An XTDB 2 database driver for Laravel: Eloquent, Query Builder and migrations o… |
| 2026-09-29 07:34:28 | [schachbulle/contao-schachcomputer-bundle](https://www.nuget.org/packages/schachbulle%2Fcontao-schachcomputer-bundle) | 1.0.0 | Frank Hoppe | Gewertete Schachpartien gegen Stockfish im Browser für Contao: Bedenkzeiten aus… |
| 2026-09-29 07:52:25 | [wexample/php-remote](https://www.nuget.org/packages/wexample%2Fphp-remote) | 1.0.2 | weeger | Registry, health checks and php-api client building for the external services a… |
| 2026-09-29 07:54:36 | [protung/easyadmin-plus-bundle](https://www.nuget.org/packages/protung%2Feasyadmin-plus-bundle) | v0.1.0 | Dragos Protung; Cezary Stepko… | Extensions for EasyAdmin: base CRUD controllers, also for editing entities thro… |
| 2026-09-29 07:59:56 | [youmad/endurance-foundation](https://www.nuget.org/packages/youmad%2Fendurance-foundation) | v0.1.1 |  | Foundational value objects and clock abstractions for activity processing |
| 2026-09-29 08:03:32 | [fyuri4/laravel-observability](https://www.nuget.org/packages/fyuri4%2Flaravel-observability) | v1.0.1 | FURUSHKA | Production-ready observability for Laravel: traces, spans, slow queries, except… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
