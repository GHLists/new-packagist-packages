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

## Latest list — 2026-11-25 13:20 UTC

New packages created between 2026-11-25 12:20 UTC and 2026-11-25 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T13-20-34-105353Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 12:39:45 | [sparkable/magento-mago-attribute-sets](https://www.nuget.org/packages/sparkable%2Fmagento-mago-attribute-sets) | 1.0.0 |  | Mago Assistant tool that reads and rearranges the groups and attributes of a pr… |
| 2026-11-25 12:39:45 | [sparkable/magento-mago-bulk-update](https://www.nuget.org/packages/sparkable%2Fmagento-mago-bulk-update) | 1.0.0 |  | Mago Assistant tool that sets attribute values on many products and adds attrib… |
| 2026-11-25 12:39:45 | [sparkable/magento-mago-product-finder](https://www.nuget.org/packages/sparkable%2Fmagento-mago-product-finder) | 1.0.0 |  | Mago Assistant tool that finds products, parent products and product attributes |
| 2026-11-25 12:42:02 | [hans2103/magento2-hyva-dashboard-google](https://www.nuget.org/packages/hans2103%2Fmagento2-hyva-dashboard-google) | v26.48.0 | Hans Kuijpers | Google Analytics 4 and Google Search Console widgets for the Hyvä Admin Dashboa… |
| 2026-11-25 12:51:46 | [salvatore/laravel-sanctum-manager](https://www.nuget.org/packages/salvatore%2Flaravel-sanctum-manager) | 1.1.0 | Salvatore Cervone | Advanced Scope/Ability registry, hierarchical wildcards, token lifecycle manage… |
| 2026-11-25 12:56:25 | [zangles/laravel-mda](https://www.nuget.org/packages/zangles%2Flaravel-mda) | v0.1.0 | Guido Fonticelli | Generadores y reglas de arquitectura para Model Domain Architecture (MDA) en La… |
| 2026-11-25 13:08:51 | [webid-am/laravel](https://www.nuget.org/packages/webid-am%2Flaravel) | v0.1.0 |  | Sign in with webid for Laravel sites: one connection key, the sign-in routes, u… |
| 2026-11-25 13:11:43 | [ianfoxdev/webhook-outbox](https://www.nuget.org/packages/ianfoxdev%2Fwebhook-outbox) | v0.1.0 | Anatoly Pankratyev | Webhooks queued in your database transaction and delivered by a separate relay,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
