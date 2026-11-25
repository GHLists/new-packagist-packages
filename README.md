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

## Latest list — 2026-11-25 15:19 UTC

New packages created between 2026-11-25 14:21 UTC and 2026-11-25 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T15-19-57-003862Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 14:28:12 | [ahasend/symfony-mailer](https://www.nuget.org/packages/ahasend%2Fsymfony-mailer) | v1.0.0 | Farhad Hedayatifard; Symfony… | AhaSend Mailer Bridge: the Symfony 8.2 bridge, with API v2 and webhooks, for Sy… |
| 2026-11-25 14:30:02 | [dimmi/dimmi-php](https://www.nuget.org/packages/dimmi%2Fdimmi-php) | v0.1.0 |  | PHP client for the dimmi REST API, identity tokens for the messenger and webhoo… |
| 2026-11-25 14:30:07 | [dimmi/dimmi-laravel](https://www.nuget.org/packages/dimmi%2Fdimmi-laravel) | v0.1.0 |  | dimmi for Laravel: the messenger with signed identity, the REST API client, web… |
| 2026-11-25 14:34:34 | [captchacore/statamic](https://www.nuget.org/packages/captchacore%2Fstatamic) | v1.2.0 | SpeedIT Solutions | Privacy-friendly CAPTCHA and bot defense for Statamic forms — proof of work ins… |
| 2026-11-25 14:35:06 | [ahasend/laravel-mailer](https://www.nuget.org/packages/ahasend%2Flaravel-mailer) | v1.0.0 | AhaSend; Aamir Yaqoob | AhaSend for Laravel 11, 12 and 13: API v2 and SMTP mail transports, and webhooks |
| 2026-11-25 14:42:20 | [coretsia/platform-routing](https://www.nuget.org/packages/coretsia%2Fplatform-routing) | v0.14.0 | Vladyslav Mudrichenko | Coretsia routing runtime package: deterministic route compilation, artifact-bac… |
| 2026-11-25 14:51:57 | [webdna/craft-cookiebot-embeds](https://www.nuget.org/packages/webdna%2Fcraft-cookiebot-embeds) | 1.0.0 | webdna | Third-party videos, maps, widgets and tracking scripts wait for the visitor's C… |
| 2026-11-25 14:56:01 | [emaia/laravel-hotwire-starter](https://www.nuget.org/packages/emaia%2Flaravel-hotwire-starter) | v0.1.0 |  | A Laravel starter kit with Hotwire and Docker. |
| 2026-11-25 14:59:37 | [tracksim/tracksim-php](https://www.nuget.org/packages/tracksim%2Ftracksim-php) | v1.0.0 | Omnibyte Technologies Limited | Official PHP and Laravel client for the TrackSim API and webhooks |
| 2026-11-25 14:59:52 | [muckiware/mucki-safe-agent-plugin](https://www.nuget.org/packages/muckiware%2Fmucki-safe-agent-plugin) | v0.1.0 | muckiware | MuckiSafe Agent plugin for Shopware 6 - agent control plane for MuckiSafe host… |
| 2026-11-25 15:01:59 | [adachsoft/mailbox-gmail](https://www.nuget.org/packages/adachsoft%2Fmailbox-gmail) | v0.1.1 | Arkadiusz Adach | Gmail API adapter for the AdachSoft provider-independent mailbox contract. |
| 2026-11-25 15:02:30 | [threadable/state-machine](https://www.nuget.org/packages/threadable%2Fstate-machine) | 0.1.0 | Padraig Nolan; Tomasz Mrozińs… | State Machine for Laravel by Threadable |
| 2026-11-25 15:03:40 | [james-draper/archipelago](https://www.nuget.org/packages/james-draper%2Farchipelago) | v1.0.0 |  | PHP 5.0.0+ compatible legacy refactoring framework. |
| 2026-11-25 15:05:03 | [licers/licers](https://www.nuget.org/packages/licers%2Flicers) | v1.0.0 | Licers | License keys for PHP apps and WordPress plugins: Ed25519-signed checks, device… |
| 2026-11-25 15:13:22 | [igne-agency/laravel-nova](https://www.nuget.org/packages/igne-agency%2Flaravel-nova) | v0.1.0 | Rick Blanksma | Reusable Laravel Nova 5 features for IGNE projects: a grouped main menu, panel… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
