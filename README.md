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

## Latest list — 2026-11-11 02:20 UTC

New packages created between 2026-11-11 01:20 UTC and 2026-11-11 02:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T02-20-44-684722Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 01:26:10 | [holyat/filament-jp-postal](https://www.nuget.org/packages/holyat%2Ffilament-jp-postal) | v1.0.0 | Holyat | Japanese postal code (郵便番号) address auto-fill for Filament: a postal code input… |
| 2026-11-11 01:50:42 | [mossy2100/better-base64](https://www.nuget.org/packages/mossy2100%2Fbetter-base64) | v1.0.0 | Shaun Moss | Base64 encoding for PHP that preserves sort order, using HTML- and filename-saf… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
