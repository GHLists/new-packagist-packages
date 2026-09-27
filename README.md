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

## Latest list — 2026-09-27 16:19 UTC

New packages created between 2026-09-27 15:21 UTC and 2026-09-27 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-27T16-19-14-608036Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-27 15:22:27 | [zemkogabor/xinfra-laravel](https://www.nuget.org/packages/zemkogabor%2Fxinfra-laravel) | v1.0.0 |  | Laravel integration for sending logs and errors to xInfra. |
| 2026-09-27 15:26:09 | [dirthara/routing](https://www.nuget.org/packages/dirthara%2Frouting) | 0.1.0 | Dirthara | Routing for the Dirthara Framework |
| 2026-09-27 15:26:16 | [vynex/pay-php](https://www.nuget.org/packages/vynex%2Fpay-php) | v1.0.0 |  | SDK PHP oficial da API Vynex Pay (/api/v1): recursos por família, Idempotency-K… |
| 2026-09-27 15:37:29 | [elephentity/graphql](https://www.nuget.org/packages/elephentity%2Fgraphql) | v0.1.0-alpha.1 |  | Experimental Framework-independent GraphQL integration for the Elephentity PHP… |
| 2026-09-27 15:37:29 | [elephentity/sqlite](https://www.nuget.org/packages/elephentity%2Fsqlite) | v0.1.0-alpha.1 |  | Experimental SQLite storage adaptor for the Elephentity PHP runtime. |
| 2026-09-27 15:40:57 | [upturnstudio/module-mcp](https://www.nuget.org/packages/upturnstudio%2Fmodule-mcp) | 1.0.0 | UpturnStudio | MCP (Model Context Protocol) connector exposing read-only Magento GraphQL acces… |
| 2026-09-27 15:43:42 | [f-lombardo/jev-php](https://www.nuget.org/packages/f-lombardo%2Fjev-php) | 1.0.0 | Franco Lombardo | A library to connect PHP applications to Jev APIs |
| 2026-09-27 15:48:35 | [bonsai-lint/bonsai-lint](https://www.nuget.org/packages/bonsai-lint%2Fbonsai-lint) | v0.4.3 |  | Multi-language cognitive complexity linter, as a single static binary |
| 2026-09-27 16:04:35 | [smtping/smtping-php](https://www.nuget.org/packages/smtping%2Fsmtping-php) | v1.0.0 | SMTPing | Official SMTPing SDK for PHP: verify email addresses, run bulk list jobs, and c… |
| 2026-09-27 16:04:59 | [memo2k/asksql](https://www.nuget.org/packages/memo2k%2Fasksql) | v0.1.0 | Mehmed | AI Text to SQL |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
