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

## Latest list — 2026-11-22 11:19 UTC

New packages created between 2026-11-22 10:21 UTC and 2026-11-22 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T11-19-34-635895Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 10:28:50 | [ibexa/agent-platform-api](https://www.nuget.org/packages/ibexa%2Fagent-platform-api) | v1.0.0-beta4 | Ibexa R&D | PHP client for the Ibexa Agentic Marketing Platform REST API |
| 2026-11-22 10:31:42 | [fiberphp/container](https://www.nuget.org/packages/fiberphp%2Fcontainer) | v0.1.0 | PangBin | 🚀 FiberPHP IoC 服务容器 —— PSR-11 实现，支持绑定/单例/上下文绑定、延迟加载、构造参数自动装配与 #[Inject] 属性注入。 |
| 2026-11-22 10:40:36 | [contractlayer/econtract-laravel](https://www.nuget.org/packages/contractlayer%2Fecontract-laravel) | v0.1.2 |  | Laravel integration of eContract e-signatures: provider interface, webhook veri… |
| 2026-11-22 10:55:07 | [fiberphp/context](https://www.nuget.org/packages/fiberphp%2Fcontext) | v0.1.0 | PangBin | 🧵 FiberPHP 请求级上下文容器 —— 基于 Workerman Coroutine 上下文、Fiber 隔离、销毁回调（onDestroy）。 |
| 2026-11-22 11:09:51 | [fiberphp/manifest](https://www.nuget.org/packages/fiberphp%2Fmanifest) | v0.1.0 | PangBin | FiberPHP 包发现清单——扫描 vendor/composer/installed.json 的 extra.fiberphp 声明，汇总 middle… |
| 2026-11-22 11:09:53 | [fiberphp/pipeline](https://www.nuget.org/packages/fiberphp%2Fpipeline) | v0.1.0 | PangBin | 🔗 FiberPHP 洋葱模型管道构造器 —— 零依赖的中间件管线核心。 |
| 2026-11-22 11:09:55 | [fiberphp/provider](https://www.nuget.org/packages/fiberphp%2Fprovider) | v0.1.0 | PangBin | FiberPHP 服务提供者基类 —— register/boot/bootAfter 生命周期钩子、critical/network/bootTimeout… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
