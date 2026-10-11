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

## Latest list — 2026-10-11 13:21 UTC

New packages created between 2026-10-11 12:22 UTC and 2026-10-11 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T13-21-01-78801Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 12:25:19 | [keyvanarasteh/laravel-bones](https://www.nuget.org/packages/keyvanarasteh%2Flaravel-bones) | 1.1.1 | Keyvan Arasteh | An X-ray for your Laravel application: explore its routes, view nodes and packa… |
| 2026-10-11 12:49:29 | [ascariodev/sereno-laravel](https://www.nuget.org/packages/ascariodev%2Fsereno-laravel) | v0.2.1 |  | Sends Laravel logs to Sereno project channels. |
| 2026-10-11 13:18:19 | [clarilens/type-locale](https://www.nuget.org/packages/clarilens%2Ftype-locale) | 0.0.1 | Farkhat Sakibaev |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
