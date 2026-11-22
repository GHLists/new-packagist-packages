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

## Latest list — 2026-11-22 14:20 UTC

New packages created between 2026-11-22 13:20 UTC and 2026-11-22 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T14-20-42-891309Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 13:26:25 | [fiberphp/helper](https://www.nuget.org/packages/fiberphp%2Fhelper) | v0.1.0 | PangBin | 🧰 FiberPHP 通用工具集 —— Arr / Str / Collection 与全局助手函数。 |
| 2026-11-22 13:30:50 | [fiberphp/event](https://www.nuget.org/packages/fiberphp%2Fevent) | v0.1.0 | PangBin | 📡 FiberPHP 事件调度器 —— PSR-14 标准实现（EventDispatcher + ListenerProvider）。 |
| 2026-11-22 13:36:19 | [daryl-peterson/librenms-device-path](https://www.nuget.org/packages/daryl-peterson%2Flibrenms-device-path) | v0.0.1-alpha | daryl-peterson | LibreNMS Plugin for showing device path under the device view |
| 2026-11-22 13:43:25 | [fiberphp/validate](https://www.nuget.org/packages/fiberphp%2Fvalidate) | v0.1.0 | PangBin | ✅ FiberPHP 数据验证 —— 多规则链式验证，支持内置规则与自定义扩展。 |
| 2026-11-22 13:45:36 | [tmonier/sylius-platform-health-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-platform-health-plugin) | v0.1.0 | Thibaut Monier | Platform health for Sylius 2: a probe contract that integrators implement in a… |
| 2026-11-22 13:51:47 | [nowo-tech/report-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Freport-kit-bundle) | v0.1.0 | Héctor Franco Aceituno; Nowo.… | Reports and scheduled exports for Symfony: report types with parameter schemas,… |
| 2026-11-22 14:05:36 | [fiberphp/console](https://www.nuget.org/packages/fiberphp%2Fconsole) | v0.1.0 | PangBin | ⌨️ FiberPHP 控制台引擎 —— 命令注册与分发、argv 解析、ANSI 输出格式化、交互问答与表格输出。 |
| 2026-11-22 14:13:33 | [fiberphp/exception](https://www.nuget.org/packages/fiberphp%2Fexception) | v0.1.0 | PangBin | 🛡️ FiberPHP 异常处理 —— ExceptionHandler 接口、框架异常基类、默认 Handler 实现，支持 HTTP/Console/RP… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
