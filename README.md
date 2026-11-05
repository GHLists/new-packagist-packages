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

## Latest list — 2026-11-05 19:20 UTC

New packages created between 2026-11-05 18:20 UTC and 2026-11-05 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T19-20-33-507388Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 18:24:44 | [shaungbhone/shopper-po](https://www.nuget.org/packages/shaungbhone%2Fshopper-po) | v1.0.0 |  | Purchase orders and auditable receiving for Laravel Shopper 2.12. |
| 2026-11-05 18:33:53 | [wfeller/laravel-schedule-monitor-healthchecksio](https://www.nuget.org/packages/wfeller%2Flaravel-schedule-monitor-healthchecksio) | 1.0.0 |  | Send spatie/laravel-schedule-monitor pings to Healthchecks.io instead of Oh Dea… |
| 2026-11-05 18:38:56 | [pijler/impersonation](https://www.nuget.org/packages/pijler%2Fimpersonation) | v0.1.0 | João Pedro Lopes | Secure user impersonation for Laravel, with per-request authorization, audit ev… |
| 2026-11-05 18:40:36 | [pijler/actions](https://www.nuget.org/packages/pijler%2Factions) | v0.1.0 | João Pedro Lopes | Typed, testable, and queueable actions for Laravel, with workflows to orchestra… |
| 2026-11-05 18:48:47 | [exeque/lumberjack-agent](https://www.nuget.org/packages/exeque%2Flumberjack-agent) | v0.1.0 | Morten Harders | The local agent that takes batches from your apps and sends them on to Lumberja… |
| 2026-11-05 18:51:54 | [mkerstner/aurora](https://www.nuget.org/packages/mkerstner%2Faurora) | 1.0.1 | Matthias Kerstner | A modern, mobile-first refresh of Roundcube's Elastic skin: a persistent phone… |
| 2026-11-05 18:59:11 | [rgusseinov/arc-skeleton](https://www.nuget.org/packages/rgusseinov%2Farc-skeleton) | v0.1.2 |  | Application skeleton for the Arc framework |
| 2026-11-05 18:59:52 | [uzapoint/digitax-client](https://www.nuget.org/packages/uzapoint%2Fdigitax-client) | v1.0.0 | Caleb Chege | DigiTax (KRA eTIMS) v2 API client for Uzapoint Laravel microservices |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
