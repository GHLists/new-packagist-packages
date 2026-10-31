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

## Latest list — 2026-10-31 23:19 UTC

New packages created between 2026-10-31 22:19 UTC and 2026-10-31 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T23-19-50-688864Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 22:52:06 | [sushidev/php-pdf-concater](https://www.nuget.org/packages/sushidev%2Fphp-pdf-concater) | v0.1.0 | Sushi Dev GmbH | Merge PDFs from PHP with a fast Rust engine. |
| 2026-10-31 23:19:05 | [phasync/canvas](https://www.nuget.org/packages/phasync%2Fcanvas) | v0.1.0 | Frode Børli | The browser's 2D canvas API for PHP, over GD or Imagick |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
