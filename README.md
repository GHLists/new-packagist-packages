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

## Latest list — 2026-11-27 08:21 UTC

New packages created between 2026-11-27 07:20 UTC and 2026-11-27 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T08-21-23-609588Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 07:28:45 | [developerawam/wire-media](https://www.nuget.org/packages/developerawam%2Fwire-media) | v1.0.0 | developerawam | Premium Livewire media upload & image editor for Laravel 12. Upload, crop, zoom… |
| 2026-11-27 07:34:38 | [masmerise/kbo-public-search-php-sdk](https://www.nuget.org/packages/masmerise%2Fkbo-public-search-php-sdk) | v1.0.0 | Muhammed Sari | An unofficial PHP SDK for accessing the KBO/BCE Public Search web service. |
| 2026-11-27 07:46:42 | [masmerise/kbo-public-search-for-laravel](https://www.nuget.org/packages/masmerise%2Fkbo-public-search-for-laravel) | 1.0.0 | Muhammed Sarı | Laravel framework adapter for the KBO Public Search SDK. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
