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

## Latest list — 2026-10-07 00:19 UTC

New packages created between 2026-10-06 23:20 UTC and 2026-10-07 00:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T00-19-30-98332Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 23:28:18 | [laravel-tipi/support](https://www.nuget.org/packages/laravel-tipi%2Fsupport) | v1.0.0 | Irakli | Shared support utilities for Laravel Tipi packages |
| 2026-10-06 23:28:20 | [laravel-tipi/filament-support](https://www.nuget.org/packages/laravel-tipi%2Ffilament-support) | v1.0.2 | Irakli | Shared Filament support utilities for Laravel Tipi packages |
| 2026-10-06 23:34:06 | [monsieurbiz/healthcheck-bundle](https://www.nuget.org/packages/monsieurbiz%2Fhealthcheck-bundle) | v1.0.0 |  | Symfony bundle providing a /healthcheck endpoint running tagged DoCheckInterfac… |
| 2026-10-07 00:12:19 | [laravel-tipi/filament-translations](https://www.nuget.org/packages/laravel-tipi%2Ffilament-translations) | v0.1.0 | Irakli | Filament integration for laravel-tipi/translations |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
