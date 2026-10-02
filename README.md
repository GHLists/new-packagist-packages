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

## Latest list — 2026-10-02 17:20 UTC

New packages created between 2026-10-02 16:21 UTC and 2026-10-02 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T17-20-21-177984Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 16:45:22 | [rahatsagor/laravel-runtime-system](https://www.nuget.org/packages/rahatsagor%2Flaravel-runtime-system) | v1.0.0 | Rahat Sagor | Runtime core installer and application validation layer for RS Application prod… |
| 2026-10-02 16:47:10 | [mattstein/usesend-laravel](https://www.nuget.org/packages/mattstein%2Fusesend-laravel) | v0.1.0 | Matt Stein | Laravel mail transport for useSend: send transactional email through the useSen… |
| 2026-10-02 16:49:33 | [mage2kishan/module-mage-pos](https://www.nuget.org/packages/mage2kishan%2Fmodule-mage-pos) | 1.0.12 | Kishan Savaliya | Panth MagePos - a full point of sale (POS) for Magento 2. Standalone touch-frie… |
| 2026-10-02 16:49:54 | [duncanmcclean/best-before](https://www.nuget.org/packages/duncanmcclean%2Fbest-before) | v1.0.0 | Duncan McClean | Give temporary classes and methods a best before date, then fail CI once they'v… |
| 2026-10-02 16:52:28 | [fundrik/toolbox](https://www.nuget.org/packages/fundrik%2Ftoolbox) | v1.0.0 | Denis Yanchevskiy | A collection of general-purpose PHP utilities used across Fundrik projects |
| 2026-10-02 16:59:19 | [webong/proxy](https://www.nuget.org/packages/webong%2Fproxy) | v0.1.0 |  | Webhook proxy system for scoped webhook routing and delivery |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
