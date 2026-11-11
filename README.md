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

## Latest list — 2026-11-11 11:20 UTC

New packages created between 2026-11-11 10:21 UTC and 2026-11-11 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T11-20-14-183018Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 10:22:21 | [sendio/sendio-php](https://www.nuget.org/packages/sendio%2Fsendio-php) | v1.0.0 | send.io | Official send.io PHP SDK. |
| 2026-11-11 10:22:30 | [sendio/sendio-laravel](https://www.nuget.org/packages/sendio%2Fsendio-laravel) | v1.0.0 | send.io | Official send.io integration for Laravel: mail transport, facade and webhooks. |
| 2026-11-11 10:24:01 | [evalship/tinyeval](https://www.nuget.org/packages/evalship%2Ftinyeval) | v0.11.0 |  | Evals for the AI calls in your PHP or Laravel app, run by one bash file |
| 2026-11-11 10:33:05 | [magicpay/magicpay-php](https://www.nuget.org/packages/magicpay%2Fmagicpay-php) | v0.1.0 | MagicPay | Official PHP SDK for the MagicPay payment API |
| 2026-11-11 10:47:05 | [logipro/turbolead-api](https://www.nuget.org/packages/logipro%2Fturbolead-api) | v0.1.0 | Frédéric Royet | Shared PSR-18 transport for Turbolead REST API clients |
| 2026-11-11 10:47:44 | [limegreentangerine/cookie_manager_kit](https://www.nuget.org/packages/limegreentangerine%2Fcookie_manager_kit) | v1.0.0 | Dave Hendy | ConcreteCMS package to manage Cookie Banner |
| 2026-11-11 10:55:00 | [cardee/phphypher](https://www.nuget.org/packages/cardee%2Fphphypher) | v8.5.0 | Sergei Gruzdov | Hyphenation library and MODX Revolution output filter |
| 2026-11-11 10:59:44 | [logipro/turbolead-core-php](https://www.nuget.org/packages/logipro%2Fturbolead-core-php) | v0.1.0 | Frédéric Royet | PHP client for the Turbolead core REST API (`/api/turbolead` and `/api/user`) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
