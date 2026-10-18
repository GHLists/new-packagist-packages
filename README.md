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

## Latest list — 2026-10-18 20:19 UTC

New packages created between 2026-10-18 19:19 UTC and 2026-10-18 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T20-19-44-812194Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 19:32:12 | [cecil/theme-pele](https://www.nuget.org/packages/cecil%2Ftheme-pele) | 1.0.0 |  | Cecil component theme Pele |
| 2026-10-18 19:33:27 | [abdelhmed/chimera](https://www.nuget.org/packages/abdelhmed%2Fchimera) | v1.0.0 | abdelhmed | A self-mutating AI-powered engine for Laravel applications. |
| 2026-10-18 19:48:18 | [siberfx/message-bus](https://www.nuget.org/packages/siberfx%2Fmessage-bus) | v0.1.0 | Siberfx | A Symfony Messenger inspired message bus for Laravel: buses, middleware, transp… |
| 2026-10-18 19:51:18 | [hamada-emam-tech/esign-sadq](https://www.nuget.org/packages/hamada-emam-tech%2Fesign-sadq) | v0.2.0 |  | SADQ (sadq.sa) driver for hamada-emam-tech/esign: Saudi e-signature envelopes w… |
| 2026-10-18 19:57:05 | [simpledatalogs/laravel](https://www.nuget.org/packages/simpledatalogs%2Flaravel) | 0.2.0 | XKD Labs | Send events, Eloquent model changes, auth events and Laravel log channels to si… |
| 2026-10-18 20:07:59 | [edalzell/statamic-features](https://www.nuget.org/packages/edalzell%2Fstatamic-features) | v1.0.0 | Erin Dalzell | Self-contained feature modules for Statamic, built on edalzell/laravel-features |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
