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

## Latest list — 2026-10-03 13:21 UTC

New packages created between 2026-10-03 12:22 UTC and 2026-10-03 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T13-21-46-568308Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 12:27:59 | [nerova/sdk](https://www.nuget.org/packages/nerova%2Fsdk) | v0.3.0-beta.2 | Nerova Systems | Server-side PHP client for the Nerova stable tenant-v1 API. |
| 2026-10-03 12:29:50 | [golo/symfony-anthropic-wrapper](https://www.nuget.org/packages/golo%2Fsymfony-anthropic-wrapper) | v0.1.1 | Barry O'Neil | Symfony bundle for the official Anthropic PHP SDK: YAML-configured defaults, pe… |
| 2026-10-03 12:32:10 | [wp-alchemist/framework](https://www.nuget.org/packages/wp-alchemist%2Fframework) | v0.1.0 |  | Runtime helpers for WordPress plugins scaffolded with wp-alchemist: lifecycle,… |
| 2026-10-03 12:35:03 | [stewart-php/client](https://www.nuget.org/packages/stewart-php%2Fclient) | v0.1.0 |  | Home Assistant WebSocket client. Usable on its own |
| 2026-10-03 12:35:07 | [stewart-php/support](https://www.nuget.org/packages/stewart-php%2Fsupport) | v0.1.0 |  | Framework-internal helpers shared by the Stewart packages. Not part of the app-… |
| 2026-10-03 12:35:16 | [stewart-php/skeleton](https://www.nuget.org/packages/stewart-php%2Fskeleton) | v0.1.0 |  | A new Stewart project: Home Assistant automations in PHP |
| 2026-10-03 12:35:21 | [stewart-php/store](https://www.nuget.org/packages/stewart-php%2Fstore) | v0.1.0 |  | Scoping, encoding and hydration for Stewart's key-value storage. Backend-agnost… |
| 2026-10-03 12:35:25 | [stewart-php/testing](https://www.nuget.org/packages/stewart-php%2Ftesting) | v0.1.0 |  | Shared test doubles for the Stewart packages. A development dependency, not par… |
| 2026-10-03 12:35:42 | [stewart-php/contracts](https://www.nuget.org/packages/stewart-php%2Fcontracts) | v0.1.0 |  | Stewart core abstractions. Pure PHP and one cron parser |
| 2026-10-03 12:35:53 | [stewart-php/runtime](https://www.nuget.org/packages/stewart-php%2Fruntime) | v0.1.0 |  | Stewart broker, workers and the channel protocol between them. |
| 2026-10-03 12:35:54 | [stewart-php/store-redis](https://www.nuget.org/packages/stewart-php%2Fstore-redis) | v0.1.0 |  | Redis backend for Stewart's key-value storage. Non-blocking, over amphp |
| 2026-10-03 12:36:08 | [stewart-php/codegen](https://www.nuget.org/packages/stewart-php%2Fcodegen) | v0.1.0 |  | Generates typed entity and service classes from a Home Assistant instance |
| 2026-10-03 12:38:32 | [mage2kishan/module-core](https://www.nuget.org/packages/mage2kishan%2Fmodule-core) | 1.2.5 | Kishan Savaliya | Panth Core - base module providing shared utilities, admin configuration helper… |
| 2026-10-03 12:44:17 | [maatify/php-i18n](https://www.nuget.org/packages/maatify%2Fphp-i18n) | v1.0.0-rc.1 | Maatify | Database-driven internationalization library for structured translation keys, e… |
| 2026-10-03 13:00:56 | [sahicheck/sahicheck-php](https://www.nuget.org/packages/sahicheck%2Fsahicheck-php) | v0.1.0 | SahiCheck | Official PHP SDK for the SahiCheck verification API |
| 2026-10-03 13:09:48 | [makallio85/cakephp-sso](https://www.nuget.org/packages/makallio85%2Fcakephp-sso) | v1.0.0 | Marko Kallio | CakePHP 5 plugin that signs users in through the central Rock Software identity… |
| 2026-10-03 13:17:31 | [mage2kishan/module-malware-scanner](https://www.nuget.org/packages/mage2kishan%2Fmodule-malware-scanner) | 1.3.6 | Kishan Savaliya | Active malware prevention + on-disk scanner for Magento 2. Three real-time guar… |
| 2026-10-03 13:20:03 | [mage2kishan/module-order-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-order-attachments) | 1.1.6 |  | Allows customers to attach files to order items |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
