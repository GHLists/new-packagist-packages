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

## Latest list — 2026-11-16 05:21 UTC

New packages created between 2026-11-16 04:21 UTC and 2026-11-16 05:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T05-21-45-289063Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 04:40:22 | [starbug/redis](https://www.nuget.org/packages/starbug%2Fredis) | v0.9.0 | Ali Gangji | Redis integration: Predis client and queue driver wiring. |
| 2026-11-16 05:05:34 | [youvision/think-store-chess](https://www.nuget.org/packages/youvision%2Fthink-store-chess) | v1.0 | indiboy-create; AI | ThinkPHP 8 中国象棋包：包内视图渲染、layui 静态资源路由与在线棋盘。 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
