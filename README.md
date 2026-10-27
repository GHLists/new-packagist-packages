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

## Latest list — 2026-10-27 11:18 UTC

New packages created between 2026-10-27 10:21 UTC and 2026-10-27 11:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T11-18-55-847664Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 10:24:50 | [elrayn/coretax-faktur](https://www.nuget.org/packages/elrayn%2Fcoretax-faktur) | v0.1.0 | Muhammad Rayhan | Generate Coretax (DJP) Faktur Pajak Keluaran XML straight from your app, with t… |
| 2026-10-27 10:34:19 | [ndate22/laravel-ndate](https://www.nuget.org/packages/ndate22%2Flaravel-ndate) | 0.1.0 | Kamal Pandey | Laravel integration for ndate22/ndate (Nepali BS/AD date converter) |
| 2026-10-27 10:36:57 | [tryhackx/flarum-homepage-blocks](https://www.nuget.org/packages/tryhackx%2Fflarum-homepage-blocks) | 2.12.0 | TryHackX | Customizable homepage blocks for tracker-style Flarum forums featuring dual sta… |
| 2026-10-27 10:44:01 | [overherz/elastic5_6_16_php8](https://www.nuget.org/packages/overherz%2Felastic5_6_16_php8) | 1.0.1 | Nicolas Ruflin | Elastica 6.2.1 fork for Elasticsearch 5.6 on PHP 7.1-8.5 |
| 2026-10-27 10:50:04 | [geekybones/typesense-bundle](https://www.nuget.org/packages/geekybones%2Ftypesense-bundle) | v0.1.0 | GeekyBones | Symfony bundle for Typesense: attribute mapping, zero-downtime reindexing, Doct… |
| 2026-10-27 10:59:14 | [michaelkaefer/table](https://www.nuget.org/packages/michaelkaefer%2Ftable) | 0.1.0 | Project Contributors | An extensible component for rendering tables |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
