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

## Latest list — 2026-10-16 03:21 UTC

New packages created between 2026-10-16 02:20 UTC and 2026-10-16 03:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T03-21-51-082062Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 02:35:03 | [phatnt93/php-upload-helper](https://www.nuget.org/packages/phatnt93%2Fphp-upload-helper) | v1.0.0 | Phat Nguyen | A modern, secure and fluent PHP file upload and image manipulation library with… |
| 2026-10-16 02:54:04 | [brewphp/brewphp](https://www.nuget.org/packages/brewphp%2Fbrewphp) | v1.0.0 |  | A small, Django-inspired PHP framework: easy to learn, readable core, zero runt… |
| 2026-10-16 02:56:03 | [brewphp/skeleton](https://www.nuget.org/packages/brewphp%2Fskeleton) | v1.0.0 |  | Starter project for BrewPHP, the small Django-inspired PHP framework. |
| 2026-10-16 02:57:50 | [anun333/oe-module-clinic-forms](https://www.nuget.org/packages/anun333%2Foe-module-clinic-forms) | v0.1.0 | anun333 | Printable clinic paperwork for OpenEMR: consents, releases, referral letters an… |
| 2026-10-16 02:59:02 | [kylin987/orm-redis-cache](https://www.nuget.org/packages/kylin987%2Form-redis-cache) | v1.0.0 |  | Fixed-record Redis cache with mutual invalidation for Eloquent, Webman ThinkORM… |
| 2026-10-16 03:08:00 | [calmify/laravel](https://www.nuget.org/packages/calmify%2Flaravel) | v1.0.0 |  | Receive articles from Calmify on a Laravel website: one install command, one pa… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
