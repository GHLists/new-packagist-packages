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

## Latest list — 2026-10-06 06:21 UTC

New packages created between 2026-10-06 05:21 UTC and 2026-10-06 06:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T06-21-08-194038Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 05:23:30 | [zactonz/zactonz-php](https://www.nuget.org/packages/zactonz%2Fzactonz-php) | v0.1.0 | Zactonz Technologies | Official PHP client for the Zactonz REST APIs: QR codes, barcodes, screenshots… |
| 2026-10-06 05:34:15 | [khaled110/launchpoint](https://www.nuget.org/packages/khaled110%2Flaunchpoint) | v1.0.1 |  | Laravel Starter Kit for API |
| 2026-10-06 05:41:11 | [felixkerser/laravel-shopify-filestorage](https://www.nuget.org/packages/felixkerser%2Flaravel-shopify-filestorage) | v0.0.1 | Kyrylo Malovanyi | Fluent Laravel SDK for Shopify's staged file upload pipeline and CDN image tran… |
| 2026-10-06 05:42:59 | [mage2kishan/module-eu-withdrawal](https://www.nuget.org/packages/mage2kishan%2Fmodule-eu-withdrawal) | 1.1.11 | Kishan Savaliya | Panth EU Withdrawal Button - a clear, accessible digital withdrawal (cancellati… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
