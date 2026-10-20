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

## Latest list — 2026-10-20 11:22 UTC

New packages created between 2026-10-20 10:21 UTC and 2026-10-20 11:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T11-22-11-017465Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 10:31:13 | [vielhuber/pinboardmcp](https://www.nuget.org/packages/vielhuber%2Fpinboardmcp) | v1.1.0 |  | Minimal PHP helper and MCP server for the complete Pinboard v1 API. |
| 2026-10-20 10:31:38 | [dmitriy-zhukov/my-test-library](https://www.nuget.org/packages/dmitriy-zhukov%2Fmy-test-library) | 1.0.1 | Дмитрий Жуков | test library 2 |
| 2026-10-20 10:41:12 | [shipaurora/borealis-theme](https://www.nuget.org/packages/shipaurora%2Fborealis-theme) | v1.0.0 | Thomas Alrek | Borealis, Aurora CMS's default admin theme: its styles, design tokens and prebu… |
| 2026-10-20 10:46:18 | [juststeveking/kit](https://www.nuget.org/packages/juststeveking%2Fkit) | v0.1.2 |  | Opinionated Laravel API starter kit: token authentication, standards-compliant… |
| 2026-10-20 10:46:39 | [farhanchoksi/laravel-pretty-logger](https://www.nuget.org/packages/farhanchoksi%2Flaravel-pretty-logger) | v1.0.1 | Farhanchoksi | Laravel Pretty Logger — a pretty_dio_logger style HTTP request/response logger… |
| 2026-10-20 10:57:42 | [hanane/outbound-guard-bundle](https://www.nuget.org/packages/hanane%2Foutbound-guard-bundle) | v0.1.0 | Hanane | Detect excessive, duplicated and slow Symfony HttpClient calls with safe metric… |
| 2026-10-20 10:58:26 | [nocache-dev/laravel](https://www.nuget.org/packages/nocache-dev%2Flaravel) | v1.0.0 |  | Correct Cache-Control headers for Laravel responses, plus artisan commands to c… |
| 2026-10-20 11:16:55 | [moneymoves/sdk](https://www.nuget.org/packages/moneymoves%2Fsdk) | v1.0.0 |  | The official PHP library for the Money Moves Business API: checkouts, payments,… |
| 2026-10-20 11:21:24 | [municipio/wp-plugin-municipio-editor-extensions](https://www.nuget.org/packages/municipio%2Fwp-plugin-municipio-editor-extensions) | 0.1.0 |  | Accessible editorial guidance for TinyMCE fields in modern Municipio. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
