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

## Latest list — 2026-11-25 09:19 UTC

New packages created between 2026-11-25 08:19 UTC and 2026-11-25 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T09-19-35-154419Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 08:20:54 | [andrekelling/kirby-anchor-field](https://www.nuget.org/packages/andrekelling%2Fkirby-anchor-field) | 1.0.0 | André Kelling | Add anchor type field for Kirby Panel |
| 2026-11-25 08:24:20 | [replayd/laravel](https://www.nuget.org/packages/replayd%2Flaravel) | v0.1.1 |  | Send Laravel backend errors and performance issues (N+1 queries, slow queries)… |
| 2026-11-25 08:41:42 | [klsoft/yii3-doctrine-app](https://www.nuget.org/packages/klsoft%2Fyii3-doctrine-app) | 1.0.0 |  | A Yii 3 web application template that supports the Doctrine ORM |
| 2026-11-25 08:45:17 | [klsoft/yii3-cms](https://www.nuget.org/packages/klsoft%2Fyii3-cms) | 1.0.0 |  | A content management system based on the Yii 3 framework and uses the Doctrine… |
| 2026-11-25 08:55:41 | [kreativsoehne/contao-request-token-bundle](https://www.nuget.org/packages/kreativsoehne%2Fcontao-request-token-bundle) | v1.0.0 | Kreativ&Söhne GmbH | Keeps Contao 4.13 forms working behind a consent tool: when a page went out wit… |
| 2026-11-25 08:55:53 | [hirasso/phpstan-illuminate-collections](https://www.nuget.org/packages/hirasso%2Fphpstan-illuminate-collections) | v1.0.0 | Rasso Hilber | PHPStan narrowing for filter()/reject()/where() on illuminate/collections, with… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
