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

## Latest list — 2026-11-01 12:20 UTC

New packages created between 2026-11-01 11:20 UTC and 2026-11-01 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T12-20-43-400989Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 11:20:32 | [nowo-tech/messenger-monitor-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fmessenger-monitor-kit-bundle) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Symfony Messenger monitoring on top of zenstruck/messenger-monitor-bundle: runt… |
| 2026-11-01 11:24:06 | [spkm/aruba-central](https://www.nuget.org/packages/spkm%2Faruba-central) | v1.0.0 | Simon Mitchell | Integrate with the Aruba Central APIs, classic and new, using SaloonPHP |
| 2026-11-01 11:25:13 | [dongasai/dbcheck](https://www.nuget.org/packages/dongasai%2Fdbcheck) | 1.0.2 |  | 数据库结构/数据自检与修复框架（按表三类检查：表结构、固定数据、字段明细） |
| 2026-11-01 11:56:31 | [abdur-rahaman/laravel-seo](https://www.nuget.org/packages/abdur-rahaman%2Flaravel-seo) | v1.1.0 | Abdurrahaman | A comprehensive SEO management package for Laravel applications, inspired by Yo… |
| 2026-11-01 12:01:16 | [hub-io/laravel-hubio-sync](https://www.nuget.org/packages/hub-io%2Flaravel-hubio-sync) | v0.1.0 | Hubio s.r.o.; Ján Hamrák | Backup, sharing and photo synchronization of Hubio NativePHP apps through Hubio… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
