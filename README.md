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

## Latest list — 2026-10-05 10:21 UTC

New packages created between 2026-10-05 09:19 UTC and 2026-10-05 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T10-21-45-63793Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 09:19:41 | [oktocode/sham-cash-laravel](https://www.nuget.org/packages/oktocode%2Fsham-cash-laravel) | v1.0.0 |  | Laravel bridge for the ShamCash PHP SDK. |
| 2026-10-05 09:32:00 | [flairuk/good-till-system](https://www.nuget.org/packages/flairuk%2Fgood-till-system) | v1.0.0 | Phil Graham | A Laravel client for the Goodtill EPOS API, with automatic token management. |
| 2026-10-05 09:32:02 | [ijeffro/laravel-aircrafts](https://www.nuget.org/packages/ijeffro%2Flaravel-aircrafts) | v1.0.0 | Phil Graham | IATA aircraft type codes for Laravel: an in-memory lookup API, validation rule… |
| 2026-10-05 09:32:03 | [ijeffro/laravel-airlines](https://www.nuget.org/packages/ijeffro%2Flaravel-airlines) | v1.0.0 | Phil Graham | IATA airline codes for Laravel: an in-memory lookup API, validation rule and op… |
| 2026-10-05 09:32:05 | [ijeffro/laravel-airports](https://www.nuget.org/packages/ijeffro%2Flaravel-airports) | v1.0.0 | Phil Graham | IATA airport codes for Laravel: an in-memory lookup API, validation rule and op… |
| 2026-10-05 09:32:07 | [ijeffro/laravel-cities](https://www.nuget.org/packages/ijeffro%2Flaravel-cities) | v1.0.0 | Phil Graham | IATA city codes for Laravel: an in-memory lookup API, validation rule and optio… |
| 2026-10-05 09:32:09 | [flairuk/laravel-countries](https://www.nuget.org/packages/flairuk%2Flaravel-countries) | v1.0.0 | Phil Graham | ISO 3166 countries for Laravel: codes, currencies, calling codes, regions, EEA… |
| 2026-10-05 09:35:09 | [kommandhub/click-and-pick-sw](https://www.nuget.org/packages/kommandhub%2Fclick-and-pick-sw) | 0.10.0 | Kommandhub Limited | Click and collect for Shopware 6: pickup-location selection in checkout, a self… |
| 2026-10-05 09:43:17 | [flairuk/laravel-world](https://www.nuget.org/packages/flairuk%2Flaravel-world) | v1.0.0 | Phil Graham | Countries, cities, airports, airlines and aircraft for Laravel, joined up: one… |
| 2026-10-05 09:53:42 | [mage2kishan/module-filter-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-filter-seo) | 1.1.6 | Kishan Savaliya | Panth Filter SEO — clean path-based URLs for layered navigation filters + dynam… |
| 2026-10-05 09:56:20 | [gingerminds/symfony-media-manager](https://www.nuget.org/packages/gingerminds%2Fsymfony-media-manager) | 0.1.0 | Gingerminds | Media library, file library and image processing for Gingerminds Symfony projec… |
| 2026-10-05 09:58:59 | [maiobarbero/laravel-aftercare](https://www.nuget.org/packages/maiobarbero%2Flaravel-aftercare) | v0.1.0 | Matteo Barbero | An opinionated starting configuration for Laravel, with Pint, PHPStan, Rector,… |
| 2026-10-05 10:02:03 | [kreatiflabs/laravel-bank-guard](https://www.nuget.org/packages/kreatiflabs%2Flaravel-bank-guard) | v1.0 | Kreatiflabs | Indonesian Bank Master Data, Account Number Sanitizer & Precision Validation Gu… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
