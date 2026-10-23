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

## Latest list — 2026-10-23 20:19 UTC

New packages created between 2026-10-23 19:20 UTC and 2026-10-23 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T20-19-13-467176Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 19:22:25 | [postalportal/zip4](https://www.nuget.org/packages/postalportal%2Fzip4) | 0.0.1 |  | Match and standardize US addresses against a local USPS ZIP+4 SQLite database |
| 2026-10-23 19:35:16 | [bepago/sdk](https://www.nuget.org/packages/bepago%2Fsdk) | v1.0.0 | bePago | SDK oficial de bePago para PHP (7.4+, sin dependencias) |
| 2026-10-23 19:41:54 | [sunasty/color-math](https://www.nuget.org/packages/sunasty%2Fcolor-math) | v1.0.0 | Bastien Sulyan | Zero-dependency sRGB, OKLCH, and WCAG 2.1 contrast calculation in PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
