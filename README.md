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

## Latest list — 2026-11-26 20:21 UTC

New packages created between 2026-11-26 19:19 UTC and 2026-11-26 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T20-21-26-378403Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 19:40:56 | [loki-checkout/magento2-at](https://www.nuget.org/packages/loki-checkout%2Fmagento2-at) | 1.0.0 |  | Austrian settings for LokiCheckout |
| 2026-11-26 19:47:25 | [loki-checkout/magento2-br](https://www.nuget.org/packages/loki-checkout%2Fmagento2-br) | 1.0.0 |  | Brazilian settings for LokiCheckout |
| 2026-11-26 19:47:27 | [loki-checkout/magento2-au](https://www.nuget.org/packages/loki-checkout%2Fmagento2-au) | 1.0.0 |  | Australian settings for LokiCheckout |
| 2026-11-26 19:57:00 | [amwaluddinlubis/ci4-tabel-form-helper](https://www.nuget.org/packages/amwaluddinlubis%2Fci4-tabel-form-helper) | v1.1.0 | Amwaluddin Lubis | Helper tabel daftar dan form modal CRUD untuk CodeIgniter 4: tabel_bantu() + fo… |
| 2026-11-26 20:20:29 | [adachsoft/social-post-contracts](https://www.nuget.org/packages/adachsoft%2Fsocial-post-contracts) | v0.1.0 | Arkadiusz Adach | Provider-independent contracts and models for publishing social media posts in… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
