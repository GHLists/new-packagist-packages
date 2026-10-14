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

## Latest list — 2026-10-14 04:21 UTC

New packages created between 2026-10-14 03:22 UTC and 2026-10-14 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T04-21-46-238998Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 03:38:11 | [caturseptian/laravel-sluggable](https://www.nuget.org/packages/caturseptian%2Flaravel-sluggable) | v1.0.0 | Catur Septian; Freek Van der… | Slug Eloquent yang paham bahasa Indonesia untuk Laravel 6–13, bisa di-eject aga… |
| 2026-10-14 03:50:51 | [expertsystemsau/trackto-laravel-client](https://www.nuget.org/packages/expertsystemsau%2Ftrackto-laravel-client) | v0.1.0 | Mitchell Williams | Laravel integration for the track.to API |
| 2026-10-14 03:50:51 | [expertsystemsau/trackto-php-client](https://www.nuget.org/packages/expertsystemsau%2Ftrackto-php-client) | v0.1.0 | Mitchell Williams | Framework-agnostic PHP client for the track.to API |
| 2026-10-14 03:54:27 | [caiyun/asr](https://www.nuget.org/packages/caiyun%2Fasr) | v1.0.0 | 刘骏霖 | 彩云语音识别服务，统一封装腾讯云、科大讯飞、阿里云一句话识别 |
| 2026-10-14 04:12:22 | [ogunsakin01/laravel-video-demos](https://www.nuget.org/packages/ogunsakin01%2Flaravel-video-demos) | v0.1.0 | Damilola Ogunsakin | Generate how-to videos of your Laravel app with Claude. Describe a flow, set a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
