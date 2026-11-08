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

## Latest list — 2026-11-08 22:20 UTC

New packages created between 2026-11-08 21:21 UTC and 2026-11-08 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T22-20-55-023996Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 21:23:25 | [jeffersongoncalves/filament-centrifugo](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-centrifugo) | 1.0.1 |  |  |
| 2026-11-08 21:31:04 | [pembayaranku/php-sdk](https://www.nuget.org/packages/pembayaranku%2Fphp-sdk) | 1.0.0 | PT MEDIA SIRINGO ABADI | Official PHP SDK for PembayaranKU Merchant API V1 |
| 2026-11-08 21:35:25 | [henzeb/housepedia-intelligence](https://www.nuget.org/packages/henzeb%2Fhousepedia-intelligence) | v1.0.0 | Henze Berkheij | Framework-independent PHP SDK for the Housepedia Intelligence API |
| 2026-11-08 21:35:29 | [henzeb/housepedia-intelligence-laravel](https://www.nuget.org/packages/henzeb%2Fhousepedia-intelligence-laravel) | v1.0.0 | Henze Berkheij | Laravel integration for the Housepedia Intelligence PHP SDK |
| 2026-11-08 21:40:35 | [kusikusicms/routes](https://www.nuget.org/packages/kusikusicms%2Froutes) | v13.2.0 |  | Run-time routes for KusikusiCMS entities: slug-based paths, redirects and a cat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
