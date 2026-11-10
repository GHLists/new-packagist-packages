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

## Latest list — 2026-11-10 23:19 UTC

New packages created between 2026-11-10 22:21 UTC and 2026-11-10 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T23-19-50-337632Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 22:23:15 | [jackbayliss/laravel-config-outdated](https://www.nuget.org/packages/jackbayliss%2Flaravel-config-outdated) | v1.1 | Jack Bayliss | Detect missing and outdated keys in your published Laravel config files after u… |
| 2026-11-10 22:33:55 | [ernestdefoe/slow-mail](https://www.nuget.org/packages/ernestdefoe%2Fslow-mail) | 1.0.0 | Ernest Defoe | Slow Mail: pen-pal letters between members that take time to arrive, depending… |
| 2026-11-10 22:43:03 | [4viewture/ai-labeling](https://www.nuget.org/packages/4viewture%2Fai-labeling) | 1.0.0 |  | Transparency fields for AI-generated or AI-modified files and content elements… |
| 2026-11-10 22:47:48 | [drupheus/drupheus-cs](https://www.nuget.org/packages/drupheus%2Fdrupheus-cs) | v1.0.0-alpha1 |  | Drupal coding standards, deprecation checks and modernization rules for Drupal… |
| 2026-11-10 22:51:48 | [charm/csv](https://www.nuget.org/packages/charm%2Fcsv) | 0.1.0 | Frode Børli | Fast RFC 4180 CSV encoding and decoding in PHP: a readonly Format, an Encoder a… |
| 2026-11-10 22:51:48 | [charm/jsonl](https://www.nuget.org/packages/charm%2Fjsonl) | 0.1.0 | Frode Børli | Fast JSON Lines (NDJSON) encoding and decoding in PHP: an Encoder and an increm… |
| 2026-11-10 22:51:48 | [charm/sort](https://www.nuget.org/packages/charm%2Fsort) | 0.1.0 | Frode Børli | Stable, fast sorting for PHP with a small object API: a Sorter configured once,… |
| 2026-11-10 22:54:59 | [artisanpack-ui/ecommerce-paypal](https://www.nuget.org/packages/artisanpack-ui%2Fecommerce-paypal) | v1.0.0 | Jacob Martella | PayPal gateway for the ArtisanPack UI ecommerce engine: PayPal, Pay Later, Venm… |
| 2026-11-10 23:07:18 | [shaungsimpson/release-impact](https://www.nuget.org/packages/shaungsimpson%2Frelease-impact) | v0.1.0 |  | A CLI for reviewing deployment-relevant changes in Laravel applications. |
| 2026-11-10 23:08:55 | [charm/canvas](https://www.nuget.org/packages/charm%2Fcanvas) | 0.3.0 | Frode Børli | The browser's 2D canvas API for PHP, over GD or Imagick |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
