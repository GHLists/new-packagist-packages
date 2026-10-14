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

## Latest list — 2026-10-14 12:21 UTC

New packages created between 2026-10-14 11:21 UTC and 2026-10-14 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T12-21-26-052051Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 11:29:19 | [oscaraccountant/sdk](https://www.nuget.org/packages/oscaraccountant%2Fsdk) | v0.1.0 | OscarAI OÜ | The PHP SDK of the Oscar accounting API. |
| 2026-10-14 11:32:29 | [a-mazalov/kali-tools](https://www.nuget.org/packages/a-mazalov%2Fkali-tools) | v1.0.1 | a-mazalov | Utilities for a Laravel Project |
| 2026-10-14 11:39:53 | [stejac/code-thresholds](https://www.nuget.org/packages/stejac%2Fcode-thresholds) | v1.0.0 | Stefan Jacomeit | Dependency-free size and complexity gate for PHP that checks only changed files… |
| 2026-10-14 11:42:08 | [vendic/hyva-checkout-mirasvit-rewards](https://www.nuget.org/packages/vendic%2Fhyva-checkout-mirasvit-rewards) | 1.0.0 |  | Hyvä checkout compatibility module for Mirasvit Rewards. See: https://mirasvit.… |
| 2026-10-14 11:58:01 | [pieceofcake2/e2e-test](https://www.nuget.org/packages/pieceofcake2%2Fe2e-test) | v1.0.0 |  | Browser end-to-end tests for CakePHP 2 applications with Symfony Panther and PH… |
| 2026-10-14 12:00:16 | [irnoti/laravel-sms-panel-api](https://www.nuget.org/packages/irnoti%2Flaravel-sms-panel-api) | v1.0.0 | irnoti | Official Laravel SDK for the irnoti platform API — SMS (single, bulk, pattern,… |
| 2026-10-14 12:02:02 | [koh/typo3-fal-s3](https://www.nuget.org/packages/koh%2Ftypo3-fal-s3) | v1.0.4 | Kai Ole Hartwig | TYPO3 FAL driver for Amazon S3: media without a FUSE mount, one IAM role per te… |
| 2026-10-14 12:08:42 | [php-es-orm/es-orm](https://www.nuget.org/packages/php-es-orm%2Fes-orm) | v1.2.0 |  | An Eloquent-style, type-safe, production-ready Elasticsearch ORM for PHP, with… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
