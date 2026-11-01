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

## Latest list — 2026-11-01 02:21 UTC

New packages created between 2026-11-01 01:18 UTC and 2026-11-01 02:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T02-21-11-39553Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 01:20:54 | [tru-laravel-club/blsc-guide](https://www.nuget.org/packages/tru-laravel-club%2Fblsc-guide) | v0.1.0 |  | A step-by-step contributor guide for the BIG Little Science Centre website. Ins… |
| 2026-11-01 01:53:25 | [wodzy/disposable-email](https://www.nuget.org/packages/wodzy%2Fdisposable-email) | v1.0.0 | Walid Oukaci | Lightweight, dependency-free PHP library that blocks disposable (throwaway) ema… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
