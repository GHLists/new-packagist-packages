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

## Latest list — 2026-11-15 18:19 UTC

New packages created between 2026-11-15 17:19 UTC and 2026-11-15 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T18-19-40-36124Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 17:22:42 | [rah/rah_vinyl](https://www.nuget.org/packages/rah%2Frah_vinyl) | 0.1.0 | Jukka Svahn | Vinyl Cache based full-page cache integration for Textpattern CMS |
| 2026-11-15 17:31:22 | [polypheny/php-driver](https://www.nuget.org/packages/polypheny%2Fphp-driver) | v1.0.0 |  | PHP driver for Polypheny through the Prism interface |
| 2026-11-15 17:37:03 | [miraqceed/laravel-foundation](https://www.nuget.org/packages/miraqceed%2Flaravel-foundation) | v0.1.2 | MIRAQCEED | どの Laravel のアプリにも要る部品（テストの守り・CSV・ログインのロック・CSP・見張り） |
| 2026-11-15 17:40:22 | [ctsoftwarellc/laravel-job-throttle](https://www.nuget.org/packages/ctsoftwarellc%2Flaravel-job-throttle) | v1.0.0 | CT Software LLC | Redis rate limiting for Laravel queued jobs that call outside APIs: exact GCRA… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
