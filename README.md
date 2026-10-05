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

## Latest list — 2026-10-05 05:21 UTC

New packages created between 2026-10-05 04:22 UTC and 2026-10-05 05:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T05-21-46-775876Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 05:06:15 | [wentthefox/services_libravatar](https://www.nuget.org/packages/wentthefox%2Fservices_libravatar) | v1.0.3 | Melissa Draper; Christian Wei… | API interfacing class for libravatar.org |
| 2026-10-05 05:16:40 | [mage2kishan/module-advanced-product-grid](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-product-grid) | 1.0.11 | Kishan Savaliya | Advanced Product Grid for Magento 2 admin - inline edit every column (text, sel… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
