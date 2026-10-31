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

## Latest list — 2026-10-31 11:18 UTC

New packages created between 2026-10-31 10:19 UTC and 2026-10-31 11:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T11-18-19-873342Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 10:24:41 | [wilbere/bagisto-bcv](https://www.nuget.org/packages/wilbere%2Fbagisto-bcv) | v1.0.0 | wilbere | Tasa BCV oficial automática, precio dual (USD/Bs.) y congelamiento por orden pa… |
| 2026-10-31 10:49:49 | [eamirgh/digipay-laravel](https://www.nuget.org/packages/eamirgh%2Fdigipay-laravel) | v1.0.0 | Amir Ghaffari | Production-grade scalable Digipay UPG integration for Laravel 11, 12, 13+ |
| 2026-10-31 10:59:56 | [mapo-89/laravel-nginx-proxy-manager-api](https://www.nuget.org/packages/mapo-89%2Flaravel-nginx-proxy-manager-api) | v1.0.0 | mapo-89 | Laravel API client for Nginx Proxy Manager |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
