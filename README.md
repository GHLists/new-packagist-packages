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

## Latest list — 2026-10-17 06:18 UTC

New packages created between 2026-10-17 05:19 UTC and 2026-10-17 06:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T06-18-58-677983Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 06:05:17 | [sameoldnick/laravel-open-observe](https://www.nuget.org/packages/sameoldnick%2Flaravel-open-observe) | v1.0.0 | Nick Hamnett | A Laravel package for integrating OpenObserve logging with your application. |
| 2026-10-17 06:12:44 | [pieceofcake2/report](https://www.nuget.org/packages/pieceofcake2%2Freport) | v1.0.0 |  | A4 PDF reports printed by the Chrome command line: a cover with the result, a l… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
