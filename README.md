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

## Latest list — 2026-10-07 13:20 UTC

New packages created between 2026-10-07 12:18 UTC and 2026-10-07 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T13-20-57-951616Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 12:29:34 | [citomni/upload](https://www.nuget.org/packages/citomni%2Fupload) | v1.0.0.0 | Lars Grove Mortensen | File intake and storage for CitOmni apps: validated uploads, local public/priva… |
| 2026-10-07 12:44:04 | [omega-mvc/framework](https://www.nuget.org/packages/omega-mvc%2Fframework) | 1.0.0 | Adriano Giovannini | OmegaFramework is a lightweight and modular PHP framework designed for building… |
| 2026-10-07 12:48:11 | [xddesigners/silverstripe-better-forms](https://www.nuget.org/packages/xddesigners%2Fsilverstripe-better-forms) | 1.0.0 | Remy Vaartjes | Nicer CMS forms: a Bootstrap grid layout field, help tooltips after labels, and… |
| 2026-10-07 12:57:11 | [andydefer/php-locationiq](https://www.nuget.org/packages/andydefer%2Fphp-locationiq) | v0.1.0 | Andy Kani | PHP SDK for LocationIQ and Nominatim APIs: balance, timezone, directions, and r… |
| 2026-10-07 13:00:12 | [wexample/symfony-activity](https://www.nuget.org/packages/wexample%2Fsymfony-activity) | 1.0.1 |  |  |
| 2026-10-07 13:03:22 | [wexample/symfony-activity-ds](https://www.nuget.org/packages/wexample%2Fsymfony-activity-ds) | 1.0.1 |  |  |
| 2026-10-07 13:07:18 | [abdulkadiragoliya/asset-guardian](https://www.nuget.org/packages/abdulkadiragoliya%2Fasset-guardian) | 1.0.0 | Abdulkadir Agoliya | Asset Health & Safe Cleanup for Craft CMS. Know what's safe to review before yo… |
| 2026-10-07 13:12:39 | [khaledabdalbasit/launchpoint](https://www.nuget.org/packages/khaledabdalbasit%2Flaunchpoint) | v1.0.6 |  | Laravel Starter Kit for API |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
