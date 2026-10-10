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

## Latest list — 2026-10-10 22:21 UTC

New packages created between 2026-10-10 21:19 UTC and 2026-10-10 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T22-21-09-446775Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 21:34:59 | [nanayawkumi/nyk-db-sync](https://www.nuget.org/packages/nanayawkumi%2Fnyk-db-sync) | 1.0.0 | Nana Yaw Kumi | Bidirectional MySQL and PostgreSQL schema translation, row sync, dual-write, an… |
| 2026-10-10 21:39:09 | [invisnet/phpstan-compose-shapes](https://www.nuget.org/packages/invisnet%2Fphpstan-compose-shapes) | 1.0.0 | Charles Lecklider | PHPStan extension providing compose-shapes<A, B, ...> to merge sealed array sha… |
| 2026-10-10 21:55:35 | [magicoli/kick-inside](https://www.nuget.org/packages/magicoli%2Fkick-inside) | 0.1.0 | Olivier van Helden | Pure PHP UPnP IGD port mapping (miniupnpc-like) without CLI dependencies. |
| 2026-10-10 21:56:17 | [shahriar/laravel-filemanager](https://www.nuget.org/packages/shahriar%2Flaravel-filemanager) | v1.0.0 |  | Project-scoped Laravel file manager: no storage:link, folders, password-protect… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
