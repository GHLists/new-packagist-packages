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

## Latest list — 2026-10-18 02:18 UTC

New packages created between 2026-10-18 01:21 UTC and 2026-10-18 02:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T02-18-42-377771Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 01:28:34 | [jeffersongoncalves/laravel-report-url](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-report-url) | 1.0.0 | Jefferson Gonçalves | Temporary, signed, expiring download links for generated files in Laravel, with… |
| 2026-10-18 01:39:21 | [coopers98/mnemon](https://www.nuget.org/packages/coopers98%2Fmnemon) | v1.0.0 |  | A self-hosted second brain for AI agents: verbatim palace storage, a compiled w… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
