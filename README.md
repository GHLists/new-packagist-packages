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

## Latest list — 2026-10-14 17:21 UTC

New packages created between 2026-10-14 16:23 UTC and 2026-10-14 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T17-21-29-898954Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 16:44:53 | [x-laravel/username](https://www.nuget.org/packages/x-laravel%2Fusername) | v1.0.0 | Mehmet ÖĞMEN | Configurable username validation, reserved-name checking and username generatio… |
| 2026-10-14 16:52:02 | [kechankrisna/php_wing](https://www.nuget.org/packages/kechankrisna%2Fphp_wing) | v1.0.0 | kechankrisna | Wing Bank online payment (Web SDK v2) client for PHP: authorize payments, open… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
