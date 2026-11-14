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

## Latest list — 2026-11-14 14:19 UTC

New packages created between 2026-11-14 13:19 UTC and 2026-11-14 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T14-19-39-763211Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 13:28:51 | [jeromebadour/fernway-laravel](https://www.nuget.org/packages/jeromebadour%2Ffernway-laravel) | v1.0.0 | Jerome Badour | Send your Laravel app's leads into GoHighLevel through Fernway, with retries, a… |
| 2026-11-14 13:30:34 | [sendclap/sendclap](https://www.nuget.org/packages/sendclap%2Fsendclap) | v0.2.0 |  | Official Sendclap client: license key checks for your app and the creator REST… |
| 2026-11-14 14:05:21 | [hsemix/laravanced-wallet](https://www.nuget.org/packages/hsemix%2Flaravanced-wallet) | v1.0.0 | Semitala Hamidouh | Double-entry multi-account wallet for Laravel: account types, transfer types, f… |
| 2026-11-14 14:06:19 | [happenv-com/laravel-queue-prefork](https://www.nuget.org/packages/happenv-com%2Flaravel-queue-prefork) | v1.0.0 | Happenv sp. z o.o.; webard | Run a pool of Laravel queue workers as forks of one small parent that never loa… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
