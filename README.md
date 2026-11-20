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

## Latest list — 2026-11-20 02:19 UTC

New packages created between 2026-11-20 01:21 UTC and 2026-11-20 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T02-19-29-235901Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 01:30:38 | [hejunjie/wechat-clawbot](https://www.nuget.org/packages/hejunjie%2Fwechat-clawbot) | v1.0.0 | 何俊杰 | WeChat ClawBot API client for PHP — QR-code login, long-polling messages, send/… |
| 2026-11-20 01:55:09 | [nowo-tech/currency-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fcurrency-kit-bundle) | v0.1.0 | Héctor Franco Aceituno; Nowo.… | Currency conversion at reference rates for Symfony: ECB euro reference rates st… |
| 2026-11-20 01:58:03 | [js-upup/reference-image-batch-checker](https://www.nuget.org/packages/js-upup%2Freference-image-batch-checker) | v0.1.0 |  | Check local reference image batches for upload limits and identical files |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
