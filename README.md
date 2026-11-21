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

## Latest list — 2026-11-21 22:20 UTC

New packages created between 2026-11-21 21:19 UTC and 2026-11-21 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T22-20-03-808023Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 21:35:12 | [el-choco/repo-sync](https://www.nuget.org/packages/el-choco%2Frepo-sync) | v0.1.0-beta.1 | el-choco | Synchronize GitHub README files with Flarum posts and announce releases in exis… |
| 2026-11-21 21:47:25 | [daryl-peterson/librenms-device-backups](https://www.nuget.org/packages/daryl-peterson%2Flibrenms-device-backups) | v0.2.0-alpha | daryl-peterson | LibreNMS plugin for device backups |
| 2026-11-21 21:52:08 | [gavtaylor/hoveractions](https://www.nuget.org/packages/gavtaylor%2Fhoveractions) | v0.1.0 | Gavin Taylor | Outlook-style hover actions for Roundcube's Elastic message list: the date move… |
| 2026-11-21 22:06:07 | [nyoncode/laravel-pwa](https://www.nuget.org/packages/nyoncode%2Flaravel-pwa) | v1.0.0 | Ondřej Nyklíček | Production-grade PWA for Laravel: offline-first service worker with per-user ca… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
