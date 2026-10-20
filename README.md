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

## Latest list — 2026-10-20 17:21 UTC

New packages created between 2026-10-20 16:20 UTC and 2026-10-20 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T17-21-15-838843Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 16:21:15 | [medienbaecker/kirby-file-usage](https://www.nuget.org/packages/medienbaecker%2Fkirby-file-usage) | 1.0.0 | Thomas Günther | See which pages use a file |
| 2026-10-20 16:35:13 | [subscope-ai/laravel-keenable](https://www.nuget.org/packages/subscope-ai%2Flaravel-keenable) | v1.0.0 | Subscope AI | Laravel client for the Keenable search & fetch API, with tools for Laravel AI a… |
| 2026-10-20 16:48:06 | [karim-tao/pipedrive-client](https://www.nuget.org/packages/karim-tao%2Fpipedrive-client) | 0.1.0 | Karim Tao | Framework-agnostic PHP client for the Pipedrive API. PSR-18, OAuth handled, raw… |
| 2026-10-20 16:49:11 | [byteminus/laravel-bdpaygate](https://www.nuget.org/packages/byteminus%2Flaravel-bdpaygate) | v0.1.0 | Mr Hawk | Every Bangladeshi payment gateway behind one Laravel API: bKash, Nagad, SSLComm… |
| 2026-10-20 16:50:24 | [karim-tao/pipedrive-laravel](https://www.nuget.org/packages/karim-tao%2Fpipedrive-laravel) | 0.1.0 | Karim Tao | Laravel integration for the Pipedrive API. Config-driven credentials and Larave… |
| 2026-10-20 17:02:50 | [ernestdefoe/salvage](https://www.nuget.org/packages/ernestdefoe%2Fsalvage) | v1.0.0 | Ernest Defoe | Fight link rot: copies hotlinked images in posts to your own storage before the… |
| 2026-10-20 17:05:05 | [tryhackx/flarum-magnet-link](https://www.nuget.org/packages/tryhackx%2Fflarum-magnet-link) | 2.10.2 | TryHackX | Secure magnet link integration for Flarum with SHA-256 token protection, SSRF-h… |
| 2026-10-20 17:05:41 | [ernestdefoe/resurface](https://www.nuget.org/packages/ernestdefoe%2Fresurface) | v1.0.0 | Ernest Defoe | Bump a discussion back to the top without replying: manual bumps with per-group… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
