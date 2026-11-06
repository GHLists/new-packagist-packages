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

## Latest list — 2026-11-06 18:21 UTC

New packages created between 2026-11-06 17:21 UTC and 2026-11-06 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T18-21-49-974209Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 17:35:33 | [maco-studios/mage-os-installer](https://www.nuget.org/packages/maco-studios%2Fmage-os-installer) | v0.0.4 |  | An interactive Mage-OS project installer and Composer project factory. |
| 2026-11-06 17:41:15 | [siberfx/laravel-logger](https://www.nuget.org/packages/siberfx%2Flaravel-logger) | 1.0.1 | Selim Gormus | A tiny, zero-config Eloquent activity logger that stores old/new values togethe… |
| 2026-11-06 17:42:28 | [muckiware/core](https://www.nuget.org/packages/muckiware%2Fcore) | 0.0.2.0 |  | Muckidrive core component |
| 2026-11-06 17:48:40 | [hryvinskyi/magento2-admin-ui](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-admin-ui) | 1.0.0 | Volodymyr Hryvinskyi | A shared look for Magento 2 admin screens: one opt-in stylesheet of hui-* compo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
