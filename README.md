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

## Latest list — 2026-10-23 21:21 UTC

New packages created between 2026-10-23 20:19 UTC and 2026-10-23 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T21-21-27-853669Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 20:33:25 | [prontuno/prontuno-laravel](https://www.nuget.org/packages/prontuno%2Fprontuno-laravel) | v0.1.0 | Prontuno Team | The official Laravel integration for Prontuno: API client, mail transport, and… |
| 2026-10-23 20:36:41 | [jalaljaberi/negarity-color](https://www.nuget.org/packages/jalaljaberi%2Fnegarity-color) | v1.0.0-beta1 | Jalal Jaberi | Negarity Color — a modern, extensible color manipulation library for PHP. |
| 2026-10-23 20:41:36 | [siberfx/laravel-risk-analyzer](https://www.nuget.org/packages/siberfx%2Flaravel-risk-analyzer) | v2.0.0 | Selim Görmüş | Security scanner for Laravel 12 & 13: AST taint analysis of your code, checks o… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
