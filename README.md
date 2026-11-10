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

## Latest list — 2026-11-10 09:20 UTC

New packages created between 2026-11-10 08:21 UTC and 2026-11-10 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T09-20-24-799976Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 08:28:42 | [youvision/think-static](https://www.nuget.org/packages/youvision%2Fthink-static) | 1.0.0 | youvision | ThinkPHP 8 项目部署插件：主项目通过 Composer 安装或更新依赖时，自动把 project 目录部署到 public/store。 |
| 2026-11-10 08:43:42 | [reeds-hq/reeds-sdk](https://www.nuget.org/packages/reeds-hq%2Freeds-sdk) | v0.1.0 | Reeds | The official PHP library for the Reeds APIs: one client for every Reeds service… |
| 2026-11-10 08:47:46 | [mainstay/page-builder](https://www.nuget.org/packages/mainstay%2Fpage-builder) | v0.2.0 |  | The Content tab for Mainstay: the page the site draws, edited in place. |
| 2026-11-10 08:47:47 | [mainstay/parts](https://www.nuget.org/packages/mainstay%2Fparts) | v0.2.0 |  | Template parts for Mainstay: a navigation, a footer, built from blocks once per… |
| 2026-11-10 08:47:48 | [mainstay/mcp](https://www.nuget.org/packages/mainstay%2Fmcp) | v0.2.0 |  | An MCP server for Mainstay: the content API as tools a language model calls. |
| 2026-11-10 08:47:48 | [mainstay/site](https://www.nuget.org/packages/mainstay%2Fsite) | v0.2.0 |  | Public pages for Mainstay: every path an entry holds, rendered in its view. |
| 2026-11-10 08:47:49 | [mainstay/ai](https://www.nuget.org/packages/mainstay%2Fai) | v0.2.0 |  | AI providers for Mainstay: keys, defaults and a Connectors screen over laravel/… |
| 2026-11-10 08:47:49 | [mainstay/forms](https://www.nuget.org/packages/mainstay%2Fforms) | v0.2.0 |  | A form builder for Mainstay: forms built from blocks, submissions kept as entri… |
| 2026-11-10 08:48:26 | [tracewick/symfony-bundle](https://www.nuget.org/packages/tracewick%2Fsymfony-bundle) | v0.1.0 | Tracewick contributors | Official Symfony integration for Tracewick (ext-excimer sampling profiler → spo… |
| 2026-11-10 08:58:46 | [enigmainc/filament-hugeicons](https://www.nuget.org/packages/enigmainc%2Ffilament-hugeicons) | v0.1.0-alpha.2 |  | Hugeicons integration for Filament with optional default icon replacement |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
