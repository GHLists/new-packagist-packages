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

## Latest list — 2026-09-29 04:19 UTC

New packages created between 2026-09-29 03:22 UTC and 2026-09-29 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T04-19-05-215423Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 04:08:16 | [qiangvei/theme-amazon](https://www.nuget.org/packages/qiangvei%2Ftheme-amazon) | 1.0.0 |  | Amazon style theme for Magento 2.4 |
| 2026-09-29 04:08:30 | [pimbay/search-query-pimcore](https://www.nuget.org/packages/pimbay%2Fsearch-query-pimcore) | v1.0.0 | Jan Sarmir | Pimcore Listing adapter for pimbay/search-query. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
