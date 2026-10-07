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

## Latest list — 2026-10-07 08:20 UTC

New packages created between 2026-10-07 07:20 UTC and 2026-10-07 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T08-20-00-780059Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 07:22:53 | [derrickob/laravel-nuxt-shadcn](https://www.nuget.org/packages/derrickob%2Flaravel-nuxt-shadcn) | v0.1.1 | Derrick Obedgiu | A Laravel starter kit with Vue, Inertia and Nuxt UI. |
| 2026-10-07 07:25:43 | [useyona/einvoice-php](https://www.nuget.org/packages/useyona%2Feinvoice-php) | v0.1.0 | Yona | Official PHP SDK for the Yona e-invoicing API — what an API key may call: invoi… |
| 2026-10-07 07:28:20 | [mage2kishan/module-checkout-extended](https://www.nuget.org/packages/mage2kishan%2Fmodule-checkout-extended) | 1.1.11 | Kishan Savaliya | Enhanced one-page checkout for Magento 2 with configurable multi-column layouts… |
| 2026-10-07 08:05:07 | [mage2kishan/module-product-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-product-attachments) | 1.1.10 |  | Product Attachments module for Magento 2 - attach files, links, and documents t… |
| 2026-10-07 08:08:49 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.19 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |
| 2026-10-07 08:12:30 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.20 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
