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

## Latest list — 2026-10-14 20:22 UTC

New packages created between 2026-10-14 19:20 UTC and 2026-10-14 20:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T20-22-08-741517Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 19:22:35 | [laraxgram/apiserver](https://www.nuget.org/packages/laraxgram%2Fapiserver) | v0.1.0 | AmirHossein | A Telegram Bot API server built on LaraGram MTProto. |
| 2026-10-14 19:30:14 | [x-laravel/sluggable](https://www.nuget.org/packages/x-laravel%2Fsluggable) | v1.0.0 | Mehmet ÖĞMEN | Slugs for Eloquent models with Turkish-aware generation, race-safe uniqueness a… |
| 2026-10-14 19:32:22 | [angeo/module-ucp-checkout](https://www.nuget.org/packages/angeo%2Fmodule-ucp-checkout) | 1.0.0 |  | UCP checkout for Magento 2 (dev.ucp.shopping.checkout + discount + fulfillment,… |
| 2026-10-14 19:37:26 | [factusmart/sdk](https://www.nuget.org/packages/factusmart%2Fsdk) | v0.1.0 | FactuSmart | SDK oficial en PHP del API de facturación electrónica de FactuSmart (SUNAT, Per… |
| 2026-10-14 19:41:29 | [x-laravel/username](https://www.nuget.org/packages/x-laravel%2Fusername) | v1.0.0 | Mehmet ÖĞMEN | Configurable username validation, reserved-name checking and username generatio… |
| 2026-10-14 19:52:40 | [runomine/runomine-php](https://www.nuget.org/packages/runomine%2Frunomine-php) | v0.1.0 |  | Cookieless, server-side analytics for runomine: pageviews, business events and… |
| 2026-10-14 20:10:02 | [disrex/magento-patch-installer](https://www.nuget.org/packages/disrex%2Fmagento-patch-installer) | 0.1.0 | Disrex | Applies Magento 2 / Adobe Commerce security patches, verifies they stay applied… |
| 2026-10-14 20:10:19 | [gavtaylor/rememberme](https://www.nuget.org/packages/gavtaylor%2Frememberme) | v0.1.0 | Gavin Taylor | "Keep me logged in" for Roundcube: longer sessions only for browsers you choose… |
| 2026-10-14 20:10:45 | [disrex/magento-security-patches](https://www.nuget.org/packages/disrex%2Fmagento-security-patches) | 0.1.0 | Disrex | Adobe's isolated and out-of-band security patches for Magento Open Source, Adob… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
