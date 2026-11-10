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

## Latest list — 2026-11-10 18:20 UTC

New packages created between 2026-11-10 17:20 UTC and 2026-11-10 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T18-20-52-15461Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 17:29:42 | [zarbinco/expiry-pricing](https://www.nuget.org/packages/zarbinco%2Fexpiry-pricing) | v0.1.1 |  | Shelf-life and expiry-based pricing calculations for Laravel. |
| 2026-11-10 17:33:13 | [atomicptr/symfony-indexed-search](https://www.nuget.org/packages/atomicptr%2Fsymfony-indexed-search) | v0.1.0 | Christopher Kaster | Indexed Search is a Symfony bundle that provides a straightforward database-pow… |
| 2026-11-10 18:10:49 | [danog/mongo-php-async-driver](https://www.nuget.org/packages/danog%2Fmongo-php-async-driver) | v0.1.0 | Daniil Gentili | Drop-in replacement for the mongodb PHP extension (ext-mongodb 2.5.6) in pure R… |
| 2026-11-10 18:14:21 | [beziworld/laravel-polkurier](https://www.nuget.org/packages/beziworld%2Flaravel-polkurier) | v1.0.0 | Kamil Ćwiertnia | Polkurier.pl WebService API client for Laravel: carriers, price valuation, orde… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
