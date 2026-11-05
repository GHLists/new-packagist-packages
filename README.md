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

## Latest list — 2026-11-05 12:20 UTC

New packages created between 2026-11-05 11:21 UTC and 2026-11-05 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T12-20-50-778921Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 11:26:53 | [o3-shop/paypal-checkout](https://www.nuget.org/packages/o3-shop%2Fpaypal-checkout) | v1.0.0 | O3-Shop; OXID eSales AG | O3-Shop PayPal Checkout module (fork of oxid-solution-catalysts/paypal-module) |
| 2026-11-05 11:34:48 | [martin-juul/doctrine-duckdb-driver](https://www.nuget.org/packages/martin-juul%2Fdoctrine-duckdb-driver) | 1.0.0 | Martin Juul Christiansen | Doctrine DBAL driver and platform for DuckDB through the native ext-duckdb exte… |
| 2026-11-05 11:40:50 | [intragile/laravel-nav-online-szamla](https://www.nuget.org/packages/intragile%2Flaravel-nav-online-szamla) | v1.0.0 | IntrAgile Kft. | Complete, Laravel-native client for the Hungarian NAV Online Számla (Online Inv… |
| 2026-11-05 11:42:10 | [k1roshio/octane-driver-rearm](https://www.nuget.org/packages/k1roshio%2Foctane-driver-rearm) | v0.1.2 | k1roshio | Laravel Octane driver and MessagePack Unix-socket worker for the Rearm Rust app… |
| 2026-11-05 11:49:56 | [mindtwo/base-security-txt](https://www.nuget.org/packages/mindtwo%2Fbase-security-txt) | v1.0.0 | mindtwo GmbH | Framework-agnostic core of the mindtwo security.txt packages: validates input a… |
| 2026-11-05 11:49:56 | [mindtwo/craftcms-security-txt](https://www.nuget.org/packages/mindtwo%2Fcraftcms-security-txt) | v1.0.0 | mindtwo GmbH | Craft CMS plugin that serves an RFC 9116 security.txt per site, maintained in t… |
| 2026-11-05 11:49:56 | [mindtwo/statamic-security-txt](https://www.nuget.org/packages/mindtwo%2Fstatamic-security-txt) | v1.0.0 | mindtwo GmbH | Statamic addon that serves an RFC 9116 security.txt per site from a global set,… |
| 2026-11-05 11:49:56 | [mindtwo/wordpress-security-txt](https://www.nuget.org/packages/mindtwo%2Fwordpress-security-txt) | v1.0.0 | mindtwo GmbH | WordPress plugin that serves an RFC 9116 security.txt maintained under Settings… |
| 2026-11-05 12:00:23 | [motivar/extend-wp](https://www.nuget.org/packages/motivar%2Fextend-wp) | 1.15.0 | Motivar | Extend WordPress with custom functionality |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
