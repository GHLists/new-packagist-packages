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

## Latest list — 2026-11-08 15:19 UTC

New packages created between 2026-11-08 14:19 UTC and 2026-11-08 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T15-19-46-126917Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 14:26:17 | [capimail/capimail-php](https://www.nuget.org/packages/capimail%2Fcapimail-php) | v0.1.1 | CapiMail | Official PHP SDK for CapiMail with Laravel integration: transactional email, a… |
| 2026-11-08 14:32:27 | [byfareska/crud](https://www.nuget.org/packages/byfareska%2Fcrud) | v0.1.0 | Karol Szarafinowski | Symfony bundle for admin panels: CRUDs from an attribute (Doctrine or DTO + use… |
| 2026-11-08 14:50:55 | [smwks/laravel-ai-kit](https://www.nuget.org/packages/smwks%2Flaravel-ai-kit) | v0.5.0 | Ralph Schindler | A component kit (turn/event data model + Livewire chat UI) for laravel/ai agent… |
| 2026-11-08 15:13:30 | [venusian/silk](https://www.nuget.org/packages/venusian%2Fsilk) | 0.11.0 | Angel Gonzalez | Self-drawn, springy widgets for Venusian Surface. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
