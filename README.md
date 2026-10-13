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

## Latest list — 2026-10-13 16:21 UTC

New packages created between 2026-10-13 15:19 UTC and 2026-10-13 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T16-21-52-833213Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 15:38:19 | [petecoop/filament-toolbar-filters](https://www.nuget.org/packages/petecoop%2Ffilament-toolbar-filters) | 0.0.1 | Pete Cooper | Lift selected Filament table filters into the toolbar. |
| 2026-10-13 15:39:44 | [daika7ana/laravel-model-cache](https://www.nuget.org/packages/daika7ana%2Flaravel-model-cache) | v1.0.0 | daika7ana; Yordan | Laravel package for caching Eloquent model queries |
| 2026-10-13 15:42:49 | [sitetus/collector](https://www.nuget.org/packages/sitetus%2Fcollector) | v0.7.2 |  | Sitetus tek dosya PHP toplayicisi - salt-okunur, sirsiz, panelden imzali pull |
| 2026-10-13 15:43:01 | [sitetus/laravel-collector](https://www.nuget.org/packages/sitetus%2Flaravel-collector) | v0.7.2 |  | Composer wrapper of the Sitetus read-only collector for Laravel: same core, ins… |
| 2026-10-13 15:48:47 | [valtopina/laravel-odbc](https://www.nuget.org/packages/valtopina%2Flaravel-odbc) | v1.0.0 |  | ODBC integration for Laravel framework |
| 2026-10-13 15:49:30 | [survos/imagor-bundle](https://www.nuget.org/packages/survos%2Fimagor-bundle) | 2.41.11 |  | Symfony bundle for signed imagor URLs (presets, crops, meta) against the Survos… |
| 2026-10-13 16:02:32 | [cable8mm/laravel-portone](https://www.nuget.org/packages/cable8mm%2Flaravel-portone) | v0.1.0 |  | Laravel package for PortOne payments. |
| 2026-10-13 16:10:22 | [bensomething/craft-placard](https://www.nuget.org/packages/bensomething%2Fcraft-placard) | 1.0.0-beta.1 |  | Configurable social images for entries. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
