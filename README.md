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

## Latest list — 2026-10-12 17:19 UTC

New packages created between 2026-10-12 16:19 UTC and 2026-10-12 17:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T17-19-38-531284Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 16:41:21 | [png/laravel-sync-engine](https://www.nuget.org/packages/png%2Flaravel-sync-engine) | v1.0.0 |  | Offline-first bidirectional sync engine for Laravel |
| 2026-10-12 16:46:51 | [laravel-monitor/laravel-monitor](https://www.nuget.org/packages/laravel-monitor%2Flaravel-monitor) | v1.0.0 |  | Laravel Application Monitoring Package — sends non-sensitive health metadata to… |
| 2026-10-12 16:50:14 | [r-portal/t-rule](https://www.nuget.org/packages/r-portal%2Ft-rule) | v1.0.1 | rochev yakov | Common contracts for the template rule |
| 2026-10-12 16:58:18 | [polaris/agent](https://www.nuget.org/packages/polaris%2Fagent) | v0.10.0 | 2am.tech | The PHP agent SDK for Polaris for PHP: discover a Polaris server, register or e… |
| 2026-10-12 16:58:18 | [polaris/agents](https://www.nuget.org/packages/polaris%2Fagents) | v0.10.0 | 2am.tech | AI agents as principals for Polaris for PHP: registration and host enrolment, d… |
| 2026-10-12 16:58:18 | [polaris/mcp](https://www.nuget.org/packages/polaris%2Fmcp) | v0.10.0 | 2am.tech | Polaris for PHP and the Model Context Protocol: protect any PHP MCP server with… |
| 2026-10-12 17:15:54 | [curentis/openfga-php](https://www.nuget.org/packages/curentis%2Fopenfga-php) | v1.0.0 |  | PHP SDK for OpenFGA — fine-grained, relationship-based authorization (Zanzibar-… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
