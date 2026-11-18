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

## Latest list — 2026-11-18 15:22 UTC

New packages created between 2026-11-18 14:21 UTC and 2026-11-18 15:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T15-22-32-884871Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 14:37:38 | [djl997/laravel-transip](https://www.nuget.org/packages/djl997%2Flaravel-transip) | v6.55.0 | Dirk Jan Laros | Laravel client for the TransIP REST API v6. |
| 2026-11-18 14:49:07 | [blackbird/dynamicprice-hyva-compatibility](https://www.nuget.org/packages/blackbird%2Fdynamicprice-hyva-compatibility) | 1.0.0 |  | Blackbird Dynamic Price Compatibility with Hÿva Theme check https://store.bird.… |
| 2026-11-18 14:51:55 | [mybeast/translations-laravel](https://www.nuget.org/packages/mybeast%2Ftranslations-laravel) | v0.1.0 | My Beast | Laravel SDK for My Beast Translations (services.my-beast.com/translations): you… |
| 2026-11-18 15:01:18 | [d3creative/statamic-popcorn](https://www.nuget.org/packages/d3creative%2Fstatamic-popcorn) | v1.0.0 | D3 Creative | Popcorn by D3 Creative - Upload, choose and play Mux videos from a Statamic fie… |
| 2026-11-18 15:04:09 | [magetips/module-appliances](https://www.nuget.org/packages/magetips%2Fmodule-appliances) | 1.0.0 | Muhammad Umar | Extended Protection Plans, Delivery Fees & Appliance-Specific Checkout for Mage… |
| 2026-11-18 15:08:08 | [himacode-company/workerless](https://www.nuget.org/packages/himacode-company%2Fworkerless) | v1.0.0 | HimaCode | A Laravel queue driver that runs your jobs without cron, SSH or queue:work. Bui… |
| 2026-11-18 15:08:53 | [devfactorych/laravel-cloudflare-access](https://www.nuget.org/packages/devfactorych%2Flaravel-cloudflare-access) | v1.0.0 | Mark Cameron | Sign users into a Laravel app with Cloudflare Access (Zero Trust) SSO. |
| 2026-11-18 15:19:44 | [bannerstop/mention-api-client](https://www.nuget.org/packages/bannerstop%2Fmention-api-client) | v1.0.0 | bannerstop GmbH | Framework-agnostic PHP client for the mention-api /v2 interface: list, describe… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
