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

## Latest list — 2026-11-03 19:21 UTC

New packages created between 2026-11-03 18:19 UTC and 2026-11-03 19:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T19-21-41-957215Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 18:25:39 | [ocherenkov/laravel-searchable-trait](https://www.nuget.org/packages/ocherenkov%2Flaravel-searchable-trait) | v1.0.1 | Oleh Cherenkov | A reusable Eloquent trait for case-insensitive searches across columns, concate… |
| 2026-11-03 18:26:07 | [sol-parts/payum-upc](https://www.nuget.org/packages/sol-parts%2Fpayum-upc) | v1.0.0 | Andrii Didenko | Payum gateway for UPC e-Commerce Connect: hosted checkout, signed notifications… |
| 2026-11-03 18:31:19 | [sightpress/plugin-core](https://www.nuget.org/packages/sightpress%2Fplugin-core) | 1.0.0 |  | The code every SightPress plugin shares: the Plugin API, public value types, te… |
| 2026-11-03 18:43:54 | [wg-vn/lunar-table-rate-shipping](https://www.nuget.org/packages/wg-vn%2Flunar-table-rate-shipping) | v2.0.0-alpha.6.1 | Lunar; Vested Networks | Lunar's table rate shipping add-on for the Inertia panel (lunarphp/panel 2.x),… |
| 2026-11-03 19:00:09 | [prinsfrank/core-14-font-metrics](https://www.nuget.org/packages/prinsfrank%2Fcore-14-font-metrics) | v1.0.0 |  | Font metrics for the core 14 PostScript Fonts |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
