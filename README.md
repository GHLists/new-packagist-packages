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

## Latest list — 2026-11-22 10:21 UTC

New packages created between 2026-11-22 09:21 UTC and 2026-11-22 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T10-21-08-173375Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 09:50:27 | [mtm4web/zatca-phase2-tlv-qr](https://www.nuget.org/packages/mtm4web%2Fzatca-phase2-tlv-qr) | v1.0.0 | MTM4WEB | Zero-dependency PHP 8.2+ & Laravel helper for ZATCA Phase 2 TLV Base64 QR code… |
| 2026-11-22 10:10:13 | [dzbuild/dzship](https://www.nuget.org/packages/dzbuild%2Fdzship) | v1.3.0 | DZBuild | PHP client for dzship, the free shipping API for Algeria: create and track COD… |
| 2026-11-22 10:20:15 | [fiberphp/config](https://www.nuget.org/packages/fiberphp%2Fconfig) | v0.1.0 | PangBin | ⚙️ FiberPHP 配置仓库与 .env 加载 —— 点号键只读配置、目录递归合并、.env 级联加载的零依赖纯库。 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
