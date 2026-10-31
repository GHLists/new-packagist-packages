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

## Latest list — 2026-10-31 16:18 UTC

New packages created between 2026-10-31 15:21 UTC and 2026-10-31 16:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T16-18-59-399926Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 15:21:58 | [siteation/magento2-commerce365-debugbar](https://www.nuget.org/packages/siteation%2Fmagento2-commerce365-debugbar) | 1.0.1 | Siteation | Commerce365 section for Siteation_DebugBar: customer prices, Hub and Business C… |
| 2026-10-31 15:29:06 | [kinetis/queue-failed-jobs](https://www.nuget.org/packages/kinetis%2Fqueue-failed-jobs) | v1.0.0 | Alon Noy | Retained failed jobs for kinetis/queue — every job the worker gives up on is re… |
| 2026-10-31 15:29:36 | [basekit-laravel/basekit-laravel-media](https://www.nuget.org/packages/basekit-laravel%2Fbasekit-laravel-media) | v1.0.0 | Gergő Tar | Media library for Laravel: metadata for files on a filesystem disk, a folder hi… |
| 2026-10-31 15:32:19 | [semitexa/notifications](https://www.nuget.org/packages/semitexa%2Fnotifications) | 2026.10.31.0849 | Semitexa | Semitexa Notifications - one notification, many channels (mail, database inbox,… |
| 2026-10-31 15:37:37 | [zivalix/zivalix](https://www.nuget.org/packages/zivalix%2Fzivalix) | v0.1.0 | ZIVALIX Founders | The official reserved package for ZIVALIX Agency to prevent dependency confusio… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
