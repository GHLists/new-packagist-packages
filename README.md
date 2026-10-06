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

## Latest list — 2026-10-06 14:22 UTC

New packages created between 2026-10-06 13:22 UTC and 2026-10-06 14:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T14-22-07-361988Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 13:23:45 | [mage2kishan/module-notification-bar](https://www.nuget.org/packages/mage2kishan%2Fmodule-notification-bar) | 1.0.21 | Kishan Savaliya | Panth Notification Bar — display customizable notification bars, promo banners,… |
| 2026-10-06 13:30:26 | [mage2kishan/module-advanced-contact-us](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-contact-us) | 1.1.11 |  | Advanced Contact Us Page - Custom fields, bot protection, submission management… |
| 2026-10-06 13:34:11 | [nadeemkhan/atlas-self-scan](https://www.nuget.org/packages/nadeemkhan%2Fatlas-self-scan) | v1.0.0 |  | Install AtlasScope into a Laravel application and it maps that application: its… |
| 2026-10-06 13:35:27 | [mage2kishan/module-producttabs](https://www.nuget.org/packages/mage2kishan%2Fmodule-producttabs) | 1.1.7 | Kishan Savaliya | Product detail page tab customization for Magento 2. Supports horizontal/vertic… |
| 2026-10-06 13:40:28 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.16 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |
| 2026-10-06 14:02:44 | [neomasterr/barcoder](https://www.nuget.org/packages/neomasterr%2Fbarcoder) | v1.0.0 | neomasterr | Barcode utils |
| 2026-10-06 14:04:21 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.13 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
