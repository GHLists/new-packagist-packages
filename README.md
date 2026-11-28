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

## Latest list — 2026-11-28 03:20 UTC

New packages created between 2026-11-28 02:21 UTC and 2026-11-28 03:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T03-20-57-66993Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 02:21:33 | [se7enxweb/exppaystack](https://www.nuget.org/packages/se7enxweb%2Fexppaystack) | v0.0.0.1 | 7x | Paystack payment gateway for the Exponential shop: inline Paystack checkout (ca… |
| 2026-11-28 02:31:03 | [diepxuan/laravel-catalog](https://www.nuget.org/packages/diepxuan%2Flaravel-catalog) | 2.9.9 | Tran Ngoc Duc | Catalog package for DXPanel |
| 2026-11-28 02:41:26 | [jonesshen/php-cs-fixer-config](https://www.nuget.org/packages/jonesshen%2Fphp-cs-fixer-config) | v1.0.0 | Jone Shen | A custom PHP CS Fixer configuration library |
| 2026-11-28 02:45:42 | [jaizendra-netizen/email-verify-pack-quote](https://www.nuget.org/packages/jaizendra-netizen%2Femail-verify-pack-quote) | v1.0.0 | Jainendra Ojha | PHP CLI that prices an email verification job on MillionVerifier packs or ZeroB… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
