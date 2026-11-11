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

## Latest list — 2026-11-11 12:19 UTC

New packages created between 2026-11-11 11:20 UTC and 2026-11-11 12:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T12-19-03-83144Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 11:30:06 | [clickfix/sdk](https://www.nuget.org/packages/clickfix%2Fsdk) | v0.1.0 |  | ClickFix public API client for PHP 8.1+: PSR-18 transport, typed errors, bounde… |
| 2026-11-11 11:30:09 | [clickfix/laravel](https://www.nuget.org/packages/clickfix%2Flaravel) | v0.1.0 |  | ClickFix for Laravel 10, 11, 12 and 13: service provider, ClickFix facade, arti… |
| 2026-11-11 11:31:38 | [refatbd/laravel-chatgpt-mirror](https://www.nuget.org/packages/refatbd%2Flaravel-chatgpt-mirror) | v2.1.0 | Mostafizur Rahman Refat | High-performance OpenAI-compatible API & ChatGPT Web UI reverse proxy for Larav… |
| 2026-11-11 11:38:50 | [luvittor/geoip-updater](https://www.nuget.org/packages/luvittor%2Fgeoip-updater) | v0.1.0 |  | Safe, framework-agnostic updater for MaxMind GeoLite2 and GeoIP2 databases. |
| 2026-11-11 11:42:25 | [sitebill/app-sdk](https://www.nuget.org/packages/sitebill%2Fapp-sdk) | v0.2.0 | Sitebill | SDK for installable Sitebill apps (PHP + Vue): base service provider, tenant-aw… |
| 2026-11-11 11:54:16 | [azhimov/laravel-idempotency](https://www.nuget.org/packages/azhimov%2Flaravel-idempotency) | v0.1.0 | Zhanibek Azhimov | Idempotency-Key middleware for Laravel: safe retries for POST/PATCH APIs with r… |
| 2026-11-11 12:10:19 | [limegreentangerine/content_importer_kit](https://www.nuget.org/packages/limegreentangerine%2Fcontent_importer_kit) | 1.2.1 | Dave Hendy; Lee Jones | Content Importer |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
