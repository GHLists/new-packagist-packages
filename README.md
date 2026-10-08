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

## Latest list — 2026-10-08 01:20 UTC

New packages created between 2026-10-08 00:21 UTC and 2026-10-08 01:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T01-20-08-779321Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 00:28:22 | [tamarackdb/tamarackdb-php](https://www.nuget.org/packages/tamarackdb%2Ftamarackdb-php) | v0.1.0 |  | PHP client for TamarackDB, an event store compliant with the DCB specification. |
| 2026-10-08 00:43:55 | [jeffersongoncalves/filament-open-hours](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-open-hours) | 3.0.0 | Jefferson Gonçalves | Opening hours for Filament: manage the weekly schedule, holidays, special dates… |
| 2026-10-08 00:43:55 | [jeffersongoncalves/laravel-open-hours](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-open-hours) | 1.0.0 | Jefferson Gonçalves | Business opening hours for Laravel, stored with spatie/laravel-settings: weekly… |
| 2026-10-08 00:56:54 | [jeffersongoncalves/filament-editorial-theme](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-editorial-theme) | 1.0.0 | Jefferson Gonçalves | Editorial Terminal: a paper + terminal theme for Filament 5. Fraunces / DM Sans… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
