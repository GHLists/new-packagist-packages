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

## Latest list — 2026-11-23 04:21 UTC

New packages created between 2026-11-23 03:19 UTC and 2026-11-23 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T04-21-49-44263Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 03:22:35 | [fiberphp/orm](https://www.nuget.org/packages/fiberphp%2Form) | v0.1.0 | PangBin | 🏗️ FiberPHP ORM —— Active Record 模式，支持关联关系、预加载、属性转换、时间戳、查询作用域。 |
| 2026-11-23 03:29:24 | [fiberphp/skeleton](https://www.nuget.org/packages/fiberphp%2Fskeleton) | v0.1.0 | PangBin | 📦 FiberPHP 应用骨架 —— 开箱即用的项目模板，集成路由、控制器、配置、中间件，快速启动。 |
| 2026-11-23 03:41:00 | [edueevaristo/reforma-tributaria-api](https://www.nuget.org/packages/edueevaristo%2Freforma-tributaria-api) | v0.2.0 | Eduardo Evaristo | Biblioteca PHP open source para a Reforma Tributaria do Consumo (IBS, CBS e IS)… |
| 2026-11-23 03:58:03 | [mucan54/laravel-transforms-request-guard](https://www.nuget.org/packages/mucan54%2Flaravel-transforms-request-guard) | v1.0.0 | Muhammed Can Özdemir | Guards Laravel's global TrimStrings / ConvertEmptyStringsToNull middleware agai… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
