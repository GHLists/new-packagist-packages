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

## Latest list — 2026-11-21 20:22 UTC

New packages created between 2026-11-21 19:19 UTC and 2026-11-21 20:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T20-22-03-400091Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 19:37:00 | [yetidevworks/yetipdf-write](https://www.nuget.org/packages/yetidevworks%2Fyetipdf-write) | 0.1.0 | Yetidevworks | The fastest PDF generation for PHP: pure PHP, no dependencies, with a layout mo… |
| 2026-11-21 19:56:22 | [steffenr/dsv-php](https://www.nuget.org/packages/steffenr%2Fdsv-php) | v0.1.0 | Steffen Rühlmann; Philipp Sch… | PHP library for parsing, validating and writing DSV files (DSV7 / DSV8) used in… |
| 2026-11-21 20:01:42 | [onysko/octane-health](https://www.nuget.org/packages/onysko%2Foctane-health) | 1.0.0 | Pavlo Onysko | Health checks for Laravel Octane in production: per-worker memory growth with r… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
