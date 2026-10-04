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

## Latest list — 2026-10-04 15:18 UTC

New packages created between 2026-10-04 14:20 UTC and 2026-10-04 15:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T15-18-51-67512Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 14:24:36 | [mage2kishan/module-indexer-manager](https://www.nuget.org/packages/mage2kishan%2Fmodule-indexer-manager) | 1.2.3 | Kishan Savaliya | Panth Indexer Manager — reindex Magento 2 from the admin with strategy options… |
| 2026-10-04 14:27:44 | [lambda-twelve/one-record-laravel](https://www.nuget.org/packages/lambda-twelve%2Fone-record-laravel) | 1.0.0-beta1 | Nick Andriopoulos | Laravel integration for lambda-twelve/one-record: service provider, routes, dat… |
| 2026-10-04 14:28:45 | [kevinpirnie/kpt-datatables](https://www.nuget.org/packages/kevinpirnie%2Fkpt-datatables) | v2.3.47 | Kevin Pirnie | Advanced PHP DataTables library with CRUD operations, search, sorting, paginati… |
| 2026-10-04 14:30:18 | [bootok/http](https://www.nuget.org/packages/bootok%2Fhttp) | v1.0.0 | hellobin | 基于 Symfony HttpClient 的 HTTP 客户端，完全兼容 yzh52521/easyhttp 门面 API（高版本 PHP 替代方案） |
| 2026-10-04 15:06:56 | [mage2kishan/module-low-stock-notification](https://www.nuget.org/packages/mage2kishan%2Fmodule-low-stock-notification) | 1.1.6 |  | Magento 2 Low Stock Notification module - allows customers to subscribe for bac… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
