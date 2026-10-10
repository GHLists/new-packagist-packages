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

## Latest list — 2026-10-10 19:20 UTC

New packages created between 2026-10-10 18:19 UTC and 2026-10-10 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T19-20-06-292133Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 18:19:47 | [ernadoo/boxtal](https://www.nuget.org/packages/ernadoo%2Fboxtal) | v0.1.0 | Erwan Nader | Boxtal API client: quotes (v1), shipping orders, labels, tracking, parcel point… |
| 2026-10-10 18:27:40 | [spaanproductions/laravel-ai-usage](https://www.nuget.org/packages/spaanproductions%2Flaravel-ai-usage) | v0.1.0 | Spaan Productions | Tracks the tokens and cost of every laravel/ai call, with a filterable Livewire… |
| 2026-10-10 18:47:09 | [zeusi/ganesha-apcu-adapter](https://www.nuget.org/packages/zeusi%2Fganesha-apcu-adapter) | 0.1.0 |  | APCu storage adapter for Ganesha implementing the sliding time window Rate stra… |
| 2026-10-10 18:47:22 | [antevemus/aspecification](https://www.nuget.org/packages/antevemus%2Faspecification) | v1.7.0 | Heliton Junior - CTO @ Anteve… | Enterprise Specification Pattern Framework for PHP 8.2+ (DDD, Notification Patt… |
| 2026-10-10 18:49:45 | [lottevo/lottevo-php](https://www.nuget.org/packages/lottevo%2Flottevo-php) | v0.1.0 | Lottevo | A thin PHP client for the Lottevo lottery data API. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
