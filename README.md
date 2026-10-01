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

## Latest list — 2026-10-01 10:20 UTC

New packages created between 2026-10-01 09:22 UTC and 2026-10-01 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T10-20-23-522087Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 09:27:11 | [mage2kishan/module-dynamic-forms](https://www.nuget.org/packages/mage2kishan%2Fmodule-dynamic-forms) | 1.2.2 |  | Dynamic Forms module for Magento 2 - Create and manage custom forms with drag-a… |
| 2026-10-01 09:34:48 | [mage2kishan/module-advanced-contact-us](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-contact-us) | 1.1.2 |  | Advanced Contact Us Page - Custom fields, bot protection, submission management… |
| 2026-10-01 09:48:05 | [wexample/symfony-mail-ds](https://www.nuget.org/packages/wexample%2Fsymfony-mail-ds) | 1.0.1 |  |  |
| 2026-10-01 09:48:37 | [wexample/symfony-mail-demo](https://www.nuget.org/packages/wexample%2Fsymfony-mail-demo) | 1.0.1 |  |  |
| 2026-10-01 09:54:08 | [larascan/larascan](https://www.nuget.org/packages/larascan%2Flarascan) | v1.0.0-alpha | Emre Balasar | Measure and analyze your Laravel 13 Core native adoption rate, discover used &… |
| 2026-10-01 09:57:11 | [nexia-cloud-os/devtools](https://www.nuget.org/packages/nexia-cloud-os%2Fdevtools) | v0.1.0 |  | Standalone Nexia App source generators |
| 2026-10-01 10:12:34 | [mage2kishan/module-mega-menu](https://www.nuget.org/packages/mage2kishan%2Fmodule-mega-menu) | 1.0.13 | Kishan Savaliya | Advanced mega menu for Magento 2 — works on Hyva and Luma. Drag-and-drop tree b… |
| 2026-10-01 10:16:27 | [mage2kishan/module-notification-bar](https://www.nuget.org/packages/mage2kishan%2Fmodule-notification-bar) | 1.0.12 | Kishan Savaliya | Panth Notification Bar — display customizable notification bars, promo banners,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
