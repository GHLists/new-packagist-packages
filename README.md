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

## Latest list — 2026-10-01 21:19 UTC

New packages created between 2026-10-01 20:20 UTC and 2026-10-01 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T21-19-00-279557Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 20:20:47 | [maukirim/sdk](https://www.nuget.org/packages/maukirim%2Fsdk) | v1.0.0 |  | Official PHP SDK for MauKirim - managed WhatsApp gateway for OTP, templated not… |
| 2026-10-01 20:29:12 | [trail/trail](https://www.nuget.org/packages/trail%2Ftrail) | 0.2.0 | Alex Brindley | A base skeleton project for the trail framework |
| 2026-10-01 20:35:45 | [slpxxv/ksef-php-client](https://www.nuget.org/packages/slpxxv%2Fksef-php-client) | v0.1.0 |  | A typed PHP client for KSeF API 2.0. |
| 2026-10-01 21:15:20 | [ctterrlt/easy-tools](https://www.nuget.org/packages/ctterrlt%2Feasy-tools) | v1.0.0 | Tursi Christian | A variety of tools that make any developer's life much easier |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
