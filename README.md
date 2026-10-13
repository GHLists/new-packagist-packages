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

## Latest list — 2026-10-13 14:20 UTC

New packages created between 2026-10-13 13:20 UTC and 2026-10-13 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T14-20-22-041716Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 13:23:48 | [forge/archive](https://www.nuget.org/packages/forge%2Farchive) | v0.1.0 |  | Archive extraction and creation for macOS |
| 2026-10-13 13:42:54 | [mage-obsidian/module-inventory-in-store-pickup](https://www.nuget.org/packages/mage-obsidian%2Fmodule-inventory-in-store-pickup) | 4.1.0 |  | In-store pickup for the MageObsidian checkout: a delivery method selector and a… |
| 2026-10-13 13:43:55 | [tranquil-tools/laravel-table-builder](https://www.nuget.org/packages/tranquil-tools%2Flaravel-table-builder) | 1.0.0 | ComfyCoders BV | Define Laravel tables in PHP: columns, filters, search, sorting, bulk and row a… |
| 2026-10-13 13:44:14 | [stellarwp/banners](https://www.nuget.org/packages/stellarwp%2Fbanners) | 1.0.0 | StellarWP; Dimi | Marketing banners for WordPress admin pages, dismissed per user across every pl… |
| 2026-10-13 13:47:03 | [kalp707/maho-razorpay](https://www.nuget.org/packages/kalp707%2Fmaho-razorpay) | 1.0.0 |  | Razorpay payment gateway module for Maho Commerce |
| 2026-10-13 13:48:04 | [medienbaecker/kirby-editoria11y](https://www.nuget.org/packages/medienbaecker%2Fkirby-editoria11y) | 0.1.0 | Thomas Günther | Editoria11y accessibility checker for Kirby editors |
| 2026-10-13 13:48:29 | [esfahanahan/phpstan-rules](https://www.nuget.org/packages/esfahanahan%2Fphpstan-rules) | v1.0.1 | EsfahanAhan | Custom PHPStan rules and extensions for EsfahanAhan. |
| 2026-10-13 13:50:44 | [sitekit/docs](https://www.nuget.org/packages/sitekit%2Fdocs) | 1.0.0 | Sitekit | 编写文档：包括分类和文档，并支持前端浏览。 |
| 2026-10-13 14:05:33 | [artisanpack-ui/ecommerce-storefront-livewire](https://www.nuget.org/packages/artisanpack-ui%2Fecommerce-storefront-livewire) | v1.0.0 | Jacob Martella | Livewire storefront for the ArtisanPack UI ecommerce engine. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
