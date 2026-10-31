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

## Latest list — 2026-10-31 07:18 UTC

New packages created between 2026-10-31 06:20 UTC and 2026-10-31 07:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T07-18-31-503843Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 06:35:24 | [phattarachai/tungsten](https://www.nuget.org/packages/phattarachai%2Ftungsten) | v0.2.0 | Phattarachai Chaimongkol | An Inertia + React admin panel kernel and UI kit for Laravel: panels, pages, a… |
| 2026-10-31 06:38:46 | [islam016/laravel-safe-checkout](https://www.nuget.org/packages/islam016%2Flaravel-safe-checkout) | v1.0.0 | Islam Gaber | Safe checkout for Laravel with Moyasar and Tap: idempotent payment creation, ve… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
