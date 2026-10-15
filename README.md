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

## Latest list — 2026-10-15 21:19 UTC

New packages created between 2026-10-15 20:21 UTC and 2026-10-15 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T21-19-24-500859Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 20:31:37 | [yanfishel/atarcms](https://www.nuget.org/packages/yanfishel%2Fatarcms) | v0.1.0 |  | AtarCMS site skeleton |
| 2026-10-15 20:31:39 | [yanfishel/atarcms-core](https://www.nuget.org/packages/yanfishel%2Fatarcms-core) | v0.1.0 |  | Lightweight content management system |
| 2026-10-15 20:46:47 | [tomac1/rockadmin](https://www.nuget.org/packages/tomac1%2Frockadmin) | v0.1.0 | Tomas Hruby | A dependency-free PHP administration SDK. Mount it on a URL, describe your page… |
| 2026-10-15 20:50:42 | [amarenkov/laravel-mutable-content-shop](https://www.nuget.org/packages/amarenkov%2Flaravel-mutable-content-shop) | v0.1.0 | Alexey Marenkov | Shop domain for laravel-mutable-content: carts of users and guests, orders with… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
