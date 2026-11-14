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

## Latest list — 2026-11-14 11:19 UTC

New packages created between 2026-11-14 10:20 UTC and 2026-11-14 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T11-19-17-487889Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 10:22:23 | [flashpi/flashpi-php](https://www.nuget.org/packages/flashpi%2Fflashpi-php) | v0.1.0 | SIGNIADIGITAL S.A. | The official PHP SDK for Flashpi, the electronic invoicing API for Ecuador's SR… |
| 2026-11-14 10:26:34 | [siellabs/siel](https://www.nuget.org/packages/siellabs%2Fsiel) | v0.1.0 | Siel Labs | The Siel SMS API for PHP: messages, batches, OTP codes, prices and webhook sign… |
| 2026-11-14 11:17:02 | [hamza-wakrim/laravel-safe-migrations](https://www.nuget.org/packages/hamza-wakrim%2Flaravel-safe-migrations) | v1.0.0 |  | Catch dangerous Laravel migrations (dropped or renamed columns, blocking indexe… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
