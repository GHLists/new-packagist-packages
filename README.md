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

## Latest list — 2026-10-23 09:19 UTC

New packages created between 2026-10-23 08:19 UTC and 2026-10-23 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T09-19-50-861205Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 08:23:52 | [infosoftas/info-subscription-php](https://www.nuget.org/packages/infosoftas%2Finfo-subscription-php) | 2026.10.2 |  | PHP SDK for INFO-Subscription API generated with Microsoft Kiota. |
| 2026-10-23 08:31:23 | [webgriffe/phpunit-dist](https://www.nuget.org/packages/webgriffe%2Fphpunit-dist) | 13.4.3 |  | PHPUnit phar distribution for Webgriffe projects |
| 2026-10-23 08:31:30 | [robertboes/laravel-interlock](https://www.nuget.org/packages/robertboes%2Flaravel-interlock) | v0.1.0 | Robert Boes | Keep the state of an Eloquent model consistent with a declared transition graph. |
| 2026-10-23 08:44:00 | [meromiti/meromiti](https://www.nuget.org/packages/meromiti%2Fmeromiti) | v1.0.0 | Inline Tech Solution | Universal Bikram Sambat (B.S.) Nepali calendar engine and date converter for PH… |
| 2026-10-23 09:11:53 | [rohama/koin-sadad](https://www.nuget.org/packages/rohama%2Fkoin-sadad) | 2.2.1 | Rohama | Koin — SADAD (Bank Melli) gateway driver (REST WebAPI v0) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
