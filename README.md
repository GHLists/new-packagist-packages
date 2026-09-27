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

## Latest list — 2026-09-27 21:19 UTC

New packages created between 2026-09-27 20:20 UTC and 2026-09-27 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-27T21-19-39-424655Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-27 20:33:03 | [ereborcodeforge/durin-installer](https://www.nuget.org/packages/ereborcodeforge%2Fdurin-installer) | v0.1.1 | Thales Ruppenthal | Global project installer for the Durin ecosystem |
| 2026-09-27 20:53:30 | [jamacio/module-setup-wizard](https://www.nuget.org/packages/jamacio%2Fmodule-setup-wizard) | 1.0.0 | Jamacio | Web Setup Wizard for Magento 2.4: install Magento or bring a store up from an e… |
| 2026-09-27 20:56:52 | [tyrann0us/improvesearch](https://www.nuget.org/packages/tyrann0us%2Fimprovesearch) | 1.0.0 |  | MediaWiki extension that widens the built-in MySQL search: substring page title… |
| 2026-09-27 20:56:59 | [ahmad-chebbo/laravel-areeba-payment](https://www.nuget.org/packages/ahmad-chebbo%2Flaravel-areeba-payment) | v3.0.0 | Ahmad Shebbo | Laravel package for the Areeba (Mastercard Gateway) hosted checkout, refunds, c… |
| 2026-09-27 20:58:47 | [weldist/spatie-medialibrary-doctor](https://www.nuget.org/packages/weldist%2Fspatie-medialibrary-doctor) | v1.0.0 | X-Adam | Finds spatie/laravel-medialibrary media rows without a file and files without a… |
| 2026-09-27 20:59:50 | [jeffersongoncalves/filament-bladewind](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-bladewind) | 1.0.0 |  |  |
| 2026-09-27 21:09:44 | [solar-icons/blade](https://www.nuget.org/packages/solar-icons%2Fblade) | v2.0.0 | Saoudi Hakim | A package to easily make use of Solar Icons in your Laravel Blade views. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
