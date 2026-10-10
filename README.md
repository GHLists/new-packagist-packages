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

## Latest list — 2026-10-10 03:19 UTC

New packages created between 2026-10-10 02:21 UTC and 2026-10-10 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T03-19-23-46139Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 03:00:12 | [jbflores24/framework](https://www.nuget.org/packages/jbflores24%2Fframework) | v1.0.0 |  | Miniframework PHP 8.2 para APIs REST. |
| 2026-10-10 03:00:12 | [jbflores24/skeleton](https://www.nuget.org/packages/jbflores24%2Fskeleton) | v1.0.0 |  | Proyecto base para APIs REST con JB Framework. |
| 2026-10-10 03:17:53 | [canebaycomputers/valorpay](https://www.nuget.org/packages/canebaycomputers%2Fvalorpay) | v0.1.0 | Cane Bay Computers | Laravel client for ValorPay: hosted payment pages, transaction lookups, card to… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
