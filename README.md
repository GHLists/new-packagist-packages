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

## Latest list — 2026-11-23 19:20 UTC

New packages created between 2026-11-23 18:20 UTC and 2026-11-23 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T19-20-41-713593Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 18:27:07 | [wenmark/wpcodebox2-cli](https://www.nuget.org/packages/wenmark%2Fwpcodebox2-cli) | v1.0.1 | Michael Wender | WP-CLI commands for managing WPCodeBox 2 snippets and folders without the brows… |
| 2026-11-23 18:27:22 | [cboxdk/laravel-signals-client](https://www.nuget.org/packages/cboxdk%2Flaravel-signals-client) | v0.1.0 |  | Typed transport for Cbox Signals |
| 2026-11-23 18:29:08 | [mockcard/laravel](https://www.nuget.org/packages/mockcard%2Flaravel) | v2.0.0 | Arixeva Labs | MockCard for Laravel: probe-guard middleware, chaos runs from Artisan and Pest/… |
| 2026-11-23 18:29:54 | [mockcard/symfony-bundle](https://www.nuget.org/packages/mockcard%2Fsymfony-bundle) | v2.0.0 | Arixeva Labs | MockCard for Symfony: probe guard for webhook routes, DI configuration and a ch… |
| 2026-11-23 19:06:28 | [rasuvaeff/mcp](https://www.nuget.org/packages/rasuvaeff%2Fmcp) | v0.1.0 | Victor Razuvaev | Framework-neutral MCP server runtime on the official mcp/sdk: attribute tools,… |
| 2026-11-23 19:06:42 | [adachsoft/calendar](https://www.nuget.org/packages/adachsoft%2Fcalendar) | v0.1.1 | Arkadiusz Adach | Calendar logic for adachsoft/calendar-contracts: calendar service with access p… |
| 2026-11-23 19:11:36 | [fisharebest/database](https://www.nuget.org/packages/fisharebest%2Fdatabase) | 0.9.0 | Greg Roach | Database abstraction layer - query builder and schema builder |
| 2026-11-23 19:12:47 | [rasuvaeff/mcp-openapi](https://www.nuget.org/packages/rasuvaeff%2Fmcp-openapi) | v0.1.0 | Victor Razuvaev | Serve allow-listed OpenAPI operations as MCP tools: PSR-18 or in-process PSR-15… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
