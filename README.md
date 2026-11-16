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

## Latest list — 2026-11-16 10:19 UTC

New packages created between 2026-11-16 09:22 UTC and 2026-11-16 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T10-19-47-127599Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 09:23:40 | [pixiaoka/orm](https://www.nuget.org/packages/pixiaoka%2Form) | v0.1.0 |  | Annotation-driven Active Record ORM for PHP 8.3+. Zero framework dependency. PD… |
| 2026-11-16 09:24:08 | [ortic/concretecms-ortic-mcp-server](https://www.nuget.org/packages/ortic%2Fconcretecms-ortic-mcp-server) | v0.1.0 |  | Concrete CMS package that turns a site into a Model Context Protocol (MCP) serv… |
| 2026-11-16 09:37:23 | [abdulwahhabkhan/device-auth-livewire](https://www.nuget.org/packages/abdulwahhabkhan%2Fdevice-auth-livewire) | v0.2.1 | Abdul Wahhab Khan | Livewire + Alpine frontend for abdulwahhabkhan/device-auth: device verification… |
| 2026-11-16 09:37:23 | [abdulwahhabkhan/device-auth-react](https://www.nuget.org/packages/abdulwahhabkhan%2Fdevice-auth-react) | v0.2.1 | Abdul Wahhab Khan | Inertia + React pages for abdulwahhabkhan/device-auth: device verification, con… |
| 2026-11-16 09:40:04 | [t-labs-co/crash-guard](https://www.nuget.org/packages/t-labs-co%2Fcrash-guard) | v1.0.0 | Ty Huynh | Lightweight exception capture, deduplication & notification for Laravel — with… |
| 2026-11-16 09:53:46 | [kontainer/laravel-model-cache](https://www.nuget.org/packages/kontainer%2Flaravel-model-cache) | v1.0.0 | Matthias Isler | A Redis based, automated and scalable database caching layer for Laravel |
| 2026-11-16 09:53:56 | [degriz/openmage-braintree](https://www.nuget.org/packages/degriz%2Fopenmage-braintree) | v3.2.0 |  | Braintree payments (Gene_Braintree) for OpenMage 20 / PHP 8 - Web SDK 3.147, 3D… |
| 2026-11-16 10:04:25 | [degriz/openmage-openai-ads](https://www.nuget.org/packages/degriz%2Fopenmage-openai-ads) | 1.0.0 | Anze Voh | OpenAI Ads (ChatGPT) measurement pixel and Conversions API for OpenMage / Magen… |
| 2026-11-16 10:04:28 | [degriz/openmage-moosend](https://www.nuget.org/packages/degriz%2Fopenmage-moosend) | 2.0.0 | Anze Voh | Moosend website tracking (page views, product views, add to cart, orders) for O… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
