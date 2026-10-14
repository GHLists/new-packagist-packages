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

## Latest list — 2026-10-14 01:22 UTC

New packages created between 2026-10-14 00:22 UTC and 2026-10-14 01:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T01-22-46-269317Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 00:41:44 | [mykholy/laravel-leakproof](https://www.nuget.org/packages/mykholy%2Flaravel-leakproof) | v1.0.1 | Ahmed Elkholy | Catch sensitive data leaking into Laravel JSON API responses before deployment. |
| 2026-10-14 01:09:25 | [jeffersongoncalves/laravel-cnpj](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-cnpj) | 1.0.0 | Jefferson Gonçalves | A simple and efficient Laravel package for querying Brazilian company registrat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
