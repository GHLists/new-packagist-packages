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

## Latest list — 2026-10-03 10:19 UTC

New packages created between 2026-10-03 09:21 UTC and 2026-10-03 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T10-19-06-205656Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 09:43:37 | [tibor-src/xai-sdk-php](https://www.nuget.org/packages/tibor-src%2Fxai-sdk-php) | v0.2.1 |  | Unofficial PHP port of the experimental SpaceXAI TypeScript SDK (@xai-official/… |
| 2026-10-03 09:44:58 | [tilscn/laravel](https://www.nuget.org/packages/tilscn%2Flaravel) | 1.0.0 | tilscn | A Laravel package for various utilities and features. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
