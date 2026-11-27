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

## Latest list — 2026-11-27 10:19 UTC

New packages created between 2026-11-27 09:19 UTC and 2026-11-27 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T10-19-29-638932Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 09:23:37 | [hryvinskyi/magento2-free-gift-import-amasty](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-free-gift-import-amasty) | 1.0.0 | Volodymyr Hryvinskyi | Imports the free gift setup of Amasty Free Gift and Free Bar into the free gift… |
| 2026-11-27 09:26:33 | [storeteam/module-disable-compare](https://www.nuget.org/packages/storeteam%2Fmodule-disable-compare) | 1.0.0 | StoreTeam — Magento 2 & Hyvä… | Lightweight Magento 2.4.x & Hyvä Theme module to cleanly disable Compare Produc… |
| 2026-11-27 09:31:53 | [loki-checkout/magento2-fi](https://www.nuget.org/packages/loki-checkout%2Fmagento2-fi) | 1.0.0 |  | Finnish settings for LokiCheckout |
| 2026-11-27 09:40:52 | [carbon/inject-javascript-on-login-page](https://www.nuget.org/packages/carbon%2Finject-javascript-on-login-page) | 0.1.0 |  | Inject JavaScript into the Neos backend login page |
| 2026-11-27 09:57:03 | [yireo/magento2-remove-search](https://www.nuget.org/packages/yireo%2Fmagento2-remove-search) | 1.0.0 |  | N/A |
| 2026-11-27 10:00:06 | [loki-checkout/magento2-dk](https://www.nuget.org/packages/loki-checkout%2Fmagento2-dk) | 1.0.0 |  | Danish settings for LokiCheckout |
| 2026-11-27 10:00:10 | [loki-checkout/magento2-it](https://www.nuget.org/packages/loki-checkout%2Fmagento2-it) | 0.0.1 |  | Italian settings for LokiCheckout |
| 2026-11-27 10:00:23 | [loki-checkout/magento2-ie](https://www.nuget.org/packages/loki-checkout%2Fmagento2-ie) | 1.0.0 |  | Irish settings for LokiCheckout |
| 2026-11-27 10:11:59 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.54.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
