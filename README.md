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

## Latest list — 2026-11-20 23:21 UTC

New packages created between 2026-11-20 22:20 UTC and 2026-11-20 23:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T23-21-34-631895Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 22:33:00 | [koderia-creative-lab/laravel-upperlink](https://www.nuget.org/packages/koderia-creative-lab%2Flaravel-upperlink) | v1.0.0 | Koderia Creative Lab | A modern Laravel client and driver for the Upperlink (PayChoice / Paygate) paym… |
| 2026-11-20 22:40:25 | [printmelo/printmelo-laravel](https://www.nuget.org/packages/printmelo%2Fprintmelo-laravel) | v1.0.1 | Printmelo | Laravel integration for Printmelo: a facade, config, webhook handling with even… |
| 2026-11-20 22:40:25 | [printmelo/printmelo-php](https://www.nuget.org/packages/printmelo%2Fprintmelo-php) | v1.0.0 | Printmelo | Official PHP SDK for the Printmelo API: print from your own software to printer… |
| 2026-11-20 22:56:51 | [devmount/kirby-updater](https://www.nuget.org/packages/devmount%2Fkirby-updater) | 1.0.0 | Andreas Müller | Update the Kirby core to the latest patch or minor release from the Panel |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
