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

## Latest list — 2026-10-06 17:21 UTC

New packages created between 2026-10-06 16:19 UTC and 2026-10-06 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T17-21-02-813385Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 16:30:27 | [haithammaznai7/form-stepper](https://www.nuget.org/packages/haithammaznai7%2Fform-stepper) | 1.0.1 | Haitham Maznai | Persistent, option-driven single-step and stepper forms for Laravel with reques… |
| 2026-10-06 16:49:40 | [youwilllikeit/silverstripe-gridfield-toolkit](https://www.nuget.org/packages/youwilllikeit%2Fsilverstripe-gridfield-toolkit) | 1.0.0 |  | Advanced UX/UI components for the Silverstripe CMS GridField: inline editing, u… |
| 2026-10-06 16:54:50 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.16 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |
| 2026-10-06 16:56:50 | [ipscanner.io/sdk](https://www.nuget.org/packages/ipscanner.io%2Fsdk) | v0.1.0 | IPScanner | Official PHP client for the IPScanner API: IP lookups, VPN and proxy detection,… |
| 2026-10-06 16:58:32 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.18 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |
| 2026-10-06 16:59:38 | [vespula/remember-me](https://www.nuget.org/packages/vespula%2Fremember-me) | 0.1.1 | Jon Elofson | A simple PHP package for managing persistent 'remember me' authentication using… |
| 2026-10-06 17:15:21 | [laravel-tipi/translations](https://www.nuget.org/packages/laravel-tipi%2Ftranslations) | v0.1.0 | Irakli | Flexible Eloquent model translations for Laravel with dedicated-table, shared-t… |
| 2026-10-06 17:15:57 | [getoutbox/outbox-php](https://www.nuget.org/packages/getoutbox%2Foutbox-php) | v0.1.0 |  | Outbox Stack PHP client for transactional email |
| 2026-10-06 17:16:02 | [getoutbox/outbox-laravel](https://www.nuget.org/packages/getoutbox%2Foutbox-laravel) | v0.1.0 |  | Outbox Stack mail driver and webhooks for Laravel |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
