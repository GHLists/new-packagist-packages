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

## Latest list — 2026-11-28 04:19 UTC

New packages created between 2026-11-28 03:20 UTC and 2026-11-28 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T04-19-46-486977Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 03:28:22 | [jaizendra-netizen/saleshandy-smartlead-plan-quote](https://www.nuget.org/packages/jaizendra-netizen%2Fsaleshandy-smartlead-plan-quote) | v1.0.0 | Jainendra Ojha | PHP CLI that picks the cheapest Saleshandy plan beside the cheapest Smartlead p… |
| 2026-11-28 03:37:51 | [hotroso/reactphp-device-bridge](https://www.nuget.org/packages/hotroso%2Freactphp-device-bridge) | v1.0.0 | Hotroso | Asynchronous, event-driven TCP socket and HTTP device bridge library built on R… |
| 2026-11-28 04:04:39 | [szgyds/gy-cron](https://www.nuget.org/packages/szgyds%2Fgy-cron) | v1.0.3 | szgyds | Hyperf 2.2 / 3.1 / 3.2 跨版本分布式定时任务组件：Scheduler 主动调度，Worker 注解声明任务，JSON-RPC 同步执行。 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
