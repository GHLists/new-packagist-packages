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

## Latest list — 2026-11-08 12:20 UTC

New packages created between 2026-11-08 11:21 UTC and 2026-11-08 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T12-20-11-746863Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 11:33:31 | [cpsit/import-export-core](https://www.nuget.org/packages/cpsit%2Fimport-export-core) | 0.1.0 | Dirk Wenzel | Core library for import/export functionality |
| 2026-11-08 11:41:58 | [pdir/contao-workmate-agent-bundle](https://www.nuget.org/packages/pdir%2Fcontao-workmate-agent-bundle) | v1.0.1 | pdir GmbH | Workmate agent for Contao projects: commits the database backup and composer.lo… |
| 2026-11-08 12:18:05 | [ikhbarnuridev/filament-mega-menu](https://www.nuget.org/packages/ikhbarnuridev%2Ffilament-mega-menu) | v1.0.0 | ikhbarnuridev | Topbar navigation groups that overflow onto a second row become a full-width me… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
