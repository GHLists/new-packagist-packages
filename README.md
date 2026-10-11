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

## Latest list — 2026-10-11 14:19 UTC

New packages created between 2026-10-11 13:21 UTC and 2026-10-11 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T14-19-05-398903Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 13:21:53 | [malzariey/filament-ga4-analytics](https://www.nuget.org/packages/malzariey%2Ffilament-ga4-analytics) | v1.0.1 | Majid Al-Zariey | A Google Analytics 4 reports page for Filament panels: live visitors, KPIs, fun… |
| 2026-10-11 13:59:49 | [snipershady/queue-bridge](https://www.nuget.org/packages/snipershady%2Fqueue-bridge) | v1.0.0 | snipershady | Backend-agnostic PHP 8.3+ message queue: one typed API for Redis Streams and Ra… |
| 2026-10-11 14:04:48 | [small/swoole-events](https://www.nuget.org/packages/small%2Fswoole-events) | 2.0.0 |  | Native Swoole event bus with fluent pipelines, coroutine synchronization and Sm… |
| 2026-10-11 14:09:25 | [antevemus/aspecification](https://www.nuget.org/packages/antevemus%2Faspecification) | v1.12.0 | Heliton Junior - CTO @ Anteve… | Enterprise Specification Pattern Framework for PHP 8.2+ (DDD, Notification Patt… |
| 2026-10-11 14:12:28 | [selldatatoai/selldatatoai](https://www.nuget.org/packages/selldatatoai%2Fselldatatoai) | v1.0.0 | Alpha Quantum | PHP client for the Data Asset Score API from selldatatoai.com: score company do… |
| 2026-10-11 14:18:27 | [ripplesanalytics/ripples-php](https://www.nuget.org/packages/ripplesanalytics%2Fripples-php) | v0.1.10 | Ripples Metrics | Official PHP SDK for Ripples Metrics (ripples.sh): server-side event tracking |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
