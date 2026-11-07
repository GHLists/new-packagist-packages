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

## Latest list — 2026-11-07 16:19 UTC

New packages created between 2026-11-07 15:20 UTC and 2026-11-07 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T16-19-54-093154Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 15:29:36 | [andydefer/laravel-support](https://www.nuget.org/packages/andydefer%2Flaravel-support) | v0.2.0 | Andy Kani | Client support ticketing system for Laravel with polymorphic author/assignee an… |
| 2026-11-07 15:31:07 | [phview/framework](https://www.nuget.org/packages/phview%2Fframework) | v1.0.0 | Rafael Faria | Declarative Server-Side Rendering (SSR) engine in PHP with native Alpine.js int… |
| 2026-11-07 15:33:03 | [prestashopheaven/build-tools](https://www.nuget.org/packages/prestashopheaven%2Fbuild-tools) | v1.0.1 | George van Engers | The PrestaHaven module factory: the ps-module command (checks, PHPStan per Pres… |
| 2026-11-07 15:37:54 | [lgu-bayambang-ict-office/lgu-laravel-development-standards](https://www.nuget.org/packages/lgu-bayambang-ict-office%2Flgu-laravel-development-standards) | v1.0.0 | Ricky Bulalakaw; Information… | Philippine LGU statutory engineering standards, architecture traits, AI complia… |
| 2026-11-07 15:49:43 | [shoplygg/shoply-php](https://www.nuget.org/packages/shoplygg%2Fshoply-php) | v0.9.0 |  | Shoply's API from your own server: every route as a method, safe retries, pages… |
| 2026-11-07 16:02:24 | [payerurl/telegrambot-crypto-payment-instant-payout](https://www.nuget.org/packages/payerurl%2Ftelegrambot-crypto-payment-instant-payout) | 1.0.0 | Rashiqul Rony | telegram crypto payment gateway laravel |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
