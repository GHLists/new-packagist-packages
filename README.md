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

## Latest list — 2026-10-24 19:19 UTC

New packages created between 2026-10-24 18:21 UTC and 2026-10-24 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T19-19-57-052897Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 18:22:48 | [jeffersongoncalves/laravel-session-management](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-session-management) | 1.0.0 | Jefferson Gonçalves | Read and manage Laravel's database session table (sessions) through a model and… |
| 2026-10-24 18:22:59 | [jeffersongoncalves/filament-session-management](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-session-management) | 1.0.1 |  |  |
| 2026-10-24 18:30:06 | [skeeks/cms-communication-max](https://www.nuget.org/packages/skeeks%2Fcms-communication-max) | 1.0.0 | Semenov Alexander | MAX messenger bot driver for skeeks/cms-communication |
| 2026-10-24 18:30:17 | [imrandevbd/laravel-ai-ocr](https://www.nuget.org/packages/imrandevbd%2Flaravel-ai-ocr) | v1.1.0 | Imran Ahmed | Private manual-first document extraction with local OCR, quality scoring and ta… |
| 2026-10-24 18:40:08 | [un-dev-suisse/laravel-files-storage](https://www.nuget.org/packages/un-dev-suisse%2Flaravel-files-storage) | v1.0.0 |  | File stores for Laravel: named stores over filesystem disks, optional AES-256-G… |
| 2026-10-24 19:18:10 | [karsawave/palakar](https://www.nuget.org/packages/karsawave%2Fpalakar) | v0.1.0 | KarsaWave; Iskandar Soesman | Palakar Framework: a simple and secure PHP 8.2+ framework, fork of Panada Frame… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
