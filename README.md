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

## Latest list — 2026-11-23 14:20 UTC

New packages created between 2026-11-23 13:20 UTC and 2026-11-23 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T14-20-04-721462Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 13:25:45 | [hk100/tcp-socket](https://www.nuget.org/packages/hk100%2Ftcp-socket) | v1.0.0 | hk100 | Multi-protocol (TCP / WebSocket / MQTT) communication package for Hyperf and La… |
| 2026-11-23 13:34:13 | [rashed50702/laravel-bangla-pdf](https://www.nuget.org/packages/rashed50702%2Flaravel-bangla-pdf) | v1.0.0 | Md. Rashedul Hasan | Generate Bangla (Bengali) + English PDFs in Laravel with mPDF: correct conjunct… |
| 2026-11-23 13:39:10 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.47.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-23 13:48:38 | [infrangible/phpstan-magento](https://www.nuget.org/packages/infrangible%2Fphpstan-magento) | 1.0.0 | Andreas Knollmann | PHPStan rules and configuration for Magento 2 modules: the checks of PhpStorm t… |
| 2026-11-23 13:57:43 | [psbits/contact-book](https://www.nuget.org/packages/psbits%2Fcontact-book) | 0.1.0-alpha | Daniel Ablass | Comprehensive contact management |
| 2026-11-23 14:10:57 | [datacircle/php-mcp-tools](https://www.nuget.org/packages/datacircle%2Fphp-mcp-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. This package adds four tools to an MCP server made with… |
| 2026-11-23 14:11:06 | [ideal-postcodes/laravel](https://www.nuget.org/packages/ideal-postcodes%2Flaravel) | v0.1.0 | Ideal Postcodes | Laravel package for the Ideal Postcodes PHP SDK: set your API key in .env, then… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
