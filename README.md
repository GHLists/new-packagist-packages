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

## Latest list — 2026-11-04 08:20 UTC

New packages created between 2026-11-04 07:21 UTC and 2026-11-04 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T08-20-08-459501Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 07:23:06 | [itmosoft/laravel-product-catalog](https://www.nuget.org/packages/itmosoft%2Flaravel-product-catalog) | v1.0.0 |  | A reusable Laravel product catalog package with products, categories, brands, a… |
| 2026-11-04 07:48:00 | [tacraft-sociality/flarum-user-uid](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-user-uid) | 1.0.0 | Tacraft Sociality | Show the numeric user id on the user card. |
| 2026-11-04 08:07:59 | [leqq00/phalapiredis](https://www.nuget.org/packages/leqq00%2Fphalapiredis) | v8.0.0 | dongxuepeng; leqq00 | 兼容 phalapi/redis 所有方法；Redis 增强版，支持 PHP 8.0+。 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
