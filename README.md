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

## Latest list — 2026-11-15 19:21 UTC

New packages created between 2026-11-15 18:19 UTC and 2026-11-15 19:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T19-21-41-635133Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 18:25:32 | [sce-urv/parcel-cat-sdk](https://www.nuget.org/packages/sce-urv%2Fparcel-cat-sdk) | 1.0.0 | David Domenech | A SDK to integrate with parcel-cat API |
| 2026-11-15 18:58:55 | [mikepultz/php-mysqlnd-tls](https://www.nuget.org/packages/mikepultz%2Fphp-mysqlnd-tls) | v1.0.0 | Mike Pultz | Turns on TLS for PHP's MySQL connections (mysqli and PDO, through mysqlnd) from… |
| 2026-11-15 19:08:15 | [youvision/think-store-example](https://www.nuget.org/packages/youvision%2Fthink-store-example) | v1.9 | indiboy-create; AI | ThinkPHP 8 示例包：包内视图渲染、layui 静态资源路由与随机抽诗接口。 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
