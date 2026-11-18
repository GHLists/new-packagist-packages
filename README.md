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

## Latest list — 2026-11-18 23:19 UTC

New packages created between 2026-11-18 22:22 UTC and 2026-11-18 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T23-19-38-972944Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 22:25:20 | [grupoclip/bcv-today](https://www.nuget.org/packages/grupoclip%2Fbcv-today) | v1.0.0 | Grupo Clip | Official PHP client for the BCV Today API: Banco Central de Venezuela (BCV) exc… |
| 2026-11-18 22:25:42 | [useflex/media-studio](https://www.nuget.org/packages/useflex%2Fmedia-studio) | v0.1.0 |  | Self-hosted media library for Laravel with workspace storage, optional AI and F… |
| 2026-11-18 22:55:45 | [esoul-cz/guidelines](https://www.nuget.org/packages/esoul-cz%2Fguidelines) | v0.1.0 |  | Layered, mergeable project guidelines for eSoul projects (Laravel, LSR, Astro)… |
| 2026-11-18 23:01:19 | [daika7ana/simple-collections](https://www.nuget.org/packages/daika7ana%2Fsimple-collections) | v1.0.0 |  | Dependency-free Collection and LazyCollection for PHP 8.3+. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
