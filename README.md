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

## Latest list — 2026-11-13 15:19 UTC

New packages created between 2026-11-13 14:22 UTC and 2026-11-13 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T15-19-11-859478Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 14:23:47 | [deokonai/larabase-core](https://www.nuget.org/packages/deokonai%2Flarabase-core) | v1.0.0 |  | Commande de setup et création de modules Larabase. |
| 2026-11-13 14:23:48 | [deokonai/larabase-filament](https://www.nuget.org/packages/deokonai%2Flarabase-filament) | v1.0.0 |  | Réglages Filament partagés par Larabase. Une application peut les surcharger. |
| 2026-11-13 14:29:00 | [tornado-engine/nav](https://www.nuget.org/packages/tornado-engine%2Fnav) | v0.3.0 |  | Tornado Engine core-module: the site's navigation menu. Other modules add their… |
| 2026-11-13 14:30:39 | [net-os/laravel-payments](https://www.nuget.org/packages/net-os%2Flaravel-payments) | v0.1.0 |  | PSP-agnostic payments, invoices and discount codes for Laravel |
| 2026-11-13 14:32:38 | [hernandotech/librenms-service-health](https://www.nuget.org/packages/hernandotech%2Flibrenms-service-health) | v0.1.0 |  | Proof of concept native LibreNMS Service Health dashboard widget |
| 2026-11-13 14:33:36 | [deokonai/larabase](https://www.nuget.org/packages/deokonai%2Flarabase) | v1.0.1 |  | Squelette Laravel neutre. Les modules partagés sont des packages deokonai/larab… |
| 2026-11-13 14:51:56 | [tornado-engine/docs](https://www.nuget.org/packages/tornado-engine%2Fdocs) | v0.2.0 |  | Tornado Engine core-module: documentation pages in Administration. Other module… |
| 2026-11-13 14:59:19 | [aiobale/aiobale-php](https://www.nuget.org/packages/aiobale%2Faiobale-php) | v1.0.1 | Abolfazl | Asynchronous PHP client for the Bale messaging API |
| 2026-11-13 15:06:37 | [paulocastellano/laravel-database-backup](https://www.nuget.org/packages/paulocastellano%2Flaravel-database-backup) | v1.0.0 | Paulo Castellano | Back up your Laravel database (PostgreSQL, MySQL, MariaDB) to a private S3-comp… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
