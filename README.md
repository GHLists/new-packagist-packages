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

## Latest list — 2026-11-05 07:21 UTC

New packages created between 2026-11-05 06:19 UTC and 2026-11-05 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T07-21-28-834171Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 06:21:09 | [itmosoft/laravel-returns](https://www.nuget.org/packages/itmosoft%2Flaravel-returns) | v1.0.0 |  | Return merchandise authorization and inspection workflows for Laravel commerce… |
| 2026-11-05 06:27:23 | [iamjuan/spamast-sso-client](https://www.nuget.org/packages/iamjuan%2Fspamast-sso-client) | v1.0.3 |  | SPAMAST SSO client for Laravel apps: sign in from the hub, pending accounts, an… |
| 2026-11-05 06:28:11 | [itmosoft/laravel-refunds](https://www.nuget.org/packages/itmosoft%2Flaravel-refunds) | v1.0.0 |  | Payment-provider-agnostic refund records and workflows for Laravel applications. |
| 2026-11-05 06:32:44 | [itmosoft/laravel-invoices](https://www.nuget.org/packages/itmosoft%2Flaravel-invoices) | v1.0.0 |  | Invoice records, line snapshots, numbering and payment tracking for Laravel app… |
| 2026-11-05 06:38:02 | [itmosoft/laravel-payments](https://www.nuget.org/packages/itmosoft%2Flaravel-payments) | v1.0.0 |  | Gateway-agnostic payment intents, transactions and webhook event tracking for L… |
| 2026-11-05 07:09:16 | [runchance/rcmaker-php](https://www.nuget.org/packages/runchance%2Frcmaker-php) | v1.0.0 | wobless | High-performance PHP applications with project initialization, isolated app pro… |
| 2026-11-05 07:11:37 | [eduardoapatat/laravel-inertia-datatable](https://www.nuget.org/packages/eduardoapatat%2Flaravel-inertia-datatable) | v0.1.0 | Eduardo Apata Tito | Server-side DataTables for Laravel + Inertia + React: pagination, sorting, filt… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
