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

## Latest list — 2026-11-25 19:22 UTC

New packages created between 2026-11-25 18:20 UTC and 2026-11-25 19:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T19-22-38-628944Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 18:29:48 | [card2k/card2k-php](https://www.nuget.org/packages/card2k%2Fcard2k-php) | v0.1.0 |  | SDK PHP chính thức cho API v3 của Card2K: nạp game, thẻ cào, đổi thẻ, ví, bảo h… |
| 2026-11-25 18:39:46 | [restruct/silverstripe-seo](https://www.nuget.org/packages/restruct%2Fsilverstripe-seo) | 0.1.0 | Restruct | SEO essentials for Silverstripe CMS 6: meta title, description fallback, robots… |
| 2026-11-25 18:55:17 | [shreifelagamy/laravel-authentica](https://www.nuget.org/packages/shreifelagamy%2Flaravel-authentica) | v0.1.1 | Shreif Ashraf | Laravel client, facade and notification channel for Authentica: SMS, and one-ti… |
| 2026-11-25 19:06:16 | [weirdo/laravel-workflow](https://www.nuget.org/packages/weirdo%2Flaravel-workflow) | v1.0.0 | Angel Hidalgo | Integerate Symfony Workflow component into Laravel. |
| 2026-11-25 19:15:38 | [binable/address-kit](https://www.nuget.org/packages/binable%2Faddress-kit) | 0.0.1 | Tim Lochmüller | Symfony bundle for address handling: validation, normalization and permutation… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
