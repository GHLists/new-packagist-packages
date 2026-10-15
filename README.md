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

## Latest list — 2026-10-15 19:23 UTC

New packages created between 2026-10-15 18:20 UTC and 2026-10-15 19:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T19-23-10-067669Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 18:21:59 | [yii2-extensions/bootstrap6](https://www.nuget.org/packages/yii2-extensions%2Fbootstrap6) | 0.1.0 | Wilmer Arambula | Bootstrap 6 widgets, forms, and asset bundles for Yii2. |
| 2026-10-15 18:44:17 | [nacew/utestme-laravel](https://www.nuget.org/packages/nacew%2Futestme-laravel) | v0.1.0 |  | uTestMe server errors for Laravel: unhandled exceptions with their request, bre… |
| 2026-10-15 18:51:07 | [proceda/proceda](https://www.nuget.org/packages/proceda%2Fproceda) | v1.0.0 | Gabriel dos Anjos | Biblioteca PHP para layouts PROCEDA (NOTFIS, OCOREN, CONEMB e DOCCOB) |
| 2026-10-15 18:58:11 | [integrad/laravel-database-backup](https://www.nuget.org/packages/integrad%2Flaravel-database-backup) | v0.1.0 | Integrad | Database backup and recovery for Laravel, with a protected dashboard. |
| 2026-10-15 19:00:25 | [everysize/checkout-gambio](https://www.nuget.org/packages/everysize%2Fcheckout-gambio) | 1.0.1 | everysize GmbH | everysize Checkout – Modul für Gambio GX26 |
| 2026-10-15 19:03:13 | [rasuvaeff/context-db](https://www.nuget.org/packages/rasuvaeff%2Fcontext-db) | v0.1.0 | Victor Razuvaev | Database-side statement timeouts from a rasuvaeff/context budget for MySQL, Mar… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
