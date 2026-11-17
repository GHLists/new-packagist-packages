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

## Latest list — 2026-11-17 11:21 UTC

New packages created between 2026-11-17 10:21 UTC and 2026-11-17 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T11-21-06-177563Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 10:24:36 | [itmosoft/laravel-comments](https://www.nuget.org/packages/itmosoft%2Flaravel-comments) | 1.0.1 |  | Polymorphic comments and threaded discussions for Laravel Eloquent models. |
| 2026-11-17 10:28:10 | [itmosoft/laravel-workflows](https://www.nuget.org/packages/itmosoft%2Flaravel-workflows) | 1.0.1 |  | Configurable stateful business workflows, transitions, and execution history fo… |
| 2026-11-17 10:33:12 | [itmosoft/laravel-file-manager](https://www.nuget.org/packages/itmosoft%2Flaravel-file-manager) | v1.0.0 |  | File uploads, folder organization, polymorphic ownership, and storage metadata… |
| 2026-11-17 10:36:25 | [itmosoft/laravel-analytics](https://www.nuget.org/packages/itmosoft%2Flaravel-analytics) | v1.0.0 |  | Application event tracking and time-based metric aggregation for Laravel applic… |
| 2026-11-17 10:42:02 | [kayko/mulla-laravel](https://www.nuget.org/packages/kayko%2Fmulla-laravel) | v0.0.1 |  | Official Laravel integration for the Mulla payment gateway (MTN MoMo & Airtel M… |
| 2026-11-17 10:42:05 | [itmosoft/laravel-api-keys](https://www.nuget.org/packages/itmosoft%2Flaravel-api-keys) | v1.0.0 |  | Secure, scoped API key management for Laravel applications, with hashed secrets… |
| 2026-11-17 10:42:45 | [wovosoft/laravel-uniexporter](https://www.nuget.org/packages/wovosoft%2Flaravel-uniexporter) | v1.0.0 | Narayan Adhikary | Describe a document once as a schema and export it to PDF, DOCX, XLSX or any fo… |
| 2026-11-17 10:49:12 | [jerry-ai-2026/db-tools](https://www.nuget.org/packages/jerry-ai-2026%2Fdb-tools) | v1.0.0 | Jerry | Laravel 数据库导入/导出工具命令集：JSON/CSV/Excel 导入，JSON/迁移/种子导出，连接信息查看。 |
| 2026-11-17 11:04:57 | [leverprice/leverprice-php](https://www.nuget.org/packages/leverprice%2Fleverprice-php) | v0.3.0 | Leverprice | Server-side SDK for Leverprice price experiments |
| 2026-11-17 11:08:25 | [nickdekruijk/listmailing-php](https://www.nuget.org/packages/nickdekruijk%2Flistmailing-php) | 0.1.0 | Nick de Kruijk | Client for the ListMailing sign-up API, with an optional Laravel layer: config,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
