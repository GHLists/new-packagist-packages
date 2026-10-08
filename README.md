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

## Latest list — 2026-10-08 08:22 UTC

New packages created between 2026-10-08 07:19 UTC and 2026-10-08 08:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T08-22-57-972074Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 07:21:20 | [kybdev/laravel-redis-read-cache](https://www.nuget.org/packages/kybdev%2Flaravel-redis-read-cache) | v1.0.1 |  | Transparent Redis read-through caching for Laravel applications. |
| 2026-10-08 07:32:09 | [evilmartians/lefthook](https://www.nuget.org/packages/evilmartians%2Flefthook) | v2.2.0 | Evil Martians | Lefthook Git hooks manager, installable via Composer. |
| 2026-10-08 07:38:05 | [patrickfischer/monolog-slack-safe](https://www.nuget.org/packages/patrickfischer%2Fmonolog-slack-safe) | 1.0.4 | Patrick Fischer | A non fatal version of the Monolog SlackWebhookHandler |
| 2026-10-08 07:40:25 | [nguoingulanh/cashier-connect](https://www.nuget.org/packages/nguoingulanh%2Fcashier-connect) | v0.1.0 |  |  |
| 2026-10-08 07:59:55 | [b4moss/crudian](https://www.nuget.org/packages/b4moss%2Fcrudian) | v0.12.0 | Kohki SHIKATA | CRUD abstraction for DDD repositories (PDO + libSQL preview) |
| 2026-10-08 08:04:13 | [wpstarter/o-canvas](https://www.nuget.org/packages/wpstarter%2Fo-canvas) | v2.0 |  | Code Generators for Laravel Applications and Packages |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
