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

## Latest list — 2026-11-05 08:19 UTC

New packages created between 2026-11-05 07:21 UTC and 2026-11-05 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T08-19-58-184143Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 07:31:32 | [fayne/laravel-filament-post-release-status](https://www.nuget.org/packages/fayne%2Flaravel-filament-post-release-status) | v1.0.0 |  | Tenant publication status and immutable release history for Filament. |
| 2026-11-05 07:40:42 | [jyim/laravel-plugin](https://www.nuget.org/packages/jyim%2Flaravel-plugin) | 2.0.0 | augustdai | Laravel 10x 适配版插件系统 |
| 2026-11-05 07:40:48 | [tausi/tausi-php](https://www.nuget.org/packages/tausi%2Ftausi-php) | v0.1.0 |  | Official PHP SDK for Tausi: verify sessions and manage users from your PHP back… |
| 2026-11-05 07:50:09 | [byiftikhar/telescope-inspector](https://www.nuget.org/packages/byiftikhar%2Ftelescope-inspector) | v1.0.1 |  | A lightweight, searchable viewer for Laravel Telescope that reads Telescope's o… |
| 2026-11-05 07:53:19 | [jyim/laravel-plugin-market](https://www.nuget.org/packages/jyim%2Flaravel-plugin-market) | 2.0.0 | augustdai | Laravel 10.x 适配版插件市场 |
| 2026-11-05 08:04:00 | [xelqun/forms](https://www.nuget.org/packages/xelqun%2Fforms) | v0.1.0 | Jay-Are Ocero | PHP-defined, schema-driven forms for Laravel, Inertia and Vue. |
| 2026-11-05 08:06:23 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.15.0 |  | The skeleton application for the Laravel framework. |
| 2026-11-05 08:13:45 | [fayne/laravel-filament-menu](https://www.nuget.org/packages/fayne%2Flaravel-filament-menu) | v1.0.0 |  | Menu management for Filament CMS. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
