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

## Latest list — 2026-11-12 06:21 UTC

New packages created between 2026-11-12 05:21 UTC and 2026-11-12 06:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T06-21-57-955508Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 05:25:12 | [tinymvc/tinyqr](https://www.nuget.org/packages/tinymvc%2Ftinyqr) | v1.0.0 | Shahin Moyshan | Lightweight PHP QR code generator and decoder with PNG and SVG output. |
| 2026-11-12 05:48:44 | [letterncms/fathomline](https://www.nuget.org/packages/letterncms%2Ffathomline) | 0.2.0 |  | A survey office's site: WebGL fields, scroll choreography and client navigation… |
| 2026-11-12 06:10:36 | [akshaysmohite/filament-form-generator](https://www.nuget.org/packages/akshaysmohite%2Ffilament-form-generator) | v0.1.0 | Akshay | Visual drag-and-drop form schema builder and PHP code generator for Filament v3… |
| 2026-11-12 06:12:00 | [olivcode/form-guard](https://www.nuget.org/packages/olivcode%2Fform-guard) | v1.0.0 | Olivier Gaillot | Progressive abuse protection for PHP forms, with optional JavaScript signals. |
| 2026-11-12 06:12:05 | [olivcode/form-guard-laravel](https://www.nuget.org/packages/olivcode%2Fform-guard-laravel) | v1.0.0 |  | Laravel adapter for the Form Guard PHP form protection engine. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
