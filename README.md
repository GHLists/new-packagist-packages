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

## Latest list — 2026-10-04 12:20 UTC

New packages created between 2026-10-04 11:20 UTC and 2026-10-04 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T12-20-29-769244Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 11:31:46 | [pnscripts/pn-invoice](https://www.nuget.org/packages/pnscripts%2Fpn-invoice) | v0.1.0 | PN Scripts | PN Invoice: framework-agnostic PHP library to generate and validate EN 16931 e-… |
| 2026-10-04 11:35:11 | [trademinator/bcmath](https://www.nuget.org/packages/trademinator%2Fbcmath) | v0.1.0 |  | Framework-agnostic BCMath helpers and precision utilities for PHP. |
| 2026-10-04 11:41:43 | [kerigard/laravel-stubs](https://www.nuget.org/packages/kerigard%2Flaravel-stubs) | v1.0.0 | Vladislav Sidelnikov | Custom stub templates for Laravel projects. |
| 2026-10-04 12:06:58 | [mage2kishan/module-live-activity](https://www.nuget.org/packages/mage2kishan%2Fmodule-live-activity) | 1.0.15 | Kishan Savaliya | Live Activity & Social Proof notifications for Magento 2. Shows real-time custo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
