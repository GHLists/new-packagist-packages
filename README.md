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

## Latest list — 2026-11-16 11:19 UTC

New packages created between 2026-11-16 10:19 UTC and 2026-11-16 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T11-19-38-292557Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 10:29:00 | [itmosoft/laravel-vendor-payouts](https://www.nuget.org/packages/itmosoft%2Flaravel-vendor-payouts) | v1.0.1 |  | Vendor earnings ledger and payout lifecycle management for Laravel marketplace… |
| 2026-11-16 10:37:11 | [itmosoft/laravel-vendor-commissions](https://www.nuget.org/packages/itmosoft%2Flaravel-vendor-commissions) | v1.0.2 |  | Configurable vendor commission rules and commission ledger for Laravel marketpl… |
| 2026-11-16 10:45:01 | [usualtool/ut-pay](https://www.nuget.org/packages/usualtool%2Fut-pay) | v1.0 | Huang Hui | UsualTool Framework Payment SDK (Alipay / Wechat / Paypal / Douyin ecpay) with… |
| 2026-11-16 10:52:26 | [predoza/predoza-laravel](https://www.nuget.org/packages/predoza%2Fpredoza-laravel) | v1.0.0 |  | Laravel package for Predoza host sign-in: the handoff route, a Blade component… |
| 2026-11-16 10:52:26 | [predoza/predoza-php](https://www.nuget.org/packages/predoza%2Fpredoza-php) | v1.0.0 |  | Predoza host sign-in for PHP: sign your site's logged-in members in to embedded… |
| 2026-11-16 10:52:26 | [predoza/predoza-symfony](https://www.nuget.org/packages/predoza%2Fpredoza-symfony) | v1.0.0 |  | Symfony bundle for Predoza host sign-in: the handoff route, a Twig function for… |
| 2026-11-16 10:52:26 | [predoza/sdk-php](https://www.nuget.org/packages/predoza%2Fsdk-php) | v1.0.0 |  | Development repository of the Predoza PHP SDK: predoza/predoza-php, predoza/pre… |
| 2026-11-16 10:53:09 | [itmosoft/laravel-customer-groups](https://www.nuget.org/packages/itmosoft%2Flaravel-customer-groups) | v1.0.1 |  | Customer segmentation and group membership management for Laravel applications. |
| 2026-11-16 10:59:45 | [kirbydesk/kirbyblock-contactform](https://www.nuget.org/packages/kirbydesk%2Fkirbyblock-contactform) | 1.0.0 | Christian Fickinger | Contact Form Block for Kirby CMS |
| 2026-11-16 11:00:03 | [itmosoft/laravel-product-bundles](https://www.nuget.org/packages/itmosoft%2Flaravel-product-bundles) | v1.0.0 |  | Manage fixed-price and component-priced product bundles in Laravel applications. |
| 2026-11-16 11:06:29 | [mhmdelbadry74/laraselector-laravel](https://www.nuget.org/packages/mhmdelbadry74%2Flaraselector-laravel) | v0.1.0 |  | Development-only Laravel tool: click an element in the browser and jump to its… |
| 2026-11-16 11:06:42 | [shoplygg/shoply-php](https://www.nuget.org/packages/shoplygg%2Fshoply-php) | v0.11.0 |  | Shoply's API from your own server: every route as a method, safe retries, pages… |
| 2026-11-16 11:09:55 | [pulsesend/pulsesend-laravel](https://www.nuget.org/packages/pulsesend%2Fpulsesend-laravel) | v0.1.0 |  | PulseSend for Laravel: a mail transport, a facade and webhook events. |
| 2026-11-16 11:09:55 | [pulsesend/pulsesend-php](https://www.nuget.org/packages/pulsesend%2Fpulsesend-php) | v0.1.0 |  | PHP client for the PulseSend transactional email API. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
