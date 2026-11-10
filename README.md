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

## Latest list — 2026-11-10 08:21 UTC

New packages created between 2026-11-10 07:20 UTC and 2026-11-10 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T08-21-39-091547Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 07:32:40 | [itmosoft/laravel-wishlist](https://www.nuget.org/packages/itmosoft%2Flaravel-wishlist) | v1.0.0 |  | Wishlist management for Laravel applications, supporting multiple wishlists, pr… |
| 2026-11-10 07:35:04 | [lgz2688/mongo-builder](https://www.nuget.org/packages/lgz2688%2Fmongo-builder) | v1.0.0 | lgz2688 | A chainable MongoDB builder with a MySQL-like API, pluggable ID generation and… |
| 2026-11-10 07:38:30 | [jojeringnax/airwallex-php-sdk](https://www.nuget.org/packages/jojeringnax%2Fairwallex-php-sdk) | v0.1.0 |  | Framework-independent Airwallex Billing and Payments SDK for PHP. |
| 2026-11-10 07:48:19 | [faisallbhr/laravel-tracelog](https://www.nuget.org/packages/faisallbhr%2Flaravel-tracelog) | v0.1.0 |  | Trace Eloquent model changes with contextual debug logs. |
| 2026-11-10 08:10:06 | [fingerly/fingerly-php](https://www.nuget.org/packages/fingerly%2Ffingerly-php) | v0.1.0 |  | Server-side Fingerly SDK: event reads, webhook verification and a same-origin p… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
