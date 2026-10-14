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

## Latest list — 2026-10-14 11:21 UTC

New packages created between 2026-10-14 10:21 UTC and 2026-10-14 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T11-21-06-701125Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 10:49:18 | [webpatser/fledge-apm](https://www.nuget.org/packages/webpatser%2Ffledge-apm) | v0.1.0 | Christoph Kempen | Fiber-aware OpenTelemetry tracing for the Fledge framework, exported as OTLP to… |
| 2026-10-14 10:52:54 | [deployecommerce/magento-community-patches](https://www.nuget.org/packages/deployecommerce%2Fmagento-community-patches) | 1.0.0 |  | Applies Adobe's official Magento Open Source security patches automatically on… |
| 2026-10-14 11:02:19 | [webpatser/fledge-pulse](https://www.nuget.org/packages/webpatser%2Ffledge-pulse) | v1.8.1.0 | Taylor Otwell; Christoph Kemp… | Fiber-native fork of Laravel Pulse for the Fledge framework: a real-time applic… |
| 2026-10-14 11:08:40 | [webpatser/fledge-pulse-elasticsearch](https://www.nuget.org/packages/webpatser%2Ffledge-pulse-elasticsearch) | v0.1.0 | Christoph Kempen | Elasticsearch storage driver for Fledge Pulse: entries in a data stream with IL… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
