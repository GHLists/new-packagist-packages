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

## Latest list — 2026-10-06 18:20 UTC

New packages created between 2026-10-06 17:21 UTC and 2026-10-06 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T18-20-58-249521Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 17:32:22 | [jairojeffersont/easy-api](https://www.nuget.org/packages/jairojeffersont%2Feasy-api) | v1.0.0 | Jairo Jefferson Teixeira Dos… | Aplicação PHP de exemplo de uma API com autenticação |
| 2026-10-06 17:32:44 | [onetracepro/onetrace-php](https://www.nuget.org/packages/onetracepro%2Fonetrace-php) | v1.0.0 |  | PHP client for the OneTrace.pro customer data platform API: events, profiles, p… |
| 2026-10-06 17:54:55 | [fosseva/laravel-web-mcp](https://www.nuget.org/packages/fosseva%2Flaravel-web-mcp) | v0.1.0-alpha.1 |  | Expose Laravel AI SDK tools in Blade through browser-native WebMCP. |
| 2026-10-06 17:59:37 | [troccoli/laravel-queue-monitor-flux](https://www.nuget.org/packages/troccoli%2Flaravel-queue-monitor-flux) | v0.0.1 | Giulio Troccoli-Allard | This is my package laravel-queue-monitor-flux |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
