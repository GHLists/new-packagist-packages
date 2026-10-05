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

## Latest list — 2026-10-05 03:21 UTC

New packages created between 2026-10-05 02:21 UTC and 2026-10-05 03:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T03-21-57-739976Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 02:34:12 | [mage2kishan/module-hero-slider](https://www.nuget.org/packages/mage2kishan%2Fmodule-hero-slider) | 1.1.5 | Kishan Savaliya | Hero / homepage carousel for Magento 2 (Hyva + Luma). Center-focused 3-up Splid… |
| 2026-10-05 03:00:31 | [mage2kishan/module-structured-data](https://www.nuget.org/packages/mage2kishan%2Fmodule-structured-data) | 1.3.3 | Kishan Savaliya | Panth Structured Data — JSON-LD schemas for Magento 2: Product, Breadcrumb, Org… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
