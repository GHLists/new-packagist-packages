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

## Latest list — 2026-11-05 06:19 UTC

New packages created between 2026-11-05 05:21 UTC and 2026-11-05 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T06-19-58-1603Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 05:45:53 | [jyim/laravel-plugin-market](https://www.nuget.org/packages/jyim%2Flaravel-plugin-market) | 1.0.0 | augustdai |  |
| 2026-11-05 05:46:13 | [jyim/laravel-plugin](https://www.nuget.org/packages/jyim%2Flaravel-plugin) | 1.0.0 | augustdai |  |
| 2026-11-05 06:13:17 | [itmosoft/laravel-shipping](https://www.nuget.org/packages/itmosoft%2Flaravel-shipping) | v1.0.0 |  | Shipping zones, methods, rates, quotes, shipments and tracking for Laravel appl… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
