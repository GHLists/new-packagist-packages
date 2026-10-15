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

## Latest list — 2026-10-15 00:21 UTC

New packages created between 2026-10-14 23:20 UTC and 2026-10-15 00:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T00-21-16-115137Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 23:43:54 | [licensekit/licensekit](https://www.nuget.org/packages/licensekit%2Flicensekit) | v0.1.0-alpha.1 | Krixx | Software licensing APIs and Filament administration for Laravel, with optional… |
| 2026-10-15 00:12:34 | [alphapay/alphapay-laravel](https://www.nuget.org/packages/alphapay%2Falphapay-laravel) | v0.1.0 | AlphaPay | Laravel SDK officiel pour l'API AlphaPay (agrégateur de paiement multi-gateway)… |
| 2026-10-15 00:12:34 | [alphapay/alphapay-php](https://www.nuget.org/packages/alphapay%2Falphapay-php) | v0.1.2 |  | Official PHP SDK for the AlphaPay payment aggregator API. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
