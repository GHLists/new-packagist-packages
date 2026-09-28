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

## Latest list — 2026-09-28 20:20 UTC

New packages created between 2026-09-28 19:20 UTC and 2026-09-28 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T20-20-13-366914Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 19:41:19 | [reynotech/dev-login-laravel](https://www.nuget.org/packages/reynotech%2Fdev-login-laravel) | v0.1.0 |  | Development-only local account seeder for the Dev Login browser extension |
| 2026-09-28 19:54:55 | [znojil/vies](https://www.nuget.org/packages/znojil%2Fvies) | v1.0.0 | Marek Znojil | PHP client for the EU VIES VAT number validation service. |
| 2026-09-28 19:58:09 | [kaveraa/data-lifecycle](https://www.nuget.org/packages/kaveraa%2Fdata-lifecycle) | v1.0.0 | Augustin Kavera | Conservation et cycle de vie des données personnelles pour Laravel et Symfony/D… |
| 2026-09-28 20:02:32 | [phpsoftbox/barcode](https://www.nuget.org/packages/phpsoftbox%2Fbarcode) | v1.0.0 | Anton K. | Barcode and QR generation component for the PhpSoftBox framework |
| 2026-09-28 20:03:41 | [huzaifaarain/laravel-pulse-mcp](https://www.nuget.org/packages/huzaifaarain%2Flaravel-pulse-mcp) | v0.1.0 | Huzaifa Saif-ur-Rehman | Securely expose Laravel Pulse production monitoring data to AI agents through a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
