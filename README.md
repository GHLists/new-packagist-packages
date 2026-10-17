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

## Latest list — 2026-10-17 14:21 UTC

New packages created between 2026-10-17 13:20 UTC and 2026-10-17 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T14-21-15-798809Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 13:35:04 | [memora/laravel-antispam](https://www.nuget.org/packages/memora%2Flaravel-antispam) | v1.1.0 | MEMORA solutions | Invisible anti-spam middleware for Laravel - honeypot, time trap, JS token, rat… |
| 2026-10-17 13:38:49 | [muehleis/laravel-talario](https://www.nuget.org/packages/muehleis%2Flaravel-talario) | v1.0.0 |  | Laravel mail transport for the Talario sending API |
| 2026-10-17 14:00:30 | [pieceofcake2/storybook](https://www.nuget.org/packages/pieceofcake2%2Fstorybook) | v1.0.0 |  | Storybook for CakePHP 2 (development only): render Elements in Storybook (Vite)… |
| 2026-10-17 14:08:55 | [dewanlab/laravel-zkteco-adms-core](https://www.nuget.org/packages/dewanlab%2Flaravel-zkteco-adms-core) | v1.0.0 | Abdullah Dewan | Comprehensive ZKTeco ADMS (Push Protocol) Core implementation for Laravel, supp… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
