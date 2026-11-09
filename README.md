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

## Latest list — 2026-11-09 14:18 UTC

New packages created between 2026-11-09 13:20 UTC and 2026-11-09 14:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T14-18-41-934956Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 13:21:06 | [adachsoft/ai-image-google](https://www.nuget.org/packages/adachsoft%2Fai-image-google) | v0.1.0 | Arkadiusz Adach | Google Gemini image generation provider for adachsoft/ai-image-contract. |
| 2026-11-09 13:25:36 | [hashtagcms/invoice](https://www.nuget.org/packages/hashtagcms%2Finvoice) | v1.0.0 | HashtagCMS | Configurable, driver-based PDF invoice generation for Laravel and HashtagCMS |
| 2026-11-09 13:26:32 | [supseven/theme-library](https://www.nuget.org/packages/supseven%2Ftheme-library) | v1.0.0 |  | Helper library for TYPO3 projects |
| 2026-11-09 13:36:19 | [dskripchenko/laravel-oidc](https://www.nuget.org/packages/dskripchenko%2Flaravel-oidc) | v0.1.0 | Denis Skripchenko | OpenID Connect for Laravel without a JOSE library: authorization code sign-in w… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
