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

## Latest list — 2026-11-15 23:21 UTC

New packages created between 2026-11-15 22:21 UTC and 2026-11-15 23:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T23-21-43-741213Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 22:51:58 | [webong/proxy-laravel](https://www.nuget.org/packages/webong%2Fproxy-laravel) | 0.4.0 |  | Laravel registry persistence, migrations and Spatie webhook integration for Pro… |
| 2026-11-15 22:52:38 | [elliottlawson/source-laravel](https://www.nuget.org/packages/elliottlawson%2Fsource-laravel) | v0.2.0 |  | Laravel filesystem driver for source, the Git-backed file store. |
| 2026-11-15 23:05:23 | [juf/doctrine-import-bundle](https://www.nuget.org/packages/juf%2Fdoctrine-import-bundle) | v0.1.0 | JuF | Generate Doctrine ORM entities and repositories from an existing database. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
