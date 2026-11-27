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

## Latest list — 2026-11-27 21:22 UTC

New packages created between 2026-11-27 20:19 UTC and 2026-11-27 21:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T21-22-06-425219Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 20:36:58 | [krystalcode/api-session](https://www.nuget.org/packages/krystalcode%2Fapi-session) | 1.0.0 | krystalcode | Provides session management functionality for API clients including requesting,… |
| 2026-11-27 20:51:36 | [termstrap/termstrap](https://www.nuget.org/packages/termstrap%2Ftermstrap) | v0.1.0 |  | Native PHP port of Termstrap terminal rendering engine |
| 2026-11-27 20:54:54 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.57.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-27 21:00:17 | [siberfx/ploi-laravel](https://www.nuget.org/packages/siberfx%2Fploi-laravel) | 1.0.1 | Selim Görmüş | The Ploi.io PHP SDK, made for Laravel: config-driven multi-account clients, Lar… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
