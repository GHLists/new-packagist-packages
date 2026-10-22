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

## Latest list — 2026-10-22 07:21 UTC

New packages created between 2026-10-22 06:21 UTC and 2026-10-22 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T07-21-10-843587Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 06:27:05 | [xph/laravel](https://www.nuget.org/packages/xph%2Flaravel) | v0.1.0 |  | Render compiled xph components in Laravel Blade with automatic assets |
| 2026-10-22 06:33:50 | [gcego/runtime](https://www.nuget.org/packages/gcego%2Fruntime) | v1.0.0 | Atangageih Leke Collins | Execution kernel for GCEGO Studio: operation dispatch, trusted execution contex… |
| 2026-10-22 06:46:13 | [novora/poka-yoke](https://www.nuget.org/packages/novora%2Fpoka-yoke) | v1.0.0 |  | Framework-independent precondition guards for PHP business operations. |
| 2026-10-22 07:03:40 | [blackaha/module-pricing-updater](https://www.nuget.org/packages/blackaha%2Fmodule-pricing-updater) | 1.0.0 | BlackAha | Keeps your Magento product prices in line with the prices you set in BlackAha:… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
