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

## Latest list — 2026-10-22 10:22 UTC

New packages created between 2026-10-22 09:19 UTC and 2026-10-22 10:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T10-22-07-988539Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 09:24:37 | [omniboost/aws-iam-proof-auth](https://www.nuget.org/packages/omniboost%2Faws-iam-proof-auth) | v0.1.0 |  | Service-to-service authentication with the caller's AWS IAM identity: sign outg… |
| 2026-10-22 09:35:48 | [ciiixid/laravel-db-timetravel](https://www.nuget.org/packages/ciiixid%2Flaravel-db-timetravel) | v1.0.0 | Ciiixid | A local database time-travel snapshot CLI tool for Laravel developers |
| 2026-10-22 09:42:50 | [spryker/merchant-sales-invoice](https://www.nuget.org/packages/spryker%2Fmerchant-sales-invoice) | 1.0.0 |  | MerchantSalesInvoice module |
| 2026-10-22 09:50:59 | [pieceofcake2/filebinder](https://www.nuget.org/packages/pieceofcake2%2Ffilebinder) | v2.9.0 | fusic | Simple file attachment plugin for CakePHP 2: local files, database and Amazon S… |
| 2026-10-22 09:53:15 | [jund-fauz/laravel-raw-query-builder](https://www.nuget.org/packages/jund-fauz%2Flaravel-raw-query-builder) | v1.0.1 | jund-fauz | Build raw query in laravel using helper function, like build a normal query in… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
