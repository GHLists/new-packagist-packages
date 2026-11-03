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

## Latest list — 2026-11-03 05:20 UTC

New packages created between 2026-11-03 04:21 UTC and 2026-11-03 05:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T05-20-44-887053Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 04:25:13 | [vtinnovations/file-inspector](https://www.nuget.org/packages/vtinnovations%2Ffile-inspector) | v1.0.1 | V&T Innovations Team | File Inspector Bundle. |
| 2026-11-03 04:54:04 | [decionis/php-client](https://www.nuget.org/packages/decionis%2Fphp-client) | v0.1.0 |  | PHP client for the Decionis execution authority: evaluate decisions, read Decis… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
