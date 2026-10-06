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

## Latest list — 2026-10-06 05:21 UTC

New packages created between 2026-10-06 04:19 UTC and 2026-10-06 05:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T05-21-52-065846Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 04:32:15 | [mahmoudtr/snowflake-for-laravel](https://www.nuget.org/packages/mahmoudtr%2Fsnowflake-for-laravel) | v1.0.0 | Mahmoud Mahmoud | Distributed, time-sortable 64-bit Snowflake IDs for Laravel with Redis coordina… |
| 2026-10-06 04:52:17 | [envless/env](https://www.nuget.org/packages/envless%2Fenv) | v0.0.1 | Envless | The Envless runtime for PHP. Loads your environment from Envless when your app… |
| 2026-10-06 04:56:01 | [risqid/laravel-attendance-engine](https://www.nuget.org/packages/risqid%2Flaravel-attendance-engine) | v1.0.0 |  | Reusable Laravel attendance engine with stateless dynamic QR challenges. |
| 2026-10-06 05:11:12 | [unwahas/error-managements](https://www.nuget.org/packages/unwahas%2Ferror-managements) | v1.0.2 | Brian | Error logging and protected error-log API for Laravel applications |
| 2026-10-06 05:16:26 | [languaojs/zap](https://www.nuget.org/packages/languaojs%2Fzap) | 1.0.0 | Zainurrahman | A mini, lightweight, secure PHP framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
