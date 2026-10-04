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

## Latest list — 2026-10-04 08:20 UTC

New packages created between 2026-10-04 07:19 UTC and 2026-10-04 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T08-20-48-432523Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 07:41:40 | [mage2kishan/module-index-now](https://www.nuget.org/packages/mage2kishan%2Fmodule-index-now) | 1.1.3 | Kishan Savaliya | Panth IndexNow — instantly notify Bing, Yandex and other search engines when co… |
| 2026-10-04 08:17:00 | [mage2kishan/module-productgallery](https://www.nuget.org/packages/mage2kishan%2Fmodule-productgallery) | 1.0.14 | Kishan Savaliya | Custom product image gallery for Magento 2 product detail pages. Features confi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
