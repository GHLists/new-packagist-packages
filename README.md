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

## Latest list — 2026-11-22 04:18 UTC

New packages created between 2026-11-22 03:19 UTC and 2026-11-22 04:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T04-18-44-876517Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 03:26:21 | [aliu-zhongzheng/laravel-compat](https://www.nuget.org/packages/aliu-zhongzheng%2Flaravel-compat) | v0.1.1 |  | Static compatibility audit for legacy Laravel/PHP projects: PHPCompatibility fi… |
| 2026-11-22 03:47:27 | [browshot-php/browshot](https://www.nuget.org/packages/browshot-php%2Fbrowshot) | v1.32.0 | Julien Sobrier | PHP library for Browshot API: take screenshots of any web page |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
