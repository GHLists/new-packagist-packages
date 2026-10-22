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

## Latest list — 2026-10-22 20:20 UTC

New packages created between 2026-10-22 19:20 UTC and 2026-10-22 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T20-20-28-659258Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 19:20:46 | [luxsite/symfony-ecommerce](https://www.nuget.org/packages/luxsite%2Fsymfony-ecommerce) | v0.1.0 | LuxSite | Symfony ecommerce LuxSite: open-source e-commerce engine on Symfony (Apache 2.0… |
| 2026-10-22 19:20:50 | [amjadiqbal/filament-stat-cards](https://www.nuget.org/packages/amjadiqbal%2Ffilament-stat-cards) | v1.0.0 | Amjad Iqbal | Richer stat cards for the Filament 4 and 5 stats overview widget: progress bars… |
| 2026-10-22 19:22:00 | [risetechapps/orchestrator-link-for-laravel](https://www.nuget.org/packages/risetechapps%2Forchestrator-link-for-laravel) | 1.0.0 | Rise Tech | Cliente Laravel da API Orchestrator da RiseTech. |
| 2026-10-22 19:22:16 | [chattrn/connector](https://www.nuget.org/packages/chattrn%2Fconnector) | v1.0.1 |  | Serves the Chattrn API (devspec.txt: "Slice 3: Laravel package installer") from… |
| 2026-10-22 19:24:32 | [silvershop-suite/import](https://www.nuget.org/packages/silvershop-suite%2Fimport) | 1.0.0 | Remy Vaartjes; SilverShop-Sui… | Channel-agnostic import engine for SilverShop (CMS 6): a two-phase stage→apply… |
| 2026-10-22 19:24:47 | [krafsys/framework](https://www.nuget.org/packages/krafsys%2Fframework) | v0.1.0 | Krafsys Technologies | A lightweight, batteries-included PHP framework: routing, ORM, auth, queues, ma… |
| 2026-10-22 19:25:50 | [krafsys/krafsys](https://www.nuget.org/packages/krafsys%2Fkrafsys) | v0.1.1 |  | The Krafsys application skeleton. |
| 2026-10-22 19:37:51 | [smtpfast/smtpfast-php](https://www.nuget.org/packages/smtpfast%2Fsmtpfast-php) | v0.1.0 |  | The official PHP SDK for the SMTPfast API. |
| 2026-10-22 19:38:48 | [cengizkemec/passkeys](https://www.nuget.org/packages/cengizkemec%2Fpasskeys) | v1.0.0 | Cengiz Kemeç | Passkey (WebAuthn/FIDO2) authentication for Flarum 2.0 |
| 2026-10-22 19:39:34 | [hypelabs-llc/connect](https://www.nuget.org/packages/hypelabs-llc%2Fconnect) | v0.1.0 |  | The PHP client for the HypeLabs Connect API. |
| 2026-10-22 19:53:21 | [amjadiqbal/filament-uptime-monitor](https://www.nuget.org/packages/amjadiqbal%2Ffilament-uptime-monitor) | v1.0.0 | Amjad Iqbal | A Filament 4 and 5 admin UI for spatie/laravel-uptime-monitor: add, edit, enabl… |
| 2026-10-22 20:05:45 | [romansh/omnipay-whop](https://www.nuget.org/packages/romansh%2Fomnipay-whop) | v1.0.0 | Roman Shalabanov | Whop driver for Omnipay payment processing library |
| 2026-10-22 20:18:11 | [smtpfast/smtpfast-laravel](https://www.nuget.org/packages/smtpfast%2Fsmtpfast-laravel) | v0.1.0 |  | Send Laravel mail through the SMTPfast API, with the SMTPfast PHP client and we… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
