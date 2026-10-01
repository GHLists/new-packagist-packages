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

## Latest list — 2026-10-01 13:20 UTC

New packages created between 2026-10-01 12:22 UTC and 2026-10-01 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T13-20-46-105725Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 12:24:03 | [veewee/ext-wasm](https://www.nuget.org/packages/veewee%2Fext-wasm) | 0.1.0 | Toon Verwerft | WebAssembly for PHP: compile, instantiate and call wasm modules with an API mod… |
| 2026-10-01 12:32:05 | [codecorner/laravel-setup-wizard](https://www.nuget.org/packages/codecorner%2Flaravel-setup-wizard) | 1.0.0 |  | Browser setup wizard that starts automatically on `php artisan serve` for a fre… |
| 2026-10-01 12:44:56 | [plin-code/laravel-platform-authorizer](https://www.nuget.org/packages/plin-code%2Flaravel-platform-authorizer) | v0.1.0 | Daniele Barbaro | Remote authorization for a vendor panel and signed feature flags in self-hosted… |
| 2026-10-01 12:47:39 | [scalexy/filament-bulk-upload](https://www.nuget.org/packages/scalexy%2Ffilament-bulk-upload) | v0.0.1 |  | Direct S3 bulk upload field for Filament and Spatie Media Library |
| 2026-10-01 12:52:13 | [mage2kishan/module-product-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-product-attachments) | 1.1.2 |  | Product Attachments module for Magento 2 - attach files, links, and documents t… |
| 2026-10-01 12:56:10 | [mage2kishan/module-price-drop-alert](https://www.nuget.org/packages/mage2kishan%2Fmodule-price-drop-alert) | 1.1.2 |  | Price Drop Alert module for Magento 2 - Allows customers to subscribe to price… |
| 2026-10-01 12:58:37 | [domm98cz/color](https://www.nuget.org/packages/domm98cz%2Fcolor) | 0.1.0 | Dominik Procházka | Small PHP library for colors: create from hex, rgb, hsl or CSS, convert, tint a… |
| 2026-10-01 12:59:51 | [mage2kishan/module-low-stock-notification](https://www.nuget.org/packages/mage2kishan%2Fmodule-low-stock-notification) | 1.1.2 |  | Magento 2 Low Stock Notification module - allows customers to subscribe for bac… |
| 2026-10-01 13:03:29 | [mage2kishan/module-order-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-order-attachments) | 1.1.2 |  | Allows customers to attach files to order items |
| 2026-10-01 13:07:49 | [mage2kishan/module-advancedcart](https://www.nuget.org/packages/mage2kishan%2Fmodule-advancedcart) | 1.0.12 |  | Advanced Cart Page Enhancements - Free shipping bar, qty buttons, trust badges,… |
| 2026-10-01 13:13:44 | [mage2kishan/module-custom-options](https://www.nuget.org/packages/mage2kishan%2Fmodule-custom-options) | 1.0.9 | Kishan Savaliya | Panth Custom Options — beautifully styled product custom options for Hyva-based… |
| 2026-10-01 13:18:18 | [mage2kishan/module-checkout-extended](https://www.nuget.org/packages/mage2kishan%2Fmodule-checkout-extended) | 1.1.6 | Kishan Savaliya | Enhanced one-page checkout for Magento 2 with configurable multi-column layouts… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
