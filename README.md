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

## Latest list — 2026-11-06 21:20 UTC

New packages created between 2026-11-06 20:21 UTC and 2026-11-06 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T21-20-43-029541Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 20:24:50 | [mltstephane/laravel-quality](https://www.nuget.org/packages/mltstephane%2Flaravel-quality) | v1.0.2 |  | Shared static analysis and architecture rules for Laravel projects: Larastan ba… |
| 2026-11-06 20:49:05 | [earlyforge/earlyforge-sdk](https://www.nuget.org/packages/earlyforge%2Fearlyforge-sdk) | v0.1.0 |  | PHP client for the EarlyForge Trends API (free Pulse mirror and paid full trend… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
