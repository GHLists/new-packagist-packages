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

## Latest list — 2026-11-28 02:21 UTC

New packages created between 2026-11-28 01:19 UTC and 2026-11-28 02:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T02-21-20-957792Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 01:21:03 | [szgyds/gy-cron](https://www.nuget.org/packages/szgyds%2Fgy-cron) | v1.0.0 | szgyds | Hyperf 2.2 / 3.1 跨版本分布式定时任务组件：Scheduler 主动调度，Worker 注解声明任务，JSON-RPC 同步执行。 |
| 2026-11-28 01:28:08 | [cipi/cache](https://www.nuget.org/packages/cipi%2Fcache) | 1.0.0 |  | Purge pages of Cipi's nginx page cache from any PHP app — by path, prefix, URL… |
| 2026-11-28 02:09:38 | [denetorus/galaxy-logging](https://www.nuget.org/packages/denetorus%2Fgalaxy-logging) | v0.1.0 |  | Standalone structured logging with optional GalaxyApplication lifecycle stages. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
