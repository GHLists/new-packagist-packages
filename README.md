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

## Latest list — 2026-10-10 10:20 UTC

New packages created between 2026-10-10 09:20 UTC and 2026-10-10 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T10-20-22-322088Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 09:27:46 | [hyperf-apex/apidoc-apifox](https://www.nuget.org/packages/hyperf-apex%2Fapidoc-apifox) | v2.0.0 | lbg-sys | Apex Apifox native document export for WebSocket contracts (Hyperf) |
| 2026-10-10 09:33:02 | [puffinmail/module-lifecycle](https://www.nuget.org/packages/puffinmail%2Fmodule-lifecycle) | v1.1.1 |  | PuffinMail for Magento 2: syncs customers, newsletter subscribers, orders, aban… |
| 2026-10-10 09:33:51 | [phattarachai/files-backup-laravel](https://www.nuget.org/packages/phattarachai%2Ffiles-backup-laravel) | v0.1.1 | Phattarachai Chaimongkol | Incremental off-site backup of a Laravel app's content files (uploads, media li… |
| 2026-10-10 09:42:25 | [pulseline/jalali-events](https://www.nuget.org/packages/pulseline%2Fjalali-events) | v1.0.0 | Farzin Bidokhti | A Laravel package for Iranian Jalali calendar events, official holidays, date r… |
| 2026-10-10 09:56:26 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.5.1 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
