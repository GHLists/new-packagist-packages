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

## Latest list — 2026-10-11 08:22 UTC

New packages created between 2026-10-11 07:21 UTC and 2026-10-11 08:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T08-22-01-448762Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 07:21:45 | [selli/ticketing](https://www.nuget.org/packages/selli%2Fticketing) | v1.0.0 | Sellinnate | The headless, multi-tenant help-desk engine for Laravel: tickets on any model,… |
| 2026-10-11 07:28:58 | [tmonier/sylius-bulk-actions-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-bulk-actions-plugin) | v1.0.0 | Thibaut Monier | Bulk actions for the Sylius 2 admin grids: enable/disable, taxons and channels… |
| 2026-10-11 07:34:15 | [tmonier/sylius-facturx-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-facturx-plugin) | v1.0.0 | Thibaut Monier | Factur-X / ZUGFeRD (EN 16931) electronic invoices for the Sylius 2 Invoicing Pl… |
| 2026-10-11 07:35:03 | [tmonier/sylius-audit-log-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-audit-log-plugin) | v1.0.0 | Thibaut Monier | Audit log of admin changes (who changed what, when) for the Sylius 2 admin panel |
| 2026-10-11 07:41:36 | [endthink/part-xpay](https://www.nuget.org/packages/endthink%2Fpart-xpay) | v1.0.0 | endthink | ET微信小程序虚拟支付插件 |
| 2026-10-11 07:51:22 | [abdulkadir/seo-redirect-manager](https://www.nuget.org/packages/abdulkadir%2Fseo-redirect-manager) | 1.0.1 | Abdulkadir Agoliya | Enterprise SEO Redirect Manager for Craft CMS 5. High-performance exact and reg… |
| 2026-10-11 08:00:41 | [iamankitthapar/laravel-data-retention](https://www.nuget.org/packages/iamankitthapar%2Flaravel-data-retention) | v1.0.0 |  | A Laravel-first, policy-driven data retention engine. |
| 2026-10-11 08:03:26 | [3neti/election-ceremonies](https://www.nuget.org/packages/3neti%2Felection-ceremonies) | v0.1.0 |  | Offline election ceremonies and signed election bundle verification |
| 2026-10-11 08:03:26 | [3neti/election-ph](https://www.nuget.org/packages/3neti%2Felection-ph) | v0.1.0 |  | Philippine election profile and registry builder for election ceremonies |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
