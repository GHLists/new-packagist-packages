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

## Latest list — 2026-10-19 11:22 UTC

New packages created between 2026-10-19 10:23 UTC and 2026-10-19 11:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T11-22-04-711278Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 10:33:46 | [jellyhaus/migrations](https://www.nuget.org/packages/jellyhaus%2Fmigrations) | 2026.10.1 | Jason Millis | Simple database migrations |
| 2026-10-19 10:40:40 | [nocwise/laravel-client](https://www.nuget.org/packages/nocwise%2Flaravel-client) | v0.4.3 | Nocwise | Cliente oficial de Nocwise para Laravel: captura logs y excepciones y las envía… |
| 2026-10-19 11:04:45 | [rolog/magma-app](https://www.nuget.org/packages/rolog%2Fmagma-app) | v0.1.1 |  |  |
| 2026-10-19 11:06:51 | [ufo-tech/mcp-bundle](https://www.nuget.org/packages/ufo-tech%2Fmcp-bundle) | 1.0.0 | Alex Maistrenko | Expose UFO JSON-RPC services as MCP tools for AI agents. |
| 2026-10-19 11:17:30 | [stefanak-michal/grafeo-php](https://www.nuget.org/packages/stefanak-michal%2Fgrafeo-php) | v0.5.44-p1 | Michal Stefanak | FFI implementation to run Grafeo embedded in PHP |
| 2026-10-19 11:20:43 | [tencentcloud/workbuddyenterprise](https://www.nuget.org/packages/tencentcloud%2Fworkbuddyenterprise) | 3.0.1683 | tencentcloudapi | TencentCloudApi php sdk workbuddyenterprise |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
