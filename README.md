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

## Latest list — 2026-10-25 02:21 UTC

New packages created between 2026-10-25 01:21 UTC and 2026-10-25 02:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T02-21-58-721016Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 01:50:53 | [postiefs/laravel-sso](https://www.nuget.org/packages/postiefs%2Flaravel-sso) | v1.0.0 |  | Sign in to a Laravel app through the Postiefs SSO portal (Microsoft Entra ID),… |
| 2026-10-25 01:51:13 | [postiefs/laravel-filament-sso](https://www.nuget.org/packages/postiefs%2Flaravel-filament-sso) | v1.0.0 |  | Filament panel plugin for the Postiefs SSO portal: a Microsoft 365 sign-in butt… |
| 2026-10-25 01:57:16 | [anun333/oe-module-title-x-report](https://www.nuget.org/packages/anun333%2Foe-module-title-x-report) | v0.1.0 |  | Title X Report for OpenEMR: the FPAR 2.0 file for the Office of Population Affa… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
