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

## Latest list — 2026-10-06 21:21 UTC

New packages created between 2026-10-06 20:20 UTC and 2026-10-06 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T21-21-58-227754Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 20:29:00 | [letkode/config-publisher-bundle](https://www.nuget.org/packages/letkode%2Fconfig-publisher-bundle) | 1.0.0 |  | Publishes the example config files that letkode/* packages ship, with a single… |
| 2026-10-06 20:34:56 | [clarilens/parser](https://www.nuget.org/packages/clarilens%2Fparser) | 0.0.1 | Farkhat Sakibaev | Extract evidence-backed facts from HTML, XML, and PDF sources. |
| 2026-10-06 20:44:08 | [debuss-a/server-request-factory](https://www.nuget.org/packages/debuss-a%2Fserver-request-factory) | 1.0.0 | Alexandre Debusschère | Creates PSR-7 server requests from globals or arrays, with any PSR-17 implement… |
| 2026-10-06 21:01:11 | [dionisiy13/confluent-schema-registry-api](https://www.nuget.org/packages/dionisiy13%2Fconfluent-schema-registry-api) | 8.2.1 | Thomas Ploch; Denys Kurasov | Fork of flix-tech/confluent-schema-registry-api with PHP 8.5 support. A PHP 8.1… |
| 2026-10-06 21:01:45 | [kkhay/kkhay](https://www.nuget.org/packages/kkhay%2Fkkhay) | v1.0.0 | K Khay | Official PHP SDK for K Khay Sovereign Crypto Payment Gateway |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
