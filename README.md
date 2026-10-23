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

## Latest list — 2026-10-23 13:20 UTC

New packages created between 2026-10-23 12:18 UTC and 2026-10-23 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T13-20-22-285451Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 12:27:01 | [prolificjones/elite-league-client](https://www.nuget.org/packages/prolificjones%2Felite-league-client) | 1.0.0-rc.1 | Lee Jones | Elite League API SDK in PHP |
| 2026-10-23 12:31:30 | [efabrica/phoenix-core](https://www.nuget.org/packages/efabrica%2Fphoenix-core) | 4.0.0 |  | Database Migrations for PHP |
| 2026-10-23 12:46:38 | [cmdimu/db-sync-package](https://www.nuget.org/packages/cmdimu%2Fdb-sync-package) | v1.1.0 | cmdimu | Database Sync Package for Laravel, CodeIgniter 4, and CodeIgniter 3 |
| 2026-10-23 12:49:17 | [rohama/koin-sep](https://www.nuget.org/packages/rohama%2Fkoin-sep) | 2.2.1 | Rohama | Koin — SEP (Saman) gateway driver (REST OnlinePG API) |
| 2026-10-23 12:49:51 | [djouamaah/laravel-algeria-sms](https://www.nuget.org/packages/djouamaah%2Flaravel-algeria-sms) | v1.0.0 | Djouamaa | SMS for Laravel through Algerian providers: OTP codes, transactional and market… |
| 2026-10-23 13:06:56 | [prolificjones/champions-hockey-league-client](https://www.nuget.org/packages/prolificjones%2Fchampions-hockey-league-client) | 1.0.0-rc.2 | Lee Jones | Champions Hockey League API SDK in PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
