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

## Latest list — 2026-11-15 12:21 UTC

New packages created between 2026-11-15 11:20 UTC and 2026-11-15 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T12-21-23-618332Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 11:25:25 | [suprim/speedy](https://www.nuget.org/packages/suprim%2Fspeedy) | 1.0.0 | suprim | Speedy Cache: full-page caching for Craft CMS that keeps your database clean, w… |
| 2026-11-15 11:28:32 | [wickedone/infection-mate-extension](https://www.nuget.org/packages/wickedone%2Finfection-mate-extension) | 0.1.0 | wicliff wolda | infection extension for symfony mate |
| 2026-11-15 11:42:17 | [laravelazier/laravelazier](https://www.nuget.org/packages/laravelazier%2Flaravelazier) | 2.1.0 | Laravelazier Contributors | Lightweight Laravel package for generating PDF and Excel files with minimal set… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
