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

## Latest list — 2026-11-06 07:19 UTC

New packages created between 2026-11-06 06:19 UTC and 2026-11-06 07:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T07-19-43-484806Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 06:24:34 | [kawayanmedia/persistence](https://www.nuget.org/packages/kawayanmedia%2Fpersistence) | 0.1.0 |  | Tiny database abstraction used by the Kawayan Media HR packages for their write… |
| 2026-11-06 06:24:37 | [kawayanmedia/dtr-pdf](https://www.nuget.org/packages/kawayanmedia%2Fdtr-pdf) | 0.1.0 |  | Framework-agnostic Daily Time Record (DTR) computation and PDF generator |
| 2026-11-06 06:24:39 | [kawayanmedia/pds](https://www.nuget.org/packages/kawayanmedia%2Fpds) | 0.1.0 |  | Framework-agnostic Personal Data Sheet (PDS / CS Form 212) PDF generator |
| 2026-11-06 06:24:41 | [kawayanmedia/leave-forms](https://www.nuget.org/packages/kawayanmedia%2Fleave-forms) | 0.1.0 |  | Framework-agnostic Service Record, leave certification, leave application, CTO,… |
| 2026-11-06 06:36:51 | [stateforge/scenario-symfony-ai](https://www.nuget.org/packages/stateforge%2Fscenario-symfony-ai) | 1.0.0 | Christina Koenig | Symfony adapter for Stateforge Scenario AI - AI-assisted generation of Scenario… |
| 2026-11-06 06:58:57 | [konekqr/laravel](https://www.nuget.org/packages/konekqr%2Flaravel) | v0.1.0 |  | Konek QR API client, facade and webhook verification middleware for Laravel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
