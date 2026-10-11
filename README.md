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

## Latest list — 2026-10-11 02:18 UTC

New packages created between 2026-10-11 01:19 UTC and 2026-10-11 02:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T02-18-42-068851Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 01:43:56 | [mainmoney/mm-aggr-wordpress](https://www.nuget.org/packages/mainmoney%2Fmm-aggr-wordpress) | v0.1.0 | MainMoney SARL | WordPress plugin for MainMoney aggregator payments |
| 2026-10-11 01:44:06 | [mainmoney/mm-aggr-woocommerce](https://www.nuget.org/packages/mainmoney%2Fmm-aggr-woocommerce) | v0.1.0 | MainMoney SARL | WooCommerce payment gateway for MainMoney aggregator |
| 2026-10-11 01:44:55 | [kuma-develop/level](https://www.nuget.org/packages/kuma-develop%2Flevel) | 1.0.0 | kuma-develop | EXP and level system for Flarum 2.0 / Hệ thống EXP và cấp độ cho Flarum 2.0 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
