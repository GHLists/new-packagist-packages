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

## Latest list — 2026-11-03 09:22 UTC

New packages created between 2026-11-03 08:19 UTC and 2026-11-03 09:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T09-22-12-479388Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 08:24:38 | [microweber-packages/microweber-deps-arcanedev-php-html](https://www.nuget.org/packages/microweber-packages%2Fmicroweber-deps-arcanedev-php-html) | v9.0.2 |  | Arcanedev PHP-Html — Microweber fork with Laravel 13 support. Replaces arcanede… |
| 2026-11-03 08:24:46 | [microweber-packages/microweber-deps-arcanedev-support](https://www.nuget.org/packages/microweber-packages%2Fmicroweber-deps-arcanedev-support) | v12.0.2 |  | Arcanedev Support — Microweber fork with Laravel 13 support. Replaces arcanedev… |
| 2026-11-03 08:24:53 | [microweber-packages/microweber-deps-laravel-repository](https://www.nuget.org/packages/microweber-packages%2Fmicroweber-deps-laravel-repository) | v1.2.2 |  | Base repository implementation for Laravel — Microweber fork with Laravel 13 su… |
| 2026-11-03 08:27:37 | [blaueskreuz/module-age-verification-mrz](https://www.nuget.org/packages/blaueskreuz%2Fmodule-age-verification-mrz) | 1.0.0-beta1 |  | Verifies the age of customers at checkout from the machine-readable zone (MRZ)… |
| 2026-11-03 08:33:39 | [mathsgod/light-linq](https://www.nuget.org/packages/mathsgod%2Flight-linq) | v1.0.0 |  | A provider-based LINQ-style query library for PHP |
| 2026-11-03 08:33:39 | [mathsgod/php-linq](https://www.nuget.org/packages/mathsgod%2Fphp-linq) | v1.0.0 |  | A provider-based LINQ-style query library for PHP |
| 2026-11-03 08:40:07 | [signedly/sdk](https://www.nuget.org/packages/signedly%2Fsdk) | v0.1.0 | Signedly | Signedly REST API client for PHP: send documents for e-signature, track them an… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
