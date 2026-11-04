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

## Latest list — 2026-11-04 10:20 UTC

New packages created between 2026-11-04 09:18 UTC and 2026-11-04 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T10-20-26-339865Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 09:27:04 | [vaersaagod/consentmate](https://www.nuget.org/packages/vaersaagod%2Fconsentmate) | 1.0.0 |  | No means no, mate! |
| 2026-11-04 09:29:49 | [rizalahmaddd/laravel-rawprint](https://www.nuget.org/packages/rizalahmaddd%2Flaravel-rawprint) | v1.0.0 | rizalahmaddd | Print RAW ESC/P, ESC/POS and ZPL data from Laravel to RawPrint Agent without a… |
| 2026-11-04 09:40:07 | [ehundu/andamio-curriculum](https://www.nuget.org/packages/ehundu%2Fandamio-curriculum) | v1.0.0 |  | Un currículum hecho con Ehundu: tus datos en un solo fichero y, de ellos, la we… |
| 2026-11-04 09:40:07 | [oleksyuk/laravel-gleif-sdk](https://www.nuget.org/packages/oleksyuk%2Flaravel-gleif-sdk) | v0.1.0 | Maks Oleksyuk | Laravel SDK for the GLEIF LEI API, built on Saloon |
| 2026-11-04 09:46:28 | [deko/codec-decodec](https://www.nuget.org/packages/deko%2Fcodec-decodec) | v0.1.1 | deko | Library of symmetric encryption algorithms |
| 2026-11-04 09:54:01 | [watcher-php/laravel](https://www.nuget.org/packages/watcher-php%2Flaravel) | v0.1.2 |  | Security intelligence and protection layer for Laravel applications: static ana… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
