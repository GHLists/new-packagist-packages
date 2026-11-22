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

## Latest list — 2026-11-22 16:18 UTC

New packages created between 2026-11-22 15:18 UTC and 2026-11-22 16:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T16-18-33-462371Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 15:19:12 | [fiberphp/http](https://www.nuget.org/packages/fiberphp%2Fhttp) | v0.1.0 | PangBin | 🌐 FiberPHP HTTP 子系统 —— 基于 Workerman 协议实现，支持请求/响应/中间件、协程管道、协程隔离。 |
| 2026-11-22 15:23:12 | [effyads/laravel](https://www.nuget.org/packages/effyads%2Flaravel) | v1.0.1 |  | EffyAds advertisement sync, rendering and click/view tracking for Laravel appli… |
| 2026-11-22 15:25:00 | [fiberphp/router](https://www.nuget.org/packages/fiberphp%2Frouter) | v0.1.0 | PangBin | 🛣️ FiberPHP 路由器 —— 属性路由声明，支持中间件管道、控制器依赖注入、路由缓存、RESTful 约定。 |
| 2026-11-22 15:41:16 | [himelali/urlkit](https://www.nuget.org/packages/himelali%2Furlkit) | v1.0.0 | Md. Himel Ali | A modern, powerful and framework-independent PHP URL management toolkit with St… |
| 2026-11-22 15:58:26 | [boctulus/simplerest-fine-grained-acl](https://www.nuget.org/packages/boctulus%2Fsimplerest-fine-grained-acl) | v1.0.0 | boctulus | Full equiped ACL for SimpleRest |
| 2026-11-22 16:04:14 | [boctulus/simplerest-basic-acl](https://www.nuget.org/packages/boctulus%2Fsimplerest-basic-acl) | v1.0.0 | boctulus | Basic ACL for SimpleRest |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
