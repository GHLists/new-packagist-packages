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

## Latest list — 2026-09-28 04:19 UTC

New packages created between 2026-09-28 03:19 UTC and 2026-09-28 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T04-19-47-004739Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 03:24:16 | [kasera/kasera-pay](https://www.nuget.org/packages/kasera%2Fkasera-pay) | v0.1.0 |  | Official PHP SDK for Kasera Pay: accept QRIS and Virtual Account payments in In… |
| 2026-09-28 03:36:57 | [runapi-ai/typesafe](https://www.nuget.org/packages/runapi-ai%2Ftypesafe) | v0.2.0 | RunAPI | RunAPI TypeSafe Composer package for PHP applications |
| 2026-09-28 04:07:53 | [medigital-dev/ci4-base](https://www.nuget.org/packages/medigital-dev%2Fci4-base) | v1.0.0 |  | Base model dan util reusable untuk project CodeIgniter 4 (UUID PK, soft delete,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
