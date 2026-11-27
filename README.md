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

## Latest list — 2026-11-27 14:19 UTC

New packages created between 2026-11-27 13:19 UTC and 2026-11-27 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T14-19-08-42607Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 13:22:46 | [loki-checkout/magento2-sp](https://www.nuget.org/packages/loki-checkout%2Fmagento2-sp) | 1.0.0 |  | Spanish settings for LokiCheckout |
| 2026-11-27 13:27:58 | [loki-checkout/magento2-se](https://www.nuget.org/packages/loki-checkout%2Fmagento2-se) | 1.0.0 |  | Swedish settings for LokiCheckout |
| 2026-11-27 13:41:18 | [loki-checkout/magento2-quote-address-extended-example](https://www.nuget.org/packages/loki-checkout%2Fmagento2-quote-address-extended-example) | 0.0.1 |  | Example of adding a column to the loki_quote_address_extended table and showing… |
| 2026-11-27 13:48:37 | [elisbanpaco/phpguard](https://www.nuget.org/packages/elisbanpaco%2Fphpguard) | v0.1.0 |  | Detector experimental de código malicioso PHP mediante análisis estático y GNN |
| 2026-11-27 13:51:36 | [loki-checkout/magento2-cz](https://www.nuget.org/packages/loki-checkout%2Fmagento2-cz) | 1.0.0 |  | Czech settings for LokiCheckout |
| 2026-11-27 14:02:15 | [loki-checkout/magento2-luma-skinny](https://www.nuget.org/packages/loki-checkout%2Fmagento2-luma-skinny) | 0.0.1 |  | Attempt to remove as many Luma non-checkout elements as possible |
| 2026-11-27 14:05:29 | [cinderwatch/cinder-php](https://www.nuget.org/packages/cinderwatch%2Fcinder-php) | 1.0.0 | Rhys Lees | Framework-agnostic PHP client for Cinder error, log, trace, health and schedule… |
| 2026-11-27 14:05:31 | [cinderwatch/cinder-laravel](https://www.nuget.org/packages/cinderwatch%2Fcinder-laravel) | 1.0.0 | Rhys Lees | Laravel adapter for Cinder error, log, trace, health and schedule monitoring. |
| 2026-11-27 14:05:33 | [cinderwatch/cinder-wordpress](https://www.nuget.org/packages/cinderwatch%2Fcinder-wordpress) | 1.0.0 | Rhys Lees | WordPress adapter for Cinder error, log, trace, health and schedule monitoring. |
| 2026-11-27 14:07:16 | [cdyun/thinkphp-filesystem](https://www.nuget.org/packages/cdyun%2Fthinkphp-filesystem) | v1.0.0 | cdyun | 基于 league/flysystem实现文件系统驱动，支持本地、OSS、COS、Q牛云、AWS S3等，提供统一的文件操作接口。 |
| 2026-11-27 14:11:53 | [loki-checkout/magento2-dotdigitalgroup-sms](https://www.nuget.org/packages/loki-checkout%2Fmagento2-dotdigitalgroup-sms) | 0.0.1 |  | Compatibility module for the Dotdigital SMS module |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
