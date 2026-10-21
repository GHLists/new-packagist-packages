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

## Latest list — 2026-10-21 02:19 UTC

New packages created between 2026-10-21 01:21 UTC and 2026-10-21 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T02-19-47-821427Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 01:28:19 | [putuwahyu29/backup-bridge](https://www.nuget.org/packages/putuwahyu29%2Fbackup-bridge) | v1.0.1 | Putu Wahyu | A secure bridge, visual control dashboard, and multi-database backup agent for… |
| 2026-10-21 01:34:43 | [wojt-janowski/laravel-glitchtip](https://www.nuget.org/packages/wojt-janowski%2Flaravel-glitchtip) | v1.0.0-RC2 | Wojt Janowski | A typed Laravel client for the GlitchTip error-tracking API. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
