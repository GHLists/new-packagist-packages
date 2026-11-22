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

## Latest list — 2026-11-22 18:18 UTC

New packages created between 2026-11-22 17:21 UTC and 2026-11-22 18:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T18-18-54-465958Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 17:28:18 | [tournayrelabs/phpstan-rules](https://www.nuget.org/packages/tournayrelabs%2Fphpstan-rules) | v0.1.0 |  | PHPStan rules you can enable one by one through configuration |
| 2026-11-22 17:45:31 | [silvershop-suite/food-information](https://www.nuget.org/packages/silvershop-suite%2Ffood-information) | 1.0.0 | Remy Vaartjes; SilverShop-Sui… | Food information for SilverShop (CMS 6), usable by any shop that sells food: an… |
| 2026-11-22 17:47:09 | [adhir2099/initials-avatar](https://www.nuget.org/packages/adhir2099%2Finitials-avatar) | v1.0.0 | Adhir Serrano | Zero-dependency PHP 8.2+ initials avatar generator supporting SVG and GD PNG re… |
| 2026-11-22 18:09:58 | [nwidart/metrics-store](https://www.nuget.org/packages/nwidart%2Fmetrics-store) | 0.1.1 | Nicolas Widart | Cross-process aggregation for OpenTelemetry metrics in shared-nothing PHP runti… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
