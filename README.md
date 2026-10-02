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

## Latest list — 2026-10-02 23:21 UTC

New packages created between 2026-10-02 22:19 UTC and 2026-10-02 23:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T23-21-44-640996Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 22:28:30 | [reyhan-commerce/core](https://www.nuget.org/packages/reyhan-commerce%2Fcore) | v1.0.0 | Reyhan Commerce Core Team | Next-Gen Headless E-Commerce Core Framework for Laravel 13 |
| 2026-10-02 22:35:29 | [reyhan-commerce/reyhan](https://www.nuget.org/packages/reyhan-commerce%2Freyhan) | v1.0.0 |  | Reyhan Commerce — Headless E-Commerce Framework for Iran. |
| 2026-10-02 22:55:16 | [ahmed-aliraqi/laravel-deep-link](https://www.nuget.org/packages/ahmed-aliraqi%2Flaravel-deep-link) | v1.0.0 | Ahmed Fathy | Universal Links, Android App Links and smart landing pages for Laravel: shareab… |
| 2026-10-02 23:06:30 | [mandrael/contao-maplibre](https://www.nuget.org/packages/mandrael%2Fcontao-maplibre) | 0.2.0 | Michael Gasperl | MapLibre-Karten für Contao mit OpenFreeMap (© OpenMapTiles, Data from OpenStree… |
| 2026-10-02 23:12:28 | [robyajo/laravel-security-monitor](https://www.nuget.org/packages/robyajo%2Flaravel-security-monitor) | v2.0.0 | Roby | Enterprise-grade headless self-hosted WAF, threat detection engine, zero-tolera… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
