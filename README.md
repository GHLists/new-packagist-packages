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

## Latest list — 2026-10-16 16:21 UTC

New packages created between 2026-10-16 15:20 UTC and 2026-10-16 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T16-21-38-227345Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 15:26:47 | [cloudcastle/connect-manager](https://www.nuget.org/packages/cloudcastle%2Fconnect-manager) | v0.0.1 | CloudCastle | Production-ready PHP 8.1+ Connect Manager library (CloudCastle). |
| 2026-10-16 15:27:55 | [andriichuk/liqpay-php-sdk](https://www.nuget.org/packages/andriichuk%2Fliqpay-php-sdk) | 0.1.0 | Serhii Andriichuk | Fluent PHP SDK for LiqPay API v7 with typed array responses, PSR-18 HTTP client… |
| 2026-10-16 15:32:30 | [proudnerds/pn-backend-manual](https://www.nuget.org/packages/proudnerds%2Fpn-backend-manual) | 1.0.1 | Jacco van der Post | Editor manuals in Markdown, registered by a sitepackage and shown as dashboard… |
| 2026-10-16 15:46:05 | [mteu/advisory-assessor](https://www.nuget.org/packages/mteu%2Fadvisory-assessor) | 0.1.0 | Martin Adler | PHP library for recording triage decisions on security advisory findings as VEX… |
| 2026-10-16 15:59:44 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.6 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-16 16:04:17 | [metricpanel/php](https://www.nuget.org/packages/metricpanel%2Fphp) | v0.1.0 |  | Authenticated MetricPanel server events and exact iGaming payment delivery |
| 2026-10-16 16:04:20 | [metricpanel/laravel](https://www.nuget.org/packages/metricpanel%2Flaravel) | v0.1.0 |  | Queued MetricPanel delivery for Laravel |
| 2026-10-16 16:05:25 | [fof/mailtrap-mail](https://www.nuget.org/packages/fof%2Fmailtrap-mail) | 2.0.0 | FriendsOfFlarum | Send your forum mail through the Mailtrap API, or catch it in a Mailtrap sandbox |
| 2026-10-16 16:10:23 | [biffbangpow/deployer](https://www.nuget.org/packages/biffbangpow%2Fdeployer) | v1.0.0 |  | Compatibility package for DorsetDigital Silverstripe Deploy |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
