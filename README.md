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

## Latest list — 2026-11-25 02:20 UTC

New packages created between 2026-11-25 01:21 UTC and 2026-11-25 02:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T02-20-39-334111Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 01:30:02 | [datacircle/opgg-laravel-mcp-tools](https://www.nuget.org/packages/datacircle%2Fopgg-laravel-mcp-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. Four tools for OP.GG's Laravel MCP Server call Datacirc… |
| 2026-11-25 01:50:02 | [vcorexplatform/core](https://www.nuget.org/packages/vcorexplatform%2Fcore) | v1.0.0 |  | Starter MVC core with RedBeanPHP |
| 2026-11-25 01:50:02 | [vcorexplatform/http-client](https://www.nuget.org/packages/vcorexplatform%2Fhttp-client) | v1.0.0 |  | Filtered outbound HTTP client for Starter |
| 2026-11-25 01:50:02 | [vcorexplatform/session](https://www.nuget.org/packages/vcorexplatform%2Fsession) | v1.0.0 |  | Cookie-based PHP sessions for Starter |
| 2026-11-25 01:50:03 | [vcorexplatform/framework](https://www.nuget.org/packages/vcorexplatform%2Fframework) | v1.1.0 |  | Starter PHP MVC application template |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
