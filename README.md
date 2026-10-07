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

## Latest list — 2026-10-07 15:19 UTC

New packages created between 2026-10-07 14:19 UTC and 2026-10-07 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T15-19-32-096986Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 14:25:49 | [folklore/laravel-image](https://www.nuget.org/packages/folklore%2Flaravel-image) | v1.1.0 | Folklore; David Mongeau-Petit… | URL-based image manipulation for Laravel, built on Imagine |
| 2026-10-07 14:45:31 | [jothamlec/laravel-offsite-backup](https://www.nuget.org/packages/jothamlec%2Flaravel-offsite-backup) | v0.1.0 | Jotham Lim | A Deployer recipe and hardened preset for spatie/laravel-backup, with pre-fligh… |
| 2026-10-07 14:45:54 | [brewless/cli](https://www.nuget.org/packages/brewless%2Fcli) | v0.1.1 | Coding Agency | The command line client of Brewless: sign in, connect a project and deploy it t… |
| 2026-10-07 14:45:58 | [brewless/laravel](https://www.nuget.org/packages/brewless%2Flaravel) | v0.1.0 | Coding Agency | What a Laravel application needs to run on Brewless: the release, schedule and… |
| 2026-10-07 14:57:05 | [atwx/silverstripe-htmlfield-cleaner](https://www.nuget.org/packages/atwx%2Fsilverstripe-htmlfield-cleaner) | v6.2.0 |  | Cleans HTML fields (tags, attributes, inline styles) of DataObjects before writ… |
| 2026-10-07 15:01:29 | [rmb32/kevin](https://www.nuget.org/packages/rmb32%2Fkevin) | v1.0.0 | Roger Barnfather | An easy bulk filesystem manipulation utility for your PHP files — find files, r… |
| 2026-10-07 15:02:55 | [collection/collection](https://www.nuget.org/packages/collection%2Fcollection) | 1.0.0 | chipslays | Laravel-compatible PHP collection with dot-notation and wildcard paths in every… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
