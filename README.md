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

## Latest list — 2026-11-07 17:21 UTC

New packages created between 2026-11-07 16:19 UTC and 2026-11-07 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T17-21-01-990082Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 16:31:30 | [siberfx/flysystem-wasabi](https://www.nuget.org/packages/siberfx%2Fflysystem-wasabi) | 0.1.1 | Selim Görmüş | Wasabi Hot Cloud Storage filesystem driver for Laravel 12 and 13 (Flysystem v3). |
| 2026-11-07 16:35:46 | [tihloh/smsgate](https://www.nuget.org/packages/tihloh%2Fsmsgate) | v0.1.0 | Christian Borsal Bustamante | Framework-independent SMSGate integration: approved Android gateways, personali… |
| 2026-11-07 16:36:47 | [clesson-de/silverstripe-pdf-templates](https://www.nuget.org/packages/clesson-de%2Fsilverstripe-pdf-templates) | 1.0.0 | Kai Feldmaier | PDF template management for Silverstripe CMS. Define page layouts with margins,… |
| 2026-11-07 16:47:10 | [simonschaufi/typo3-cms-scanner](https://www.nuget.org/packages/simonschaufi%2Ftypo3-cms-scanner) | v14.0.0 | Christian Kuhn; Oliver Hader;… | TYPO3 CMS static file analysis |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
