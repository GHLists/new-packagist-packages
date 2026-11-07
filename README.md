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

## Latest list — 2026-11-07 22:20 UTC

New packages created between 2026-11-07 21:19 UTC and 2026-11-07 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T22-20-16-915249Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 21:23:32 | [ophelix/ophelix-php](https://www.nuget.org/packages/ophelix%2Fophelix-php) | v0.1.0 | Lunify SAS | Bibliothèque PHP officielle de l'API Ophelix : facturation de l'Assurance Malad… |
| 2026-11-07 21:27:50 | [flagbearer/flagbearer](https://www.nuget.org/packages/flagbearer%2Fflagbearer) | v0.1.0 |  | Flagbearer PHP SDK |
| 2026-11-07 21:46:31 | [goaop/goaop-yii3-bridge](https://www.nuget.org/packages/goaop%2Fgoaop-yii3-bridge) | 1.0.0 | Lisachenko Alexander | Integration bridge for Go! AOP framework and Yii3 |
| 2026-11-07 21:55:16 | [ankane/php-memcheck](https://www.nuget.org/packages/ankane%2Fphp-memcheck) | v0.1.0 | Andrew Kane | Check PHP FFI bindings for memory issues |
| 2026-11-07 22:01:24 | [flytachi/winter-sdk-s5w](https://www.nuget.org/packages/flytachi%2Fwinter-sdk-s5w) | v1.0.0 | Flytachi | PHP SDK for S5W, the file store and CDN: buckets, folders, uploads with resumab… |
| 2026-11-07 22:01:47 | [romanfedorskij/seed](https://www.nuget.org/packages/romanfedorskij%2Fseed) | v0.1.0 | Roman Fedorskij | Framework-agnostic toolkit for versioned, fingerprinted data seeds |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
