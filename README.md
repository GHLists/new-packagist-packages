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

## Latest list — 2026-10-24 11:22 UTC

New packages created between 2026-10-24 10:20 UTC and 2026-10-24 11:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T11-22-28-792161Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 10:31:11 | [yavuz-dev/filament-theme](https://www.nuget.org/packages/yavuz-dev%2Ffilament-theme) | v1.2.1 | Yavuz | A panel theme for Filament: dark full-height sidebar, a top bar with breadcrumb… |
| 2026-10-24 10:31:29 | [saivra/meui-theme](https://www.nuget.org/packages/saivra%2Fmeui-theme) | v0.1.0 | Saivra Technologies; Ghulam M… | A native light and dark application theme for Filament 5. |
| 2026-10-24 10:34:18 | [gared/php-fints](https://www.nuget.org/packages/gared%2Fphp-fints) | 4.2.0 |  | PHP Library for the protocols fints and hbci |
| 2026-10-24 10:37:50 | [atoria/alfred](https://www.nuget.org/packages/atoria%2Falfred) | v1.0.2 | Andria Toria | Point at anything in your Laravel app and ask how it is calculated, change it w… |
| 2026-10-24 11:01:07 | [djosend/php-sdk](https://www.nuget.org/packages/djosend%2Fphp-sdk) | v0.1.0 |  | PHP client for the Djosend Messages API |
| 2026-10-24 11:04:46 | [tmonier/sylius-erp-flatfile-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-erp-flatfile-plugin) | v0.1.0 | Thibaut Monier | Flat-file exchange with an ERP for Sylius 2: orders exported as CSV files (docu… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
