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

## Latest list — 2026-10-20 23:19 UTC

New packages created between 2026-10-20 22:19 UTC and 2026-10-20 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T23-19-38-303369Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 22:24:21 | [yousef-aman/laravel-feedback-board](https://www.nuget.org/packages/yousef-aman%2Flaravel-feedback-board) | v1.0.1 | Yousef Aman | Self-hosted in-app feedback board for Laravel — clients report, developers reso… |
| 2026-10-20 22:32:44 | [ornio/filament-decorated-column](https://www.nuget.org/packages/ornio%2Ffilament-decorated-column) | v1.0.0 | Flamur Mavraj | Badge and icon decorations before or after the text of Filament table columns a… |
| 2026-10-20 22:35:37 | [bluedot-bd/sanity-check](https://www.nuget.org/packages/bluedot-bd%2Fsanity-check) | v1.0.0 | Bluedot Technology Ltd. | Malicious payload filter and security posture checks for Laravel applications. |
| 2026-10-20 22:42:09 | [mnd/dm-platform-client](https://www.nuget.org/packages/mnd%2Fdm-platform-client) | v1.0.0 |  | PHP client of Drift Manager Platform API |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
