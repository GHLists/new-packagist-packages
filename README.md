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

## Latest list — 2026-10-28 15:19 UTC

New packages created between 2026-10-28 14:20 UTC and 2026-10-28 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T15-19-13-920086Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 14:32:41 | [pdfkiln/pdfkiln](https://www.nuget.org/packages/pdfkiln%2Fpdfkiln) | 1.0.3 |  | Drop-in replacement for wkhtmltopdf, powered by Chromium: vendor/bin/wkhtmltopd… |
| 2026-10-28 14:49:25 | [ardanayatraa/laravel-mcp-hub](https://www.nuget.org/packages/ardanayatraa%2Flaravel-mcp-hub) | v0.1.0-alpha.1 | Ardana Yatra | Application-owned Laravel source APIs and a scoped MCP Hub client. |
| 2026-10-28 14:52:33 | [ollily/php-sonar-scanner](https://www.nuget.org/packages/ollily%2Fphp-sonar-scanner) | 0.1.0-BETA | ollily | A sonar-scanner for PHP using composer |
| 2026-10-28 15:01:40 | [rabbitevents/outbox](https://www.nuget.org/packages/rabbitevents%2Foutbox) | v0.1.0 | Eugene Kirdzei | Delivers RabbitEvents messages through a database outbox: written in the transa… |
| 2026-10-28 15:05:57 | [coyshdigital/craft-small-change](https://www.nuget.org/packages/coyshdigital%2Fcraft-small-change) | 1.0.0 | Coysh Digital | A small, Stripe-only shop and donations plugin for Craft CMS. Built for chariti… |
| 2026-10-28 15:06:48 | [dsdcr/tronweb](https://www.nuget.org/packages/dsdcr%2Ftronweb) | v2.1.1 | dsdcr | 专业的PHP SDK，用于与TRON波场区块链网络交互，提供HTTP API封装、智能合约部署与调用、TRC20代币管理、交易构建与签名功能 |
| 2026-10-28 15:08:30 | [brbunny/brway](https://www.nuget.org/packages/brbunny%2Fbrway) | v1.0.0 | Kevin Siqueira; Robson V. Lei… | Roteador PHP simples para MVC e APIs: verbos RESTful, grupos, rotas nomeadas, m… |
| 2026-10-28 15:09:20 | [binhtq1/kern-core](https://www.nuget.org/packages/binhtq1%2Fkern-core) | v0.2.0 |  | Upgradeable Kern CMS runtime |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
