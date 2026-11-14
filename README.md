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

## Latest list — 2026-11-14 05:21 UTC

New packages created between 2026-11-14 04:18 UTC and 2026-11-14 05:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T05-21-11-776691Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 04:59:19 | [maatify/php-product](https://www.nuget.org/packages/maatify%2Fphp-product) | v1.0.0-rc.1 | Maatify | Framework-agnostic PHP library for managing Products, Variants, and configurabl… |
| 2026-11-14 05:13:27 | [trappistes/kingdee-k3cloud-sdk](https://www.nuget.org/packages/trappistes%2Fkingdee-k3cloud-sdk) | v1.0.0-beta.1 |  | 金蝶云星空（Kingdee K3 Cloud）开放平台 WebAPI 客户端 SDK |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
