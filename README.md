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

## Latest list — 2026-11-17 14:20 UTC

New packages created between 2026-11-17 13:20 UTC and 2026-11-17 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T14-20-27-415366Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 13:52:28 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.30.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-17 14:02:31 | [colibri-informatique/laravel-geotools](https://www.nuget.org/packages/colibri-informatique%2Flaravel-geotools) | v1.0.0 |  | Generic geolocation for Laravel Eloquent models: address value object, pluggabl… |
| 2026-11-17 14:02:32 | [crystoline/xpsr-database-seeder](https://www.nuget.org/packages/crystoline%2Fxpsr-database-seeder) | v0.8.1 | Adekunle | Seed data for XPSR applications: seeders that converge, so running them again c… |
| 2026-11-17 14:04:45 | [jeffersongoncalves/filament-gdpr-dpia](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-gdpr-dpia) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-gdpr-dpia: data protection impact assessments (Art.… |
| 2026-11-17 14:11:02 | [jeffersongoncalves/filament-gdpr-breaches](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-gdpr-breaches) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-gdpr-breaches: your personal data breach register i… |
| 2026-11-17 14:15:50 | [jeffersongoncalves/filament-gdpr-children](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-gdpr-children) | 1.0.0 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
