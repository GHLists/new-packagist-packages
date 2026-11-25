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

## Latest list — 2026-11-25 00:20 UTC

New packages created between 2026-11-24 23:19 UTC and 2026-11-25 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T00-20-28-271569Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 23:32:30 | [wsign/wsign-php](https://www.nuget.org/packages/wsign%2Fwsign-php) | v1.0.0 | wsign | Official PHP library for the wsign e-signature API: signature requests, templat… |
| 2026-11-24 23:51:56 | [andrexdd/tombstone](https://www.nuget.org/packages/andrexdd%2Ftombstone) | v1.0.0 | andre | Keeps deleted discussions from becoming dead 404 links. Automatically serves a… |
| 2026-11-25 00:06:17 | [protocollive/php86time](https://www.nuget.org/packages/protocollive%2Fphp86time) | 2026.11.24 | Fabio Carpi | Time namespace classes for PHP < 8.6 |
| 2026-11-25 00:17:25 | [datacircle/laravel-boost](https://www.nuget.org/packages/datacircle%2Flaravel-boost) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. Four Laravel Boost tools call Datacircle's public API.… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
