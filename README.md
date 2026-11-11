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

## Latest list — 2026-11-11 15:19 UTC

New packages created between 2026-11-11 14:20 UTC and 2026-11-11 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T15-19-34-536358Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 14:24:16 | [etel/coding-standard](https://www.nuget.org/packages/etel%2Fcoding-standard) | v0.2.0 | Mykola Zyk | The coding standard of the etel projects: a php-cs-fixer rule set with its fixe… |
| 2026-11-11 14:25:16 | [tilttek/collections-bundle](https://www.nuget.org/packages/tilttek%2Fcollections-bundle) | 0.1.0-alpha | Philippe Gamache | Collectibles for Symfony on tilttek/collections: the catalog in configuration o… |
| 2026-11-11 14:25:16 | [tilttek/dice-bundle](https://www.nuget.org/packages/tilttek%2Fdice-bundle) | 0.1.0-alpha | Philippe Gamache | Dice for Symfony on tilttek/dice: limits, custom dice and notations from the co… |
| 2026-11-11 14:25:16 | [tilttek/exchange](https://www.nuget.org/packages/tilttek%2Fexchange) | 0.1.0-alpha | Philippe Gamache | Exchanges for gamification: rewards bought with points in two steps, a reservat… |
| 2026-11-11 14:30:08 | [rrcatto/omnipay-stitch-express](https://www.nuget.org/packages/rrcatto%2Fomnipay-stitch-express) | v1.0.0 | Richard Catto | Stitch Express gateway for the Omnipay payment processing library: payment link… |
| 2026-11-11 14:36:00 | [helturkey/php-webtrawler](https://www.nuget.org/packages/helturkey%2Fphp-webtrawler) | v1.0.0 |  | A PHP-first web scraping and crawling toolkit with adaptive extraction, concurr… |
| 2026-11-11 15:07:49 | [andmemasin/query-builder](https://www.nuget.org/packages/andmemasin%2Fquery-builder) | 0.1.0 |  | Framework-free query rules: turn rules JSON into a SQL WHERE clause with bound… |
| 2026-11-11 15:11:46 | [isbnlab/onix](https://www.nuget.org/packages/isbnlab%2Fonix) | v0.1.0 | ISBNLab | Streaming ONIX for Books reader for PHP: ONIX 3.0/3.1 and 2.1, reference and sh… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
