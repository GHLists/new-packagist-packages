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

## Latest list — 2026-10-12 23:19 UTC

New packages created between 2026-10-12 22:19 UTC and 2026-10-12 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T23-19-22-428785Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 22:30:12 | [julioserpone/gig-economics](https://www.nuget.org/packages/julioserpone%2Fgig-economics) | v1.0.0 | Julio Serpone | Platform-agnostic, decoupled PHP library to measure fuel efficiency and the rea… |
| 2026-10-12 22:31:22 | [wilycode/database-query](https://www.nuget.org/packages/wilycode%2Fdatabase-query) | v0.1.0 | Simon Piter | Lightweight SQL query builder, canonical compiled queries, and driver binding c… |
| 2026-10-12 22:58:55 | [treehousetim/waffle](https://www.nuget.org/packages/treehousetim%2Fwaffle) | v0.1.0 | Tim Gallagher | Waffle Application Framework For Lazy Engineers: a test-first starting point fo… |
| 2026-10-12 23:01:16 | [wilycode/database-driver-pdo](https://www.nuget.org/packages/wilycode%2Fdatabase-driver-pdo) | v0.1.0 | Simon Piter | PDO database driver implementing WilyCode database contracts, with a query para… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
