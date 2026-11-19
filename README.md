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

## Latest list — 2026-11-19 21:18 UTC

New packages created between 2026-11-19 20:19 UTC and 2026-11-19 21:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T21-18-58-94903Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 20:35:19 | [tomvondracek/bolt-altcha](https://www.nuget.org/packages/tomvondracek%2Fbolt-altcha) | v1.0.1 | Tomáš Vondráček | Bolt CMS extension that protects forms from bots with ALTCHA, a self-hosted pro… |
| 2026-11-19 20:35:45 | [ua0leg/yii2-mcp](https://www.nuget.org/packages/ua0leg%2Fyii2-mcp) | v1.0.0 | Oleg | Yii2 MCP server module: Streamable HTTP endpoint, optional OAuth 2.1 for Claude… |
| 2026-11-19 20:36:54 | [speedyspec/cli-wordpress-org](https://www.nuget.org/packages/speedyspec%2Fcli-wordpress-org) | v0.1.1 |  | The speedyspec CLI source plugin for wordpress.org's plugin and theme directori… |
| 2026-11-19 20:49:27 | [narek/sharp-php](https://www.nuget.org/packages/narek%2Fsharp-php) | v0.1.1 | Narek | SharpPHP: a C#-like language that compiles to modern PHP. |
| 2026-11-19 21:00:51 | [voharaa/privatbank-autoclient](https://www.nuget.org/packages/voharaa%2Fprivatbank-autoclient) | v0.1.0 | Vohar Andrii | Unofficial PHP client for the PrivatBank Autoclient API (Privat24 for Business)… |
| 2026-11-19 21:13:45 | [ayewar/strata](https://www.nuget.org/packages/ayewar%2Fstrata) | v1.0.0 | zerak jamil | High-performance hybrid search engine for Laravel (<1ms HTTP cycle, 1.5M+ recor… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
