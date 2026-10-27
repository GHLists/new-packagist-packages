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

## Latest list — 2026-10-27 02:20 UTC

New packages created between 2026-10-27 01:18 UTC and 2026-10-27 02:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T02-20-21-62826Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 01:41:31 | [spoolbit/spoolbit-php](https://www.nuget.org/packages/spoolbit%2Fspoolbit-php) | v0.0.1 |  | Official PHP SDK for the Spoolbit cloud printing API (coming soon). |
| 2026-10-27 01:45:45 | [normann/silverstripe-used-on](https://www.nuget.org/packages/normann%2Fsilverstripe-used-on) | 1.0.0 | Normann Lou | Improves the "Used on" tab of files in Silverstripe CMS: working CMS edit links… |
| 2026-10-27 01:58:24 | [rootstuff/laravel-ops-mcp](https://www.nuget.org/packages/rootstuff%2Flaravel-ops-mcp) | v0.1.1 | Adam Balée | A read-only MCP server inside your Laravel app so your agent can read the logs,… |
| 2026-10-27 02:10:15 | [zzktz/laravel-health](https://www.nuget.org/packages/zzktz%2Flaravel-health) | v1.0.0 |  | 为 Laravel 8 提供符合统一契约的存活与就绪健康检查接口。 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
