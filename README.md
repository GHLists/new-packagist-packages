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

## Latest list — 2026-10-28 06:19 UTC

New packages created between 2026-10-28 05:21 UTC and 2026-10-28 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T06-19-29-183529Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 05:31:36 | [mitydigital/cargo-australia-post](https://www.nuget.org/packages/mitydigital%2Fcargo-australia-post) | 1.0.0 |  |  |
| 2026-10-28 05:44:14 | [lck/swoft](https://www.nuget.org/packages/lck%2Fswoft) | v2.0.13 |  | Swoft skeleton application, PHP 8.4 ready maintained fork |
| 2026-10-28 05:48:34 | [faysoft/kbutils](https://www.nuget.org/packages/faysoft%2Fkbutils) | 1.0.0 | fayfox | 公共工具类 |
| 2026-10-28 05:58:17 | [phattarachai/laravel-kradan](https://www.nuget.org/packages/phattarachai%2Flaravel-kradan) | v0.1.0 | Phattarachai Chaimongkol | A review board inside your Laravel app: Claude pushes pages that ask for a deci… |
| 2026-10-28 05:58:44 | [warsita/warsita-php](https://www.nuget.org/packages/warsita%2Fwarsita-php) | v0.1.0 |  | Official PHP client for the Warsita WhatsApp API: send messages, manage session… |
| 2026-10-28 06:09:10 | [astral-php/astral-testing](https://www.nuget.org/packages/astral-php%2Fastral-testing) | 0.1.0 | astral-php | Helpers de test Astral — HttpTestCase, factories, assertions (events / mails /… |
| 2026-10-28 06:15:17 | [touhidurabir/envlens](https://www.nuget.org/packages/touhidurabir%2Fenvlens) | 1.0.0 | Touhidur Rahman | Inspect, compare, audit and safely maintain Laravel .env files. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
