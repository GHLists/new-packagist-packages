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

## Latest list — 2026-10-10 23:20 UTC

New packages created between 2026-10-10 22:21 UTC and 2026-10-10 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T23-20-16-536038Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 22:29:44 | [antevemus/aspecification](https://www.nuget.org/packages/antevemus%2Faspecification) | v1.8.0 | Heliton Junior - CTO @ Anteve… | Enterprise Specification Pattern Framework for PHP 8.2+ (DDD, Notification Patt… |
| 2026-10-10 22:29:55 | [joust/joust](https://www.nuget.org/packages/joust%2Fjoust) | 0.1.0 | Woody Gilk | Just another JSON API kit |
| 2026-10-10 22:31:53 | [tueen/database](https://www.nuget.org/packages/tueen%2Fdatabase) | v1.0.0-alpha.1 | Tueen Ecosystem Team | The zero-config, high-throughput relational database engine engineered for Tele… |
| 2026-10-10 22:45:58 | [quadcompanies/quadpayment](https://www.nuget.org/packages/quadcompanies%2Fquadpayment) | v0.1.0 |  | Tokenized Payload (v2) card payments for Laravel with built-in card-testing def… |
| 2026-10-10 22:52:56 | [jeffersongoncalves/laravel-telegram-logger](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-telegram-logger) | 1.0.0 | Jefferson Gonçalves | Send Laravel logs to a Telegram chat with deduplication, configurable error gro… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
