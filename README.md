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

## Latest list — 2026-10-23 15:20 UTC

New packages created between 2026-10-23 14:19 UTC and 2026-10-23 15:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T15-20-19-534701Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 14:20:51 | [payum-payu/payum-payu](https://www.nuget.org/packages/payum-payu%2Fpayum-payu) | v1.0.0 | Serhii Puzikov | PayU (REST API 2.1) gateway for Payum: hosted checkout, card-token recurring pa… |
| 2026-10-23 14:22:07 | [tapp/filament-mcp](https://www.nuget.org/packages/tapp%2Ffilament-mcp) | v0.1.0 | Tapp Network | MCP for Laravel apps in Filament: a token page with one Sanctum ability per too… |
| 2026-10-23 14:28:05 | [pteal79/otp-code](https://www.nuget.org/packages/pteal79%2Fotp-code) | 1.0.0 | Peter Teal | One-time code input EDGE element (<native:otp-code>) for NativePHP Mobile: one… |
| 2026-10-23 14:32:19 | [rohama/koin-zibal](https://www.nuget.org/packages/rohama%2Fkoin-zibal) | 2.2.1 | Rohama | Koin — Zibal gateway driver (IPG REST v1) |
| 2026-10-23 14:34:27 | [malikad/php2shell-guard](https://www.nuget.org/packages/malikad%2Fphp2shell-guard) | v0.3.0 | Malik Adnan | Read-only runtime, SAPI, stale-worker, configuration, and IaC auditor for PHP2S… |
| 2026-10-23 14:39:45 | [jlrodriguezdev/laravel-bot-protection](https://www.nuget.org/packages/jlrodriguezdev%2Flaravel-bot-protection) | v1.0.1 | jlrodriguezdev | High-performance Laravel WAF & Anti-Bot Middleware mitigating automated scanner… |
| 2026-10-23 14:49:18 | [analytics-platform/platform](https://www.nuget.org/packages/analytics-platform%2Fplatform) | v0.2.1 | steviec87 | Firewall, error monitoring and server analytics for your PHP or Laravel site, r… |
| 2026-10-23 14:51:49 | [skeeks/cms-proposal](https://www.nuget.org/packages/skeeks%2Fcms-proposal) | 1.0.0 | Semenov Alexander | Commercial proposals for SkeekS CMS CRM: versions, items with sections, templat… |
| 2026-10-23 15:04:41 | [markup-carve/cakephp-carve](https://www.nuget.org/packages/markup-carve%2Fcakephp-carve) | 0.1.0 | Markup Carve | CakePHP plugin for Carve: rendering, views, validation, ORM behavior, commands… |
| 2026-10-23 15:10:46 | [cmdimu/pwa-builder](https://www.nuget.org/packages/cmdimu%2Fpwa-builder) | v1.0.0 | cmdimu | Progressive Web App (PWA) Builder for Laravel, CodeIgniter 4, and CodeIgniter 3 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
