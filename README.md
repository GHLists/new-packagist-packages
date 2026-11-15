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

## Latest list — 2026-11-15 11:20 UTC

New packages created between 2026-11-15 10:20 UTC and 2026-11-15 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T11-20-31-591752Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 10:28:07 | [youvision/think-store-codeditor](https://www.nuget.org/packages/youvision%2Fthink-store-codeditor) | 1.0.0 | indiboy-create; AI | ThinkPHP 8 模板代码编辑器扩展：基于 Ace 与 layui 编辑 HTML + PHP 混合模板，提供页面、读取、更新、新增与静态资源路由。 |
| 2026-11-15 10:37:28 | [shubhamkanungoo007/module-media-orphan-finder](https://www.nuget.org/packages/shubhamkanungoo007%2Fmodule-media-orphan-finder) | 1.0.0 |  | A Magento 2 module to find and clean orphaned media files. |
| 2026-11-15 10:59:46 | [abdalazeze/laravel-coupons](https://www.nuget.org/packages/abdalazeze%2Flaravel-coupons) | v0.1.1 | Abdulaziz Nour Eddin | Concurrency-safe coupons, discounts, and cashback engine for Laravel |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
