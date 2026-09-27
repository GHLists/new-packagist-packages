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

## Latest list — 2026-09-27 19:20 UTC

New packages created between 2026-09-27 18:20 UTC and 2026-09-27 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-27T19-20-24-025907Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-27 18:53:58 | [cboxdk/laravel-telemetry-insights](https://www.nuget.org/packages/cboxdk%2Flaravel-telemetry-insights) | v1.0.0 | Sylvester Damgaard | Stateful insights on top of cboxdk/laravel-telemetry-ui: deduplicated issues, i… |
| 2026-09-27 18:54:37 | [minstrel/api-client](https://www.nuget.org/packages/minstrel%2Fapi-client) | v1.0.0 |  | PHP client for the Minstrel public API (v1), generated from docs/openapi/v1.jso… |
| 2026-09-27 19:12:26 | [carloscardoso05/pptx-template](https://www.nuget.org/packages/carloscardoso05%2Fpptx-template) | v1.0.0 | Carlos Cardoso | Biblioteca PHP para manipulação de templates PPTX com substituição de tags por… |
| 2026-09-27 19:14:27 | [pietervanleuven/laravel-mcp-discovery](https://www.nuget.org/packages/pietervanleuven%2Flaravel-mcp-discovery) | v0.1.0 | Pieter Van Leuven | Make your laravel/mcp servers discoverable by AI agents: server cards, llms.txt… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
