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

## Latest list — 2026-11-19 01:20 UTC

New packages created between 2026-11-19 00:22 UTC and 2026-11-19 01:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T01-20-36-746356Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 00:45:30 | [ajaflow/sdk](https://www.nuget.org/packages/ajaflow%2Fsdk) | v1.0.0 |  | PHP client for the AJA order API: the shop sends its orders and polls the merch… |
| 2026-11-19 00:57:17 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.34.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-19 00:58:18 | [train-horn/yii2-sound-level](https://www.nuget.org/packages/train-horn%2Fyii2-sound-level) | v1.0.0 | Train Horn | Yii 2 extension: sound pressure level at distance (inverse-square law with opti… |
| 2026-11-19 01:01:25 | [train-horn/craft-sound-level](https://www.nuget.org/packages/train-horn%2Fcraft-sound-level) | 1.0.0 | Train Horn | Twig helpers for Craft CMS 5 that estimate sound level at distance (inverse-squ… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
