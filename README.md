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

## Latest list — 2026-10-15 14:21 UTC

New packages created between 2026-10-15 13:22 UTC and 2026-10-15 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T14-21-55-716314Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 13:25:50 | [apavliukov/laravel-ai-core](https://www.nuget.org/packages/apavliukov%2Flaravel-ai-core) | v0.2.2 | Aleksandr Pavliukov | Shared AI core on top of laravel/ai: model catalogue with prices, request ledge… |
| 2026-10-15 13:27:13 | [pollora/meta](https://www.nuget.org/packages/pollora%2Fmeta) | v0.1.0 | Amphibee | Typed WordPress meta declared with attributes: register_meta(), typed reads and… |
| 2026-10-15 13:29:10 | [laravelopenpackages/laravel-optimized](https://www.nuget.org/packages/laravelopenpackages%2Flaravel-optimized) | v1.0.0 | Zeeshan Ali | Laravel, optimized: a compiled request path for Laravel applications, with Lara… |
| 2026-10-15 13:36:56 | [achttienvijftien/make-pot-twig](https://www.nuget.org/packages/achttienvijftien%2Fmake-pot-twig) | 1.0.0 | 1815 | Adds Twig template support to `wp i18n make-pot`, using Twig's own parser. |
| 2026-10-15 13:47:36 | [mnd/back-office-sdk](https://www.nuget.org/packages/mnd%2Fback-office-sdk) | v1.0.1 |  | PHP SDK of back-office with a Laravel adapter: client, DTO, webhook signature c… |
| 2026-10-15 13:53:06 | [agrekom/customization-payment](https://www.nuget.org/packages/agrekom%2Fcustomization-payment) | v1.1.0 |  | Customization for Magento payment methods |
| 2026-10-15 14:07:25 | [everysize/checkout-shopware6](https://www.nuget.org/packages/everysize%2Fcheckout-shopware6) | 3.1.1 | everysize GmbH | everysize Checkout: Bestellungen aus dem everysize-Direktkauf in Shopware 6 / o… |
| 2026-10-15 14:13:10 | [wexample/symfony-preference](https://www.nuget.org/packages/wexample%2Fsymfony-preference) | 1.0.1 |  |  |
| 2026-10-15 14:19:41 | [pollora/roles](https://www.nuget.org/packages/pollora%2Froles) | v0.1.0 | Amphibee | WordPress roles and capabilities declared with attributes: a #[Role] class, #[M… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
