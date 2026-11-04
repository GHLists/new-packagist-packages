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

## Latest list — 2026-11-04 13:21 UTC

New packages created between 2026-11-04 12:20 UTC and 2026-11-04 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T13-21-29-298337Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 12:22:18 | [mozex/iminify-php](https://www.nuget.org/packages/mozex%2Fiminify-php) | 1.0.0 | Mozex | PHP client for the Iminify image optimization API, with an optimizer for Spatie… |
| 2026-11-04 12:23:25 | [stolt/php-lean](https://www.nuget.org/packages/stolt%2Fphp-lean) | v0.9.1 | Raphael Stolt | A library and CLI for validating and managing package release contents in lean… |
| 2026-11-04 12:28:09 | [spkm/jamf](https://www.nuget.org/packages/spkm%2Fjamf) | v0.0.1 | Simon Mitchell | Integrate with the Jamf Pro API and Classic API using SaloonPHP |
| 2026-11-04 12:29:33 | [adamjenkins/moodle-format_spiffy](https://www.nuget.org/packages/adamjenkins%2Fmoodle-format_spiffy) | v0.1.0 | Adam Jenkins | A course format of colourful activity cards: students work inside the card, one… |
| 2026-11-04 12:35:23 | [mozex/iminify-laravel](https://www.nuget.org/packages/mozex%2Fiminify-laravel) | 1.0.0 | Mozex | Laravel wrapper for the Iminify image optimization API, with webhooks and an op… |
| 2026-11-04 12:53:02 | [studioastra/multilang-bundle](https://www.nuget.org/packages/studioastra%2Fmultilang-bundle) | v1.0.0 |  | Symfony bundle for multilingual sites: pre-filled translations (14 languages),… |
| 2026-11-04 12:57:18 | [miasssite/yu_social](https://www.nuget.org/packages/miasssite%2Fyu_social) | 1.0.0 |  | Social links block for Drupal 11 |
| 2026-11-04 13:04:45 | [itmosoft/laravel-tax](https://www.nuget.org/packages/itmosoft%2Flaravel-tax) | v1.0.0 |  | A reusable Laravel tax package with tax classes, rates, location-based rules, a… |
| 2026-11-04 13:06:31 | [runapi-ai/muse-video](https://www.nuget.org/packages/runapi-ai%2Fmuse-video) | v0.2.0 | RunAPI | RunAPI Muse Video Composer package for PHP applications |
| 2026-11-04 13:10:09 | [studioastra/image-optimizer-bundle](https://www.nuget.org/packages/studioastra%2Fimage-optimizer-bundle) | v1.0.0 | Studio Astra | Symfony bundle that losslessly optimizes every uploaded image (weight, format,… |
| 2026-11-04 13:14:37 | [itmosoft/laravel-cart](https://www.nuget.org/packages/itmosoft%2Flaravel-cart) | v1.0.1 |  | A reusable Laravel shopping cart package with persistent carts, items, quantity… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
