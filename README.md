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

## Latest list — 2026-10-15 07:21 UTC

New packages created between 2026-10-15 06:19 UTC and 2026-10-15 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T07-21-55-385748Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 06:21:41 | [manojkiran/filament-quick-view](https://www.nuget.org/packages/manojkiran%2Ffilament-quick-view) | v1.0.0 | Manoj Kiran | Quick view slide-overs for related records in Filament tables and infolists. |
| 2026-10-15 06:48:31 | [everysize/checkout-prestashop](https://www.nuget.org/packages/everysize%2Fcheckout-prestashop) | 1.1.0 | everysize GmbH | everysize Checkout for PrestaShop 8.1/9: imports everysize orders and reports s… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
