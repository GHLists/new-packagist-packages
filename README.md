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

## Latest list — 2026-10-30 08:19 UTC

New packages created between 2026-10-30 07:20 UTC and 2026-10-30 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T08-19-25-246087Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 07:27:22 | [panda-men/think-throttle](https://www.nuget.org/packages/panda-men%2Fthink-throttle) | v0.1.0 |  | Atomic Redis Lua rate limiting for ThinkPHP 8 and PHP 8.2+ |
| 2026-10-30 07:53:14 | [laraveladmin/think-scout](https://www.nuget.org/packages/laraveladmin%2Fthink-scout) | v1.0.1 |  | Laravel Scout style full-text search for ThinkPHP ORM, with MySQL, PostgreSQL,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
