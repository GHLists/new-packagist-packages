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

## Latest list — 2026-09-29 01:22 UTC

New packages created between 2026-09-29 00:20 UTC and 2026-09-29 01:22 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T01-22-35-29897Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 00:24:27 | [dirthara/queue](https://www.nuget.org/packages/dirthara%2Fqueue) | 0.1.0 | Dirthara | Transport-neutral message queues and workers for PHP and the Dirthara framework |
| 2026-09-29 00:26:07 | [senddart/senddart](https://www.nuget.org/packages/senddart%2Fsenddart) | v1.0.0 |  | Official SendDart PHP SDK — send transactional and marketing email from your ow… |
| 2026-09-29 00:29:00 | [petar-spasic/laravel-kanban](https://www.nuget.org/packages/petar-spasic%2Flaravel-kanban) | v0.1.2 | Petar Spasic | Git-backed kanban board, worktree workflow and Claude Code hooks for Laravel pr… |
| 2026-09-29 00:29:07 | [petar-spasic/laravel-house](https://www.nuget.org/packages/petar-spasic%2Flaravel-house) | v0.1.2 | Petar Spasic | House skills for Laravel projects (project setup, Docker hosting, laravel-kanba… |
| 2026-09-29 00:31:39 | [monkeyscloud/monkeyslegion-inertia](https://www.nuget.org/packages/monkeyscloud%2Fmonkeyslegion-inertia) | 1.0.0 |  | Inertia.js server adapter for MonKeysLegion — bridges PHP controllers with Reac… |
| 2026-09-29 00:39:16 | [automattic/jetpack-sharing-likes](https://www.nuget.org/packages/automattic%2Fjetpack-sharing-likes) | v0.1.0 |  | Sharing buttons and Like buttons for your posts. |
| 2026-09-29 00:41:03 | [automattic/jetpack-ads](https://www.nuget.org/packages/automattic%2Fjetpack-ads) | v0.1.0 |  | WordAds: the Ads section and widgets of the Premium Analytics dashboard. |
| 2026-09-29 01:01:12 | [nnaemekanweke/logwatch](https://www.nuget.org/packages/nnaemekanweke%2Flogwatch) | v1.0.0 |  | Push your Laravel app's logs to LogWatch as a standard log channel. |
| 2026-09-29 01:02:14 | [monkeyscloud/monkeyslegion-testing](https://www.nuget.org/packages/monkeyscloud%2Fmonkeyslegion-testing) | 1.0.0 |  | Testing toolkit for MonKeysLegion — HTTP testing DSL, database traits, fake sub… |
| 2026-09-29 01:02:40 | [monkeyscloud/monkeyslegion-vite](https://www.nuget.org/packages/monkeyscloud%2Fmonkeyslegion-vite) | 1.0.0 |  | Vite asset pipeline integration for MonKeysLegion — manifest parser, @vite dire… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
