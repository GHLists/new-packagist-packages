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

## Latest list — 2026-11-14 12:20 UTC

New packages created between 2026-11-14 11:19 UTC and 2026-11-14 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T12-20-27-441713Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 11:26:50 | [pitchayakit/laravel-buddhist-era](https://www.nuget.org/packages/pitchayakit%2Flaravel-buddhist-era) | v1.0.0 |  | Laravel package that makes Carbon's translatedFormat() show the Buddhist Era ye… |
| 2026-11-14 11:27:38 | [studio-variable/kirby-assets-versioning](https://www.nuget.org/packages/studio-variable%2Fkirby-assets-versioning) | v1.0.0 | Studio Variable | Append a content hash to the URLs of the CSS and JS files of a Kirby site, so b… |
| 2026-11-14 11:37:17 | [timber/rings](https://www.nuget.org/packages/timber%2Frings) | 1.0.0 | Nicolas Lemoine | A Query Monitor panel that shows you what's happening in your Twig templates |
| 2026-11-14 11:49:35 | [osaris-uk/monzo](https://www.nuget.org/packages/osaris-uk%2Fmonzo) | 1.0.0 | Osaris | A full-featured Laravel package for the Monzo Developer API: OAuth with automat… |
| 2026-11-14 12:06:09 | [unipo/siakad-sdk](https://www.nuget.org/packages/unipo%2Fsiakad-sdk) | v1.0.0 | Pustikom Universitas Pohuwato | SDK resmi API SIAKAD UNIPO untuk PHP 8.1+: token OAuth2 otomatis, 2.000+ endpoi… |
| 2026-11-14 12:08:16 | [four-bytes/four-http-client](https://www.nuget.org/packages/four-bytes%2Ffour-http-client) | v4.2.1 | Four Bytes | Modern PHP 8.4+ HTTP client factory and middleware library for API integrations |
| 2026-11-14 12:16:58 | [phoenix1331/laravel-clorian](https://www.nuget.org/packages/phoenix1331%2Flaravel-clorian) | v0.1.0 | Darren Williams | Confidence-aware typed decisions for Laravel models and input: let Jev make the… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
