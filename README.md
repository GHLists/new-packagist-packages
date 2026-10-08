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

## Latest list — 2026-10-08 13:21 UTC

New packages created between 2026-10-08 12:18 UTC and 2026-10-08 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T13-21-12-0538Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 12:21:13 | [lekoala/kaly-forms](https://www.nuget.org/packages/lekoala%2Fkaly-forms) | 0.1.0 | Thomas | Small framework-independent server-first forms DSL with progressive enhancement… |
| 2026-10-08 12:39:35 | [codalaya/php-project-install-wizard](https://www.nuget.org/packages/codalaya%2Fphp-project-install-wizard) | v1.0.1 | Rajesh Chaurasiya | Web installer for Laravel products: requirements, permissions, database, option… |
| 2026-10-08 12:39:43 | [wmd/craft-design-field](https://www.nuget.org/packages/wmd%2Fcraft-design-field) | 1.0.1 | WMD | One field for every design option of a block: tone, spacing, layout, columns an… |
| 2026-10-08 12:42:04 | [tilscn/laravel-starter](https://www.nuget.org/packages/tilscn%2Flaravel-starter) | 12.0.0 | tilscn | A Laravel package for various utilities and features. |
| 2026-10-08 12:51:12 | [wexample/symfony-media](https://www.nuget.org/packages/wexample%2Fsymfony-media) | 1.0.1 |  |  |
| 2026-10-08 12:52:01 | [wexample/symfony-media-ds](https://www.nuget.org/packages/wexample%2Fsymfony-media-ds) | 1.0.1 |  |  |
| 2026-10-08 12:52:53 | [youmad/endurance-fit-repair](https://www.nuget.org/packages/youmad%2Fendurance-fit-repair) | v0.1.0 |  | Preserving FIT activity repair with JSON audit reports |
| 2026-10-08 12:53:07 | [wexample/symfony-media-demo](https://www.nuget.org/packages/wexample%2Fsymfony-media-demo) | 1.0.1 |  |  |
| 2026-10-08 13:04:54 | [nodexstudiovn/installer](https://www.nuget.org/packages/nodexstudiovn%2Finstaller) | 1.0.2 | Nguyễn Anh Kiệt | The official CLI project installer for NodeX Studio Framework v1.1.0. |
| 2026-10-08 13:04:54 | [rishadblack/wire-bootstrap](https://www.nuget.org/packages/rishadblack%2Fwire-bootstrap) | 1.0.0 | S M Rishad | Livewire-native Bootstrap 5.3 UI: one artisan command sets up Bootstrap, Vite a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
