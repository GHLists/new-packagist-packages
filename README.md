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

## Latest list — 2026-10-26 05:18 UTC

New packages created between 2026-10-26 04:19 UTC and 2026-10-26 05:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T05-18-46-023734Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 04:34:49 | [siberfx/google-indexing](https://www.nuget.org/packages/siberfx%2Fgoogle-indexing) | 1.0.1 | Selim Görmüş | Notify Google (Indexing API + Search Console sitemaps) and IndexNow search engi… |
| 2026-10-26 04:59:58 | [rafiquljakir/fynoverify](https://www.nuget.org/packages/rafiquljakir%2Ffynoverify) | v0.1.0 | Rafiqul Jakir | Laravel-first API and authorization regression-testing companion: inventories r… |
| 2026-10-26 05:01:52 | [happyqu/laravel-admin](https://www.nuget.org/packages/happyqu%2Flaravel-admin) | v2.0.0 |  | Laravel Admin with customized frontend, global navigation and iframe tabs |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
