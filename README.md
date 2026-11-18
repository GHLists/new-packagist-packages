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

## Latest list — 2026-11-18 18:21 UTC

New packages created between 2026-11-18 17:19 UTC and 2026-11-18 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T18-21-10-305391Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 17:40:19 | [hrabosh/ema-upd-client](https://www.nuget.org/packages/hrabosh%2Fema-upd-client) | 0.1.0 |  | Framework-independent PHP client for the EMA Union Product Database for veterin… |
| 2026-11-18 17:46:08 | [e98/laravel-youtrack](https://www.nuget.org/packages/e98%2Flaravel-youtrack) | v0.1.0 |  | Laravel wrapper for the JetBrains YouTrack REST API: create issues, read status… |
| 2026-11-18 18:07:11 | [amrachraf6699/wtf-happened](https://www.nuget.org/packages/amrachraf6699%2Fwtf-happened) | v1.0.1 |  | A Git-first Laravel catch-up command with optional AI summaries. |
| 2026-11-18 18:07:38 | [bannerstop/sonar-php](https://www.nuget.org/packages/bannerstop%2Fsonar-php) | v1.0.0 | bannerstop GmbH | Pulse client for sonar: report that a PHP job ran, with a short timeout, an on-… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
