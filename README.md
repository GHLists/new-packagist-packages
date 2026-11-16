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

## Latest list — 2026-11-16 21:19 UTC

New packages created between 2026-11-16 20:20 UTC and 2026-11-16 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T21-19-02-036927Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 20:34:55 | [adminphp-cms/core](https://www.nuget.org/packages/adminphp-cms%2Fcore) | v0.1.0 | Greg Marineau | A content management admin for Laravel, inspired by Twill |
| 2026-11-16 20:54:32 | [vusys/zefram](https://www.nuget.org/packages/vusys%2Fzefram) | v0.1.0 | Bryan | Skip PHPUnit tests whose executed code hasn't changed since they last passed. F… |
| 2026-11-16 21:03:30 | [mertaydin/laravel-composer-monitor](https://www.nuget.org/packages/mertaydin%2Flaravel-composer-monitor) | v0.1.6 |  | A Laravel dashboard for Composer dependency health, outdated packages, security… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
