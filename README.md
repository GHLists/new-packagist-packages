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

## Latest list — 2026-11-24 07:20 UTC

New packages created between 2026-11-24 06:21 UTC and 2026-11-24 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T07-20-22-408866Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 06:21:46 | [ongudidan/laravel-payments-engine](https://www.nuget.org/packages/ongudidan%2Flaravel-payments-engine) | v1.0.1 | Ongudidan | Unified enterprise payment accounts, physical cash vault denominations, custome… |
| 2026-11-24 06:24:03 | [fiberphp/queue-rabbitmq](https://www.nuget.org/packages/fiberphp%2Fqueue-rabbitmq) | v0.1.0 | PangBin | 🐰 FiberPHP RabbitMQ 队列驱动 —— AMQP 协议实现，支持连接池、延迟消息、消息确认。 |
| 2026-11-24 07:04:28 | [psbits/gift-log](https://www.nuget.org/packages/psbits%2Fgift-log) | 0.1.0-alpha | Daniel Ablass | Keep a record of all the gifts you have received or given. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
