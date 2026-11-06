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

## Latest list — 2026-11-06 23:19 UTC

New packages created between 2026-11-06 22:20 UTC and 2026-11-06 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T23-19-27-85818Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 22:43:54 | [diephp/telegraph](https://www.nuget.org/packages/diephp%2Ftelegraph) | v2.0.1 | Fabio Ivona | Focused Laravel Telegram integration for Restsify notifications and bot callbac… |
| 2026-11-06 23:05:43 | [store-doc/laravel-storage-driver](https://www.nuget.org/packages/store-doc%2Flaravel-storage-driver) | v1.0.0 | Store-Doc Team | Laravel Storage Driver for Store-Doc S3-compatible storage service with complet… |
| 2026-11-06 23:09:17 | [vallic/domain-investors](https://www.nuget.org/packages/vallic%2Fdomain-investors) | 1.0.0 |  | Sell your own domain names from your own site: a Drupal Commerce starter for on… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
