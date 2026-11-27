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

## Latest list — 2026-11-27 13:19 UTC

New packages created between 2026-11-27 12:21 UTC and 2026-11-27 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T13-19-30-950686Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 12:23:01 | [qiick/laravel-http-basics](https://www.nuget.org/packages/qiick%2Flaravel-http-basics) | v1.0.0-beta.1 | Qiick | Shared HTTP runtime for qiick Laravel products: X-Request-Id, Accept-Language /… |
| 2026-11-27 12:44:09 | [kariricode/router](https://www.nuget.org/packages/kariricode%2Frouter) | v4.1.0 | Walmir Silva | Protocol-agnostic routing engine for PHP 8.4+: static routes in a hash map, par… |
| 2026-11-27 12:44:11 | [kariricode/cache](https://www.nuget.org/packages/kariricode%2Fcache) | v4.1.0 | Walmir Silva | Multi-tier cache for PHP 8.4+: SIEVE eviction, XFetch probabilistic early recom… |
| 2026-11-27 12:45:27 | [visus/module-admin-sso-login](https://www.nuget.org/packages/visus%2Fmodule-admin-sso-login) | 1.0.0 |  | Magento module providing SAML single sign-on for admin users |
| 2026-11-27 12:47:30 | [loki-checkout/magento2-joseph-leedy-custom-fees](https://www.nuget.org/packages/loki-checkout%2Fmagento2-joseph-leedy-custom-fees) | 1.0.0 |  | Compatibility module for the JosephLeedy CustomFees module |
| 2026-11-27 13:00:29 | [mhinspeya/module-onlineshop](https://www.nuget.org/packages/mhinspeya%2Fmodule-onlineshop) | 1.0.0 | MHinspeya | OnlineShop app webview login |
| 2026-11-27 13:03:55 | [nsilver/laravel-click-merchant](https://www.nuget.org/packages/nsilver%2Flaravel-click-merchant) | v0.1.0 |  | Laravel integration for CLICK Merchant API |
| 2026-11-27 13:10:51 | [neuron-core/iq-stream-php](https://www.nuget.org/packages/neuron-core%2Fiq-stream-php) | 1.0.0 | Valerio Barbera | IQ-Stream official client library for the PHP ecosystem. |
| 2026-11-27 13:12:53 | [jonesshen/php-cs-fixer-config](https://www.nuget.org/packages/jonesshen%2Fphp-cs-fixer-config) | v1.0.0 | Jone Shen | A custom PHP CS Fixer configuration library |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
