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

## Latest list — 2026-10-27 03:21 UTC

New packages created between 2026-10-27 02:20 UTC and 2026-10-27 03:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T03-21-32-178696Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 02:39:15 | [naufalamr17/sivera-reporter](https://www.nuget.org/packages/naufalamr17%2Fsivera-reporter) | v0.1.1 |  | Fail-safe Laravel exception reporter for SIVERA |
| 2026-10-27 02:50:35 | [artygrand/pdfplumber-php](https://www.nuget.org/packages/artygrand%2Fpdfplumber-php) | 0.11.10 | ArtyGrand | Pure PHP port of pdfplumber: characters with coordinates, words, page text, tex… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
