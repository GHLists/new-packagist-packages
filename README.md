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

## Latest list — 2026-11-28 15:22 UTC

New packages created between 2026-11-28 14:21 UTC and 2026-11-28 15:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T15-22-04-109314Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 14:29:18 | [knvillena/laravel-sibling-cookies](https://www.nuget.org/packages/knvillena%2Flaravel-sibling-cookies) | v1.0.1 | knvillena | Per-app XSRF and remember-me cookie names for Laravel apps that share a parent… |
| 2026-11-28 14:34:28 | [philipschlender/http-php](https://www.nuget.org/packages/philipschlender%2Fhttp-php) | 1.0.0 | Philip Schlender | Http |
| 2026-11-28 14:49:12 | [klsoft/yii3-doctrine-app](https://www.nuget.org/packages/klsoft%2Fyii3-doctrine-app) | 1.0.0 |  | A Yii 3 web application template that supports the Doctrine ORM |
| 2026-11-28 15:15:24 | [fiberphp/lock](https://www.nuget.org/packages/fiberphp%2Flock) | v0.1.0 | PangBin | 🔒 FiberPHP 分布式锁组件 —— 基于 Redis 的分布式锁实现，支持自动续期、阻塞等待、可扩展驱动，协程安全。 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
