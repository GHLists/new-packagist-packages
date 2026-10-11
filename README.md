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

## Latest list — 2026-10-11 20:18 UTC

New packages created between 2026-10-11 19:20 UTC and 2026-10-11 20:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T20-18-45-037033Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 19:20:20 | [padosoft/askmydocs-connector-zendesk](https://www.nuget.org/packages/padosoft%2Faskmydocs-connector-zendesk) | v1.0.0 | Padosoft | Zendesk connector for AskMyDocs: resumable ingestion of Support tickets, commen… |
| 2026-10-11 19:42:35 | [mohannadelemary/laravel-console-streams](https://www.nuget.org/packages/mohannadelemary%2Flaravel-console-streams) | v0.1.0 | Mohannad Elemary | Opt-in Artisan trait that keeps machine data on STDOUT and sends console compon… |
| 2026-10-11 19:43:28 | [t3s/vars](https://www.nuget.org/packages/t3s%2Fvars) | v1.0.0 | Helmut Hackbarth | Global variables for TYPO3 v14: maintain company, address, phone, email etc. on… |
| 2026-10-11 20:00:55 | [trollbus/symfony-messenger-bridge](https://www.nuget.org/packages/trollbus%2Fsymfony-messenger-bridge) | 0.1.0 | Kenny1911 |  |
| 2026-10-11 20:03:41 | [antevemus/aspecification](https://www.nuget.org/packages/antevemus%2Faspecification) | v1.13.0 | Heliton Junior - CTO @ Anteve… | Enterprise Specification Pattern Framework for PHP 8.2+ (DDD, Notification Patt… |
| 2026-10-11 20:06:58 | [zenky/exceptions](https://www.nuget.org/packages/zenky%2Fexceptions) | v2.1.0 | tzurbaev | Exceptions Package |
| 2026-10-11 20:10:29 | [zenky/infrastructure](https://www.nuget.org/packages/zenky%2Finfrastructure) | v6.0.0 | tzurbaev | Zenky Infrastructure |
| 2026-10-11 20:12:26 | [zenky/loyalty-microservice](https://www.nuget.org/packages/zenky%2Floyalty-microservice) | v4.0.0 | tzurbaev | Loyalty Microservice Package |
| 2026-10-11 20:14:34 | [zenky/model-settings](https://www.nuget.org/packages/zenky%2Fmodel-settings) | v1.0.0 | tzurbaev | Zenky Model Settings |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
