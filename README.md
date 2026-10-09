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

## Latest list — 2026-10-09 07:19 UTC

New packages created between 2026-10-09 06:20 UTC and 2026-10-09 07:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T07-19-33-175628Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 06:26:33 | [taldres/laravel-immutable-attributes](https://www.nuget.org/packages/taldres%2Flaravel-immutable-attributes) | v1.0.0 | Dennis Petersmann | Guard Eloquent model attributes against changes once a row exists: declare them… |
| 2026-10-09 06:31:35 | [crawlora/reddit](https://www.nuget.org/packages/crawlora%2Freddit) | v0.1.1 |  | Reddit client for the Crawlora hosted API |
| 2026-10-09 06:31:54 | [crawlora/amazon](https://www.nuget.org/packages/crawlora%2Famazon) | v0.1.1 |  | Amazon client for the Crawlora hosted API |
| 2026-10-09 06:32:27 | [crawlora/imdb](https://www.nuget.org/packages/crawlora%2Fimdb) | v0.1.1 |  | IMDb client for the Crawlora hosted API |
| 2026-10-09 06:37:37 | [crawlora/tiktok](https://www.nuget.org/packages/crawlora%2Ftiktok) | v0.1.1 |  | TikTok client for the Crawlora hosted API |
| 2026-10-09 06:42:49 | [omroepgelderland/php-coding-standard](https://www.nuget.org/packages/omroepgelderland%2Fphp-coding-standard) | 0.1.0 | Remy Glaser | PHP coding standard used by Omroep Gelderland. |
| 2026-10-09 07:03:06 | [digit7s/laravel-audit-toolkit](https://www.nuget.org/packages/digit7s%2Flaravel-audit-toolkit) | v0.1.0 | Digit7s | A Laravel-native, privacy-conscious audit event recorder and read API. |
| 2026-10-09 07:03:07 | [digit7s/filament-audit-toolkit](https://www.nuget.org/packages/digit7s%2Ffilament-audit-toolkit) | v0.1.0 | Digit7s | A read-only Filament 5 explorer and record history for Digit7s Laravel audit ev… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
