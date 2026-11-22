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

## Latest list — 2026-11-22 15:18 UTC

New packages created between 2026-11-22 14:20 UTC and 2026-11-22 15:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T15-18-48-323335Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 14:34:23 | [freebirds/apptagg-shop](https://www.nuget.org/packages/freebirds%2Fapptagg-shop) | v1.0.0 |  | Sell a Laravel shop's products in the Apptagg app: product sync, order import a… |
| 2026-11-22 14:36:10 | [fiberphp/cache](https://www.nuget.org/packages/fiberphp%2Fcache) | v0.1.0 | PangBin | ⚡ PSR-16 缓存组件 —— Redis store（键前缀隔离、TTL 归一、NX 抢占）与多 store 静态门面。 |
| 2026-11-22 14:46:23 | [nakanoaas/uuid58](https://www.nuget.org/packages/nakanoaas%2Fuuid58) | v0.1.2 |  | Shorten UUIDs to 22-character Base58 strings, and back. URL-safe, order-preserv… |
| 2026-11-22 14:50:32 | [luany/pt](https://www.nuget.org/packages/luany%2Fpt) | v1.0.0 | António Ambrósio Ngola | Luany em Português — a API do framework Luany em português: Modelo, Consulta, E… |
| 2026-11-22 15:01:49 | [fiberphp/framework](https://www.nuget.org/packages/fiberphp%2Fframework) | v0.1.0 | PangBin | 🚀 FiberPHP 框架核心 —— 应用生命周期编排、容器、配置、日志、控制台 CLI、环境变量、包发现、文件热重载与内存监控。 |
| 2026-11-22 15:04:07 | [wsrv/client](https://www.nuget.org/packages/wsrv%2Fclient) | v0.1.0-rc.1 |  | PHP client for the wsrvd WebSocket sidecar (IPC protocol v0) and an embedded se… |
| 2026-11-22 15:09:30 | [daun/statamic-tree-sync](https://www.nuget.org/packages/daun%2Fstatamic-tree-sync) | 1.0.0 | Philipp Daun | Keep the trees of collections and navigations in sync across Statamic sites |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
