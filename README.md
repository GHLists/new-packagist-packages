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

## Latest list — 2026-10-14 16:23 UTC

New packages created between 2026-10-14 14:23 UTC and 2026-10-14 16:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T16-23-00-687779Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 14:25:17 | [mikhailmelnikov/backpack-jobs-monitor](https://www.nuget.org/packages/mikhailmelnikov%2Fbackpack-jobs-monitor) | v1.0.1 | Mikhail Melnikov | Backpack for Laravel add-on: scheduler tasks and database queue jobs in the adm… |
| 2026-10-14 14:40:59 | [diablomedia/address-formatter-php](https://www.nuget.org/packages/diablomedia%2Faddress-formatter-php) | 1.2.0 | PredictHQ; Robert Kern; Diabl… | Address formatter using country templates from https://github.com/OpenCageData/… |
| 2026-10-14 14:41:18 | [hwkdo/intranet-app-maqual](https://www.nuget.org/packages/hwkdo%2Fintranet-app-maqual) | v0.1.1 | hwkdo | Verwaltung, Beantragung und Bewertung von Mitarbeiterqualifizierungen |
| 2026-10-14 14:46:50 | [praveendias1180/a2a-laravel-starter](https://www.nuget.org/packages/praveendias1180%2Fa2a-laravel-starter) | v1.0.1 |  | A Laravel app that is already an A2A (Agent2Agent) agent. Clone it, run it, and… |
| 2026-10-14 15:05:29 | [codetiv/upgates-php-sdk](https://www.nuget.org/packages/codetiv%2Fupgates-php-sdk) | v0.0.1 | Pavel Skrbel | Elegant SDK written in PHP to work with the Upgates API |
| 2026-10-14 15:13:08 | [statikbe/craft-entry-anchors](https://www.nuget.org/packages/statikbe%2Fcraft-entry-anchors) | 1.0.0-beta.2 | Statik | Anchor titles for Craft CMS blocks, and an anchor dropdown on Link fields to li… |
| 2026-10-14 15:21:53 | [miraiportal/laravel-kagero](https://www.nuget.org/packages/miraiportal%2Flaravel-kagero) | 1.0.0 |  |  |
| 2026-10-14 15:25:15 | [ernestdefoe/backdrop](https://www.nuget.org/packages/ernestdefoe%2Fbackdrop) | 1.0.0 | Ernest Defoe | Profile covers for Flarum 2: upload, drag to frame, zoom. On profiles, hover ca… |
| 2026-10-14 15:27:47 | [hussainweb/taarikh-picker](https://www.nuget.org/packages/hussainweb%2Ftaarikh-picker) | v0.1.0 | Hussain Abbas | Lightweight, accessible Hijri calendar date picker |
| 2026-10-14 16:16:07 | [echoproof/laravel](https://www.nuget.org/packages/echoproof%2Flaravel) | v0.1.0 |  | Record real Laravel traffic as Echoproof snapshots, without a proxy |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
