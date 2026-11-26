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

## Latest list — 2026-11-26 06:21 UTC

New packages created between 2026-11-26 05:19 UTC and 2026-11-26 06:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T06-21-09-228972Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 05:30:57 | [smart145/html](https://www.nuget.org/packages/smart145%2Fhtml) | v6.5.0 | Adam Engebretson; Taylor Otwe… | HTML and Form Builders for the Laravel Framework (Smart 145 fork of the abandon… |
| 2026-11-26 05:51:56 | [diepxuan/laravel-catalog](https://www.nuget.org/packages/diepxuan%2Flaravel-catalog) | 2.9.1 | Tran Ngoc Duc | Catalog package for DXPanel |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
