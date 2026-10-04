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

## Latest list — 2026-10-04 20:20 UTC

New packages created between 2026-10-04 19:19 UTC and 2026-10-04 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T20-20-07-577241Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 19:20:14 | [mage2kishan/module-order-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-order-attachments) | 1.1.7 |  | Allows customers to attach files to order items |
| 2026-10-04 19:54:50 | [artisan-build/telltale-client](https://www.nuget.org/packages/artisan-build%2Ftelltale-client) | v1.0.0 |  | NativePHP client package for reporting device analytics to a self-hosted Tellta… |
| 2026-10-04 19:54:53 | [artisan-build/telltale-contracts](https://www.nuget.org/packages/artisan-build%2Ftelltale-contracts) | v1.0.0 |  | Versioned wire contracts shared by the Telltale client and server. |
| 2026-10-04 20:02:49 | [vivutio/property-module](https://www.nuget.org/packages/vivutio%2Fproperty-module) | v0.1.0 | Ezekiel Mjema | Properties for vivutio: the camps, lodges and hotels an organization runs, each… |
| 2026-10-04 20:07:19 | [nurbekjummayev/filament-tdc-sso](https://www.nuget.org/packages/nurbekjummayev%2Ffilament-tdc-sso) | 0.1 | Nurbek Jummayev | TDC-SSO (OAuth2 Authorization Code + PKCE) login, screen lock and PIN unlock pl… |
| 2026-10-04 20:11:16 | [mage2kishan/module-checkout-extended](https://www.nuget.org/packages/mage2kishan%2Fmodule-checkout-extended) | 1.1.8 | Kishan Savaliya | Enhanced one-page checkout for Magento 2 with configurable multi-column layouts… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
