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

## Latest list — 2026-10-04 18:19 UTC

New packages created between 2026-10-04 17:20 UTC and 2026-10-04 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T18-19-50-829116Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 17:31:10 | [kevinpirnie/kpt-datatables](https://www.nuget.org/packages/kevinpirnie%2Fkpt-datatables) | v2.3.60 | Kevin Pirnie | Advanced PHP DataTables library with CRUD operations, search, sorting, paginati… |
| 2026-10-04 17:34:32 | [football-api/laravel-sdk](https://www.nuget.org/packages/football-api%2Flaravel-sdk) | v1.0.0 |  | Unofficial Laravel SDK for the 5DollarFootballAPI |
| 2026-10-04 17:39:04 | [smronju/nativephp-purchases](https://www.nuget.org/packages/smronju%2Fnativephp-purchases) | 1.0.0 | Mohammad Shoriful Islam Ronju | One-time in-app purchases (non-consumables like "Remove Ads") with restore, via… |
| 2026-10-04 17:53:08 | [mage2kishan/module-admin-menu-manager](https://www.nuget.org/packages/mage2kishan%2Fmodule-admin-menu-manager) | 1.0.16 | Kishan Savaliya | Customises the Magento 2 backend menu — hide, rename, re-icon, recolor, reorder… |
| 2026-10-04 18:00:17 | [kafka-bus/metadata](https://www.nuget.org/packages/kafka-bus%2Fmetadata) | v2.0.1 | Kirill Popkov | Kafka cluster metadata for Kafka Bus: topics, partitions, consumer group offset… |
| 2026-10-04 18:00:22 | [kafka-bus/worker](https://www.nuget.org/packages/kafka-bus%2Fworker) | v2.0.1 | Kirill Popkov | Kafka polling worker infrastructure for Kafka Bus — reads messages from Kafka a… |
| 2026-10-04 18:14:59 | [kerigard/laravel-api-starter-kit](https://www.nuget.org/packages/kerigard%2Flaravel-api-starter-kit) | v1.0.0 |  | The skeleton application for the Laravel framework. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
