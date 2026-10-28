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

## Latest list — 2026-10-28 14:20 UTC

New packages created between 2026-10-28 13:19 UTC and 2026-10-28 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T14-20-53-840773Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 13:25:47 | [creacoon/laravel-dashboard-dutch-trains](https://www.nuget.org/packages/creacoon%2Flaravel-dashboard-dutch-trains) | v1.1.0 |  | Fetch upcoming departures for the live departure board tile |
| 2026-10-28 13:28:03 | [phpwarden/phpwarden](https://www.nuget.org/packages/phpwarden%2Fphpwarden) | v1.0.0 | phpwarden | PHP exposure & exploitation guard — scan PHP engine, Composer deps & WordPress… |
| 2026-10-28 13:31:21 | [brbunny/brlayer](https://www.nuget.org/packages/brbunny%2Fbrlayer) | v1.0.0 | Kevin Siqueira; Robson V. Lei… | Camada de persistência com PDO e prepared statements: model Active Record com C… |
| 2026-10-28 13:43:21 | [mojahed/aiapi](https://www.nuget.org/packages/mojahed%2Faiapi) | 1.0.3 | Md. Mojahedul Islam | A Laravel AI API package — connect to any LLM provider with a clean, unified in… |
| 2026-10-28 13:44:00 | [cabuz/laravel-stedi](https://www.nuget.org/packages/cabuz%2Flaravel-stedi) | v1.1.2 | Florin Cabuz | Laravel SDK for the Stedi healthcare APIs: real-time eligibility checks, claims… |
| 2026-10-28 14:00:27 | [excelle-insights/sms](https://www.nuget.org/packages/excelle-insights%2Fsms) | v1.0.0 | Excelle Insights | Multi-provider SMS package for Excelle applications |
| 2026-10-28 14:00:53 | [nth-root/phpstan-security](https://www.nuget.org/packages/nth-root%2Fphpstan-security) | v0.1.0 |  | A PHPStan extension that checks your code for security vulnerabilities |
| 2026-10-28 14:15:36 | [magepow/custompdffont](https://www.nuget.org/packages/magepow%2Fcustompdffont) | 1.0.0 | Magepow | Customize PDF invoice fonts. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
