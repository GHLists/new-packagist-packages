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

## Latest list — 2026-10-23 07:20 UTC

New packages created between 2026-10-23 06:19 UTC and 2026-10-23 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T07-20-59-837025Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 06:21:22 | [isaacjuwon/probe](https://www.nuget.org/packages/isaacjuwon%2Fprobe) | v0.1.0 | Isaac Juwon | Dev-only in-app REST client for Laravel |
| 2026-10-23 06:23:52 | [nowo-tech/manual-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fmanual-kit-bundle) | v1.0.1 | Héctor Franco Aceituno; Nowo.… | In-app product manual for Symfony from your docs/manual Markdown: one source fo… |
| 2026-10-23 06:26:04 | [davingm/laravel-devtools](https://www.nuget.org/packages/davingm%2Flaravel-devtools) | v1.0.0 |  | Laravel 11, 12, and 13 development tools and generators. |
| 2026-10-23 06:43:28 | [rasuvaeff/pinned-http-client](https://www.nuget.org/packages/rasuvaeff%2Fpinned-http-client) | v0.1.0 | Victor Razuvaev | PSR-18 client for untrusted URLs: resolves the host, checks every address and p… |
| 2026-10-23 06:48:00 | [exportaccelerator/productfeed](https://www.nuget.org/packages/exportaccelerator%2Fproductfeed) | v1.0.0 |  | Product feed module for Magento 2.4.6 and above |
| 2026-10-23 06:54:26 | [shopper/migrator](https://www.nuget.org/packages/shopper%2Fmigrator) | v1.0.0 | Arthur Monney | Migrate your store from other e-commerce platforms to Shopper |
| 2026-10-23 06:54:47 | [paul-elpidorou/laravel-custom-log](https://www.nuget.org/packages/paul-elpidorou%2Flaravel-custom-log) | v1.0.0 | paul-elpidorou | This is my package laravel-custom-log |
| 2026-10-23 06:59:28 | [anun333/openhealthcare-common](https://www.nuget.org/packages/anun333%2Fopenhealthcare-common) | v1.0.0 |  | Code shared by the openhealthcare OpenEMR modules: one compatibility layer for… |
| 2026-10-23 07:10:17 | [rohama/koin-nextpay](https://www.nuget.org/packages/rohama%2Fkoin-nextpay) | 2.2.0 | Rohama | Koin — NextPay gateway driver (direct gateway) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
