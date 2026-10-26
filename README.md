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

## Latest list — 2026-10-26 14:20 UTC

New packages created between 2026-10-26 13:21 UTC and 2026-10-26 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T14-20-29-798825Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 13:31:05 | [freemagento/module-base](https://www.nuget.org/packages/freemagento%2Fmodule-base) | v1.0.0 | FreeMagento (Mentalworkz Ltd) | FreeMagento Base - shared foundation for FreeMagento extensions: installed-modu… |
| 2026-10-26 13:31:26 | [freemagento/module-customer-two-factor](https://www.nuget.org/packages/freemagento%2Fmodule-customer-two-factor) | v1.0.0 | FreeMagento (Mentalworkz Ltd) | Email one-time-code two-factor authentication for Magento 2 storefront customer… |
| 2026-10-26 13:35:55 | [back-to-code/peil-laravel](https://www.nuget.org/packages/back-to-code%2Fpeil-laravel) | v0.1.0 |  | Laravel integration for Peil: a queue canary and a pingPeil schedule macro. |
| 2026-10-26 13:42:17 | [awl/supreme-sniffle](https://www.nuget.org/packages/awl%2Fsupreme-sniffle) | 1.0.0 | Andrew Longosz | Mock package to test Packagist integration |
| 2026-10-26 13:50:41 | [ivanvasechko/oukitel-php-sdk](https://www.nuget.org/packages/ivanvasechko%2Foukitel-php-sdk) | v0.3.0 | Ivan Vasechko | Unofficial framework-agnostic Oukitel power-station SDK with typed telemetry an… |
| 2026-10-26 14:03:07 | [symfony/ai-doctrine-store](https://www.nuget.org/packages/symfony%2Fai-doctrine-store) | v1.0.0-BETA1 | Christopher Hertel; Symfony C… | Doctrine ORM bridge for Symfony AI, embedding entities on their own table or mi… |
| 2026-10-26 14:05:49 | [mjoris/router](https://www.nuget.org/packages/mjoris%2Frouter) | v2.0.0 | Joris Maervoet; Bram(us) Van… | A lightweight and simple object oriented PHP router, small enough to read and u… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
