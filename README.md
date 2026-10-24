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

## Latest list — 2026-10-24 23:20 UTC

New packages created between 2026-10-24 22:19 UTC and 2026-10-24 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T23-20-34-610284Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 23:07:49 | [jsonscraper/instagram-api-php](https://www.nuget.org/packages/jsonscraper%2Finstagram-api-php) | v0.1.0 |  | Instagram Scraper API client for PHP with Composer and response models |
| 2026-10-24 23:08:31 | [jsonscraper/tiktok-api-php](https://www.nuget.org/packages/jsonscraper%2Ftiktok-api-php) | v0.1.0 | Evelode | TikTok Scraper API for PHP — typed response models, video, profiles, comments a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
