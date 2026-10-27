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

## Latest list — 2026-10-27 09:22 UTC

New packages created between 2026-10-27 08:19 UTC and 2026-10-27 09:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T09-22-19-499463Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 08:20:30 | [net-os/laravel-balena-api](https://www.nuget.org/packages/net-os%2Flaravel-balena-api) | v1.0.0 | Rick Bongers | A Laravel HTTP client wrapper for the balenaCloud API. |
| 2026-10-27 08:21:50 | [maikschneider/api-key](https://www.nuget.org/packages/maikschneider%2Fapi-key) | 1.0.0 | Maik Schneider | Stateless API key authentication for TYPO3 — lets scripts, cron jobs, CI pipeli… |
| 2026-10-27 08:30:37 | [contena-cms/phpstan-contena](https://www.nuget.org/packages/contena-cms%2Fphpstan-contena) | 0.2.5 |  | PhpStan Rules for Contena |
| 2026-10-27 08:30:45 | [contena-cms/images-generator](https://www.nuget.org/packages/contena-cms%2Fimages-generator) | 1.0.1 | Yoann Vanitou; Bruce Heller | Generator of placeholder images for Faker |
| 2026-10-27 08:30:52 | [contena/dev-tools](https://www.nuget.org/packages/contena%2Fdev-tools) | 1.3.0 |  |  |
| 2026-10-27 08:32:14 | [mdestafadilah/aapanelapi](https://www.nuget.org/packages/mdestafadilah%2Faapanelapi) | v2.1.0 | mdestafadilah; NaysKutzu; sko… | PHP client for the aaPanel panel API v2 (websites, domains, SSL, MySQL database… |
| 2026-10-27 08:35:48 | [agentoom/core-compliance](https://www.nuget.org/packages/agentoom%2Fcore-compliance) | 0.8.0 |  | Agentoom EU AI Act compliance package |
| 2026-10-27 08:35:48 | [agentoom/core-privacy](https://www.nuget.org/packages/agentoom%2Fcore-privacy) | 0.8.0 |  | Agentoom PII replacement and privacy package |
| 2026-10-27 08:35:49 | [agentoom/core-main](https://www.nuget.org/packages/agentoom%2Fcore-main) | 0.9.0 |  | Agentoom Core package |
| 2026-10-27 08:35:50 | [agentoom/core-instant-messaging](https://www.nuget.org/packages/agentoom%2Fcore-instant-messaging) | 0.8.0 |  | Instant Messaging package for Agentoom |
| 2026-10-27 08:35:51 | [agentoom/core-sentinel](https://www.nuget.org/packages/agentoom%2Fcore-sentinel) | 0.8.0 |  | Agentoom Sentinel security package |
| 2026-10-27 08:35:53 | [agentoom/core-chat-widget](https://www.nuget.org/packages/agentoom%2Fcore-chat-widget) | 0.8.0 |  | Agentoom Chat Widget package |
| 2026-10-27 08:35:53 | [agentoom/core-openapi-v1](https://www.nuget.org/packages/agentoom%2Fcore-openapi-v1) | 0.8.0 |  | OpenAI-compatible API v1 adapter for Agentoom |
| 2026-10-27 08:35:55 | [agentoom/core-accessibility-widget](https://www.nuget.org/packages/agentoom%2Fcore-accessibility-widget) | 0.8.0 |  | Agentoom Accessibility Widget package |
| 2026-10-27 08:37:46 | [madbox-99/filament-essentials](https://www.nuget.org/packages/madbox-99%2Ffilament-essentials) | v2.0.0 | Zoltán Tamás Szabó | Sensible defaults for Filament: translated labels on every field, entry and col… |
| 2026-10-27 08:40:33 | [openeuropa/ai-devkit](https://www.nuget.org/packages/openeuropa%2Fai-devkit) | 0.1.0 |  | OpenEuropa layer on drupal/ai_best_practices: OE skills, Kiro steering, a guard… |
| 2026-10-27 09:12:59 | [tinovn/laravel-tinopay](https://www.nuget.org/packages/tinovn%2Flaravel-tinopay) | v1.0.0 | Tino Group | Laravel Package cho TinoPay - Tự động xác nhận thanh toán chuyển khoản ngân hàng |
| 2026-10-27 09:18:23 | [billy210504/mongodb-commenter](https://www.nuget.org/packages/billy210504%2Fmongodb-commenter) | v1.0.0 | Billy | Commenter Controller for Project tB |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
