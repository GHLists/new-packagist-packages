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

## Latest list — 2026-09-29 06:21 UTC

New packages created between 2026-09-29 05:21 UTC and 2026-09-29 06:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T06-21-17-779401Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 06:10:39 | [fundrik/coding-standard](https://www.nuget.org/packages/fundrik%2Fcoding-standard) | 0.2.0 | Denis Yanchevskiy | Custom PHP_CodeSniffer rules for Fundrik |
| 2026-09-29 06:11:21 | [socket-bridge/laravel-socketio](https://www.nuget.org/packages/socket-bridge%2Flaravel-socketio) | v0.1.0 |  | Reusable Laravel integration for authenticated Socket.IO events over Redis. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
