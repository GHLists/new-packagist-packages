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

## Latest list — 2026-11-11 21:20 UTC

New packages created between 2026-11-11 19:19 UTC and 2026-11-11 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T21-20-36-929247Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 19:19:18 | [kirora/kirora-laravel](https://www.nuget.org/packages/kirora%2Fkirora-laravel) | v0.1.0 | Kirora and contributors | Kirora for Laravel. |
| 2026-11-11 19:19:44 | [crabphp/tide](https://www.nuget.org/packages/crabphp%2Ftide) | v0.1.0 |  | Typed models and explicit relations for the Crab framework |
| 2026-11-11 19:45:34 | [php-io-extensions/sokol-audio](https://www.nuget.org/packages/php-io-extensions%2Fsokol-audio) | v0.11.0 | Project Saturn Studios, LLC | 1:1 PHP bindings of sokol_audio.h (floooh/sokol), with the library compiled int… |
| 2026-11-11 19:46:14 | [rippera/laravel-api-types](https://www.nuget.org/packages/rippera%2Flaravel-api-types) | v0.1.0 | Mikheil Mezurnishvili | Generate TypeScript types, enums and interfaces from Laravel routes, FormReques… |
| 2026-11-11 19:55:04 | [php-io-extensions/miniaudio](https://www.nuget.org/packages/php-io-extensions%2Fminiaudio) | v0.11.1 | Project Saturn Studios, LLC | 1:1 PHP bindings of miniaudio 0.11.26, with the library compiled into the exten… |
| 2026-11-11 20:41:21 | [sadaya/sadaya-php](https://www.nuget.org/packages/sadaya%2Fsadaya-php) | v1.0.1 |  | Sadaya API client for PHP: orders, refunds, webhook, signature verification and… |
| 2026-11-11 20:55:10 | [kalvi/nfse](https://www.nuget.org/packages/kalvi%2Fnfse) | v0.1.0 |  | Cliente PHP da API Kalvi: classifica e confere a NFS-e do padrão nacional para… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
