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

## Latest list — 2026-11-24 04:21 UTC

New packages created between 2026-11-24 03:18 UTC and 2026-11-24 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T04-21-47-290606Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 03:23:32 | [lucasferro0/boleto-kit](https://www.nuget.org/packages/lucasferro0%2Fboleto-kit) | 0.1.0 | Lucas Ferro | Biblioteca PHP para validação e conversão entre código de barras e linha digitá… |
| 2026-11-24 03:37:05 | [klsoft/yii3-doctrine-app](https://www.nuget.org/packages/klsoft%2Fyii3-doctrine-app) | 1.0.0 |  | A Yii 3 web application template that supports the Doctrine ORM |
| 2026-11-24 03:37:45 | [fiberphp/queue](https://www.nuget.org/packages/fiberphp%2Fqueue) | v0.1.0 | PangBin | 📨 FiberPHP 队列核心 —— 契约与管理器，驱动策略模式，支持生产者/消费者模型、重试/死信策略、链路追踪传播。 |
| 2026-11-24 03:40:34 | [klsoft/yii3-cms](https://www.nuget.org/packages/klsoft%2Fyii3-cms) | 1.0.0 |  | A content management system based on the Yii 3 framework and uses the Doctrine… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
