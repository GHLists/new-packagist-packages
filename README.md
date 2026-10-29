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

## Latest list — 2026-10-29 10:20 UTC

New packages created between 2026-10-29 09:21 UTC and 2026-10-29 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T10-20-42-805356Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 09:33:37 | [devfactorych/ai-spam](https://www.nuget.org/packages/devfactorych%2Fai-spam) | v1.0.0 | Mark Cameron | AI-backed, queued spam protection for Laravel forms, powered by the Laravel AI… |
| 2026-10-29 09:38:47 | [theshakhawat/laravel-nagad-fdet](https://www.nuget.org/packages/theshakhawat%2Flaravel-nagad-fdet) | v1.0.1 | Shakhawat | Nagad Modified Payment Gateway only for Freelancer Digital Expert Team. More in… |
| 2026-10-29 09:40:51 | [jield-webdev/jield-api-tools](https://www.nuget.org/packages/jield-webdev%2Fjield-api-tools) | v2.0.0-beta.1 | Johan van der Heide | Own implementation of API endpoints. This repository is based on the Laminas AP… |
| 2026-10-29 09:58:27 | [ghf/webgeeker-validation](https://www.nuget.org/packages/ghf%2Fwebgeeker-validation) | v0.1.1 | photondragon | Validation for WebGeeker (fork of photondragon/webgeeker-validation, PHP 8.4/8.… |
| 2026-10-29 10:01:00 | [samt/skipcash-laravel](https://www.nuget.org/packages/samt%2Fskipcash-laravel) | v1.0.0 | Samt | Unofficial, production-grade Laravel SDK for the SkipCash payment gateway (Qata… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
