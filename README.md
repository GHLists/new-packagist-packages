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

## Latest list — 2026-10-20 22:19 UTC

New packages created between 2026-10-20 21:21 UTC and 2026-10-20 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T22-19-30-42235Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 21:22:48 | [kallookoo/wp-stubs](https://www.nuget.org/packages/kallookoo%2Fwp-stubs) | 0.1.0 |  | WordPress and WooCommerce stubs for PHP |
| 2026-10-20 21:27:22 | [orderingco/ordering-theme-engine](https://www.nuget.org/packages/orderingco%2Fordering-theme-engine) | v0.4.0 | Ordering, Inc. | api-core's theme engine (version 2 themes) in PHP: the same schema, the same ru… |
| 2026-10-20 21:27:40 | [chevere/translate](https://www.nuget.org/packages/chevere%2Ftranslate) | 1.0.0 | Rodolfo Berrios | A chevere translate component. |
| 2026-10-20 21:33:27 | [risetechapps/media-for-laravel](https://www.nuget.org/packages/risetechapps%2Fmedia-for-laravel) | 1.0.0 | Rise Tech | Laravel package for advanced media and upload management, with exact storage ac… |
| 2026-10-20 21:59:55 | [zalliant/ethernize-core](https://www.nuget.org/packages/zalliant%2Fethernize-core) | v0.1.0-beta.1 |  | Núcleo do Zalliant Ethernize: container, HTTP, middleware e roteamento. |
| 2026-10-20 22:00:03 | [zalliant/ethernize-weave](https://www.nuget.org/packages/zalliant%2Fethernize-weave) | v0.1.0-beta.1 |  | Weave: compiled, contextually escaped template engine for Zalliant Ethernize. |
| 2026-10-20 22:00:11 | [zalliant/ethernize-pulse](https://www.nuget.org/packages/zalliant%2Fethernize-pulse) | v0.1.0-beta.1 |  | Pulse: server-driven reactive components for Zalliant Ethernize. |
| 2026-10-20 22:00:18 | [zalliant/ethernize-strata](https://www.nuget.org/packages/zalliant%2Fethernize-strata) | v0.1.0-beta.1 |  | Strata: persistence foundation (PDO connections, query builder, transactions, m… |
| 2026-10-20 22:00:26 | [zalliant/ethernize-shield](https://www.nuget.org/packages/zalliant%2Fethernize-shield) | v0.1.0-beta.1 |  | Shield: authentication, authorization, CSRF protection and secure sessions for… |
| 2026-10-20 22:00:34 | [zalliant/ethernize](https://www.nuget.org/packages/zalliant%2Fethernize) | v0.1.0-beta.1 |  | Application skeleton for Zalliant Ethernize (experimental beta). |
| 2026-10-20 22:05:48 | [ssdev/laravel-headless](https://www.nuget.org/packages/ssdev%2Flaravel-headless) | v0.1.1 | Sead Silajdzic | Installable Laravel foundation with authentication, teams, roles, 2FA and multi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
