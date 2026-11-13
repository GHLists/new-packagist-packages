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

## Latest list — 2026-11-13 06:21 UTC

New packages created between 2026-11-13 05:21 UTC and 2026-11-13 06:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T06-21-39-689706Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 06:10:24 | [atannex/desk-editor](https://www.nuget.org/packages/atannex%2Fdesk-editor) | v1.0.0 | Atannex Enterprise | A premium, first-class rich text editor for Laravel: Blade & Livewire component… |
| 2026-11-13 06:17:12 | [mrsunset9x/vietqr-php](https://www.nuget.org/packages/mrsunset9x%2Fvietqr-php) | v0.1.0 |  | Small, offline VietQR (NAPAS247) payload generator and strict parser for PHP, w… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
