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

## Latest list — 2026-11-12 05:21 UTC

New packages created between 2026-11-12 04:21 UTC and 2026-11-12 05:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T05-21-36-945438Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 04:32:56 | [ohauthcat/ohauthcat-php](https://www.nuget.org/packages/ohauthcat%2Fohauthcat-php) | v0.0.2 | OhAuthCat | OhAuthCat server SDK: enterprise SSO and SCIM directory sync |
| 2026-11-12 05:07:24 | [bayurifkialghifari/dynamic-qris-php-client](https://www.nuget.org/packages/bayurifkialghifari%2Fdynamic-qris-php-client) | v0.1.1 | Bayu Rifki Alghifari | Laravel client with typed DTOs for the Dynamic QRIS ShopeePay and GoPay gateway |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
