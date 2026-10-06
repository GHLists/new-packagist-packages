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

## Latest list — 2026-10-06 08:22 UTC

New packages created between 2026-10-06 07:20 UTC and 2026-10-06 08:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T08-22-30-151032Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 07:26:14 | [mage2kishan/module-mage-pos](https://www.nuget.org/packages/mage2kishan%2Fmodule-mage-pos) | 1.0.16 | Kishan Savaliya | Panth MagePos - a full point of sale (POS) for Magento 2. Standalone touch-frie… |
| 2026-10-06 07:32:05 | [nadeemkhan/atlas-scope](https://www.nuget.org/packages/nadeemkhan%2Fatlas-scope) | v1.0.1 |  | Scan a Laravel, C++, C# or Python project and explore it as a 3D map of routes,… |
| 2026-10-06 07:44:23 | [maikschneider/scheduler-as-code](https://www.nuget.org/packages/maikschneider%2Fscheduler-as-code) | 0.1.0 | Maik Schneider | Manage TYPO3 scheduler tasks as YAML files in version control: export existing… |
| 2026-10-06 07:46:43 | [naiuz/sdk](https://www.nuget.org/packages/naiuz%2Fsdk) | v0.1.0 |  | The official PHP client for the NeuronAI API. |
| 2026-10-06 07:57:30 | [mage2kishan/module-low-stock-notification](https://www.nuget.org/packages/mage2kishan%2Fmodule-low-stock-notification) | 1.1.7 |  | Magento 2 Low Stock Notification module - allows customers to subscribe for bac… |
| 2026-10-06 08:01:12 | [mage2kishan/module-product-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-product-attachments) | 1.1.6 |  | Product Attachments module for Magento 2 - attach files, links, and documents t… |
| 2026-10-06 08:04:26 | [qt897/skiff](https://www.nuget.org/packages/qt897%2Fskiff) | v0.1.0 | Quoc Ta | Control Ubuntu/Debian VPS over SSH. |
| 2026-10-06 08:04:40 | [coderemon24/lkms](https://www.nuget.org/packages/coderemon24%2Flkms) | v1.0.0 | Ahmed Emon | Zero-configuration, drop-in software licensing client with RSA-2048 verificatio… |
| 2026-10-06 08:07:14 | [maarsson/agent-guidelines](https://www.nuget.org/packages/maarsson%2Fagent-guidelines) | 1.0.0 | VMaarsson | Reusable, opinionated guidelines and skills for AI coding agents. |
| 2026-10-06 08:09:37 | [ianfoxdev/inbox](https://www.nuget.org/packages/ianfoxdev%2Finbox) | v0.1.0 | Anatoly Pankratyev | Consumer-side deduplication for PHP: the message key is written in the same dat… |
| 2026-10-06 08:13:38 | [vortech/laravel-fuse](https://www.nuget.org/packages/vortech%2Flaravel-fuse) | v1.0.0 | Mate Papp | Track and enforce temporary code and technical debt in Laravel applications. |
| 2026-10-06 08:19:14 | [se7enxweb/exp_adminui](https://www.nuget.org/packages/se7enxweb%2Fexp_adminui) | v1.0.0.0 | 7x | Exponential Admin UI: the Admin UI look and layout (ported from Netgen Admin UI… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
