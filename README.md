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

## Latest list — 2026-10-26 15:21 UTC

New packages created between 2026-10-26 14:20 UTC and 2026-10-26 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T15-21-57-426989Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 14:39:08 | [alokhindev/ad-hp-updates](https://www.nuget.org/packages/alokhindev%2Fad-hp-updates) | 1.0.0 |  | Updates manager for alokhin.dev products for HivePress. |
| 2026-10-26 14:41:36 | [dskripchenko/process-engine](https://www.nuget.org/packages/dskripchenko%2Fprocess-engine) | v1.0.0 | Denis Skripchenko | Framework-agnostic engine for long-running processes: hierarchical state machin… |
| 2026-10-26 14:43:01 | [dskripchenko/laravel-process-engine](https://www.nuget.org/packages/dskripchenko%2Flaravel-process-engine) | v1.0.1 | Denis Skripchenko | Laravel bridge for dskripchenko/process-engine: database store, queue workers,… |
| 2026-10-26 14:43:43 | [dskripchenko/laravel-admin-process](https://www.nuget.org/packages/dskripchenko%2Flaravel-admin-process) | v1.0.0 | Denis Skripchenko | Process-engine screens for dskripchenko/laravel-admin: instances, live flow dia… |
| 2026-10-26 14:43:50 | [psbits/frontend-users](https://www.nuget.org/packages/psbits%2Ffrontend-users) | 0.1.0-alpha | Daniel Ablass | a versatile set of tools and objects for dealing with frontend-users |
| 2026-10-26 14:50:32 | [dwivedianuj9118/laravel-ai-sarvam](https://www.nuget.org/packages/dwivedianuj9118%2Flaravel-ai-sarvam) | v0.1.0 | Anuj Dwivedi | Sarvam AI provider for the Laravel AI SDK: chat, text-to-speech and speech-to-t… |
| 2026-10-26 15:15:54 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v0.9.0 |  | The skeleton application for the Laravel framework. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
