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

## Latest list — 2026-10-01 23:20 UTC

New packages created between 2026-10-01 22:22 UTC and 2026-10-01 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T23-20-17-598612Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 22:23:58 | [hipsterjazzbo/php-style](https://www.nuget.org/packages/hipsterjazzbo%2Fphp-style) | 0.1.0 |  | Shared PHP-CS-Fixer configuration for HipsterJazzbo projects. |
| 2026-10-01 22:24:23 | [mage2kishan/module-product-slider](https://www.nuget.org/packages/mage2kishan%2Fmodule-product-slider) | 1.1.2 |  | Advanced Product Slider widget with extensive customization options for Magento… |
| 2026-10-01 22:30:33 | [fundrik/coding-standard](https://www.nuget.org/packages/fundrik%2Fcoding-standard) | v0.9.0 | Denis Yanchevskiy | Custom PHP_CodeSniffer rules for Fundrik |
| 2026-10-01 22:34:51 | [mage2kishan/module-dynamic-forms](https://www.nuget.org/packages/mage2kishan%2Fmodule-dynamic-forms) | 1.2.6 |  | Dynamic Forms module for Magento 2 - Create and manage custom forms with drag-a… |
| 2026-10-01 22:38:18 | [mage2kishan/module-admin-menu-manager](https://www.nuget.org/packages/mage2kishan%2Fmodule-admin-menu-manager) | 1.0.15 | Kishan Savaliya | Customises the Magento 2 backend menu — hide, rename, re-icon, recolor, reorder… |
| 2026-10-01 22:52:24 | [1994/ghostwriter-core](https://www.nuget.org/packages/1994%2Fghostwriter-core) | v0.1.0 | 1994 | The framework-free core shared by the Ghostwriter addons for Statamic, Filament… |
| 2026-10-01 23:14:46 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.4 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |
| 2026-10-01 23:18:06 | [mage2kishan/module-eu-withdrawal](https://www.nuget.org/packages/mage2kishan%2Fmodule-eu-withdrawal) | 1.1.6 | Kishan Savaliya | Panth EU Withdrawal Button - a clear, accessible digital withdrawal (cancellati… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
