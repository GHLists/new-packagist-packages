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

## Latest list — 2026-11-17 07:18 UTC

New packages created between 2026-11-17 06:19 UTC and 2026-11-17 07:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T07-18-36-927206Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 06:32:18 | [cable8mm/laravel-vite-s3](https://www.nuget.org/packages/cable8mm%2Flaravel-vite-s3) | v1.0.1 | Samgu Lee | Sync the Vite build output to an S3 (or any Flysystem) disk with one artisan co… |
| 2026-11-17 06:33:01 | [billionsend/billionsend-php](https://www.nuget.org/packages/billionsend%2Fbillionsend-php) | v0.1.1 | BillionSend | PHP SDK for the BillionSend email API |
| 2026-11-17 06:34:04 | [gsnugroho/laravel-rescue-audit](https://www.nuget.org/packages/gsnugroho%2Flaravel-rescue-audit) | v0.1.2 | Galih S. Nugroho | One-command health & security audit for existing Laravel apps. Generates an HTM… |
| 2026-11-17 06:56:01 | [starbug/impersonate](https://www.nuget.org/packages/starbug%2Fimpersonate) | v0.9.1 | Ali Gangji | Impersonate a user from the admin. |
| 2026-11-17 07:00:03 | [itmosoft/laravel-multitenancy](https://www.nuget.org/packages/itmosoft%2Flaravel-multitenancy) | v1.0.0 |  | Tenant resolution, request context, and shared-database isolation primitives fo… |
| 2026-11-17 07:06:14 | [itmosoft/laravel-leads](https://www.nuget.org/packages/itmosoft%2Flaravel-leads) | v1.0.0 |  | Lead capture, qualification, assignment, pipeline stages, and conversion tracki… |
| 2026-11-17 07:11:48 | [itmosoft/laravel-forms](https://www.nuget.org/packages/itmosoft%2Flaravel-forms) | v1.0.0 |  | Dynamic form definitions, versioned fields, submissions, and validation for Lar… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
