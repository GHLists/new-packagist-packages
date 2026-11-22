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

## Latest list — 2026-11-22 13:20 UTC

New packages created between 2026-11-22 12:19 UTC and 2026-11-22 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T13-20-47-613421Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 12:26:22 | [sunder6218/laravel-crate.io](https://www.nuget.org/packages/sunder6218%2Flaravel-crate.io) | v14.1.0 | Sunder S | Crate.io driver for Laravel |
| 2026-11-22 12:37:17 | [datacircle/laravel-mcp-tools](https://www.nuget.org/packages/datacircle%2Flaravel-mcp-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. Four Laravel MCP tools call Datacircle's public API. Yo… |
| 2026-11-22 12:40:17 | [sunder6218/html](https://www.nuget.org/packages/sunder6218%2Fhtml) | v6.5.0 | Sunder S | HTML and Form Builders for the Laravel Framework |
| 2026-11-22 12:46:17 | [sunder6218/adldap2-laravel](https://www.nuget.org/packages/sunder6218%2Fadldap2-laravel) | v6.2.0 |  | LDAP Authentication & Management for Laravel. |
| 2026-11-22 12:48:42 | [survos/ai-embed-bundle](https://www.nuget.org/packages/survos%2Fai-embed-bundle) | 2.45.83 |  | Model-aware embedding requests, reusable vector caches and document embedding w… |
| 2026-11-22 12:52:47 | [sunder6218/adldap2](https://www.nuget.org/packages/sunder6218%2Fadldap2) | v10.6.0 | Sunder | A PHP LDAP Package for humans. |
| 2026-11-22 13:00:36 | [oe2i/panda](https://www.nuget.org/packages/oe2i%2Fpanda) | v1.0.0 | Anthony Osawere; oe2i | Opinionated Laravel 13 + Livewire 4 + Flux UI starter kit. |
| 2026-11-22 13:01:05 | [fiberphp/redis](https://www.nuget.org/packages/fiberphp%2Fredis) | v0.1.0 | PangBin | 🔴 Redis 协程客户端 —— 基于 Workerman 连接池与 phpredis，多连接池化、协程内复用、协程结束自动归还。 |
| 2026-11-22 13:02:55 | [zimmer-yan/open-sentinel](https://www.nuget.org/packages/zimmer-yan%2Fopen-sentinel) | 0.1.0 |  | Simple open source sentry alternative |
| 2026-11-22 13:16:10 | [nwidart/laravel-actuator](https://www.nuget.org/packages/nwidart%2Flaravel-actuator) | 1.0.0 | Nicolas Widart | Production-ready monitoring endpoints for Laravel, modelled on Spring Boot Actu… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
