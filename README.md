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

## Latest list — 2026-11-09 08:20 UTC

New packages created between 2026-11-09 07:18 UTC and 2026-11-09 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T08-20-24-742206Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 07:33:58 | [serdominus/nova-poshta-api-2](https://www.nuget.org/packages/serdominus%2Fnova-poshta-api-2) | 0.3.0 | Serdominus; Team | PHP-клієнт для роботи з API 2.0 Нової пошти |
| 2026-11-09 07:44:27 | [hydrastat/dto-hydrator](https://www.nuget.org/packages/hydrastat%2Fdto-hydrator) | v1.0.0 |  | Framework-agnostic DTO hydrator with Laravel, CodeIgniter, and Symfony integrat… |
| 2026-11-09 07:56:21 | [vanda/core](https://www.nuget.org/packages/vanda%2Fcore) | v0.1.0 |  | Vanda core: screens, typed UI schema, state snapshots, actions and reactions fo… |
| 2026-11-09 07:57:49 | [fabianmichael/kirby-themekit](https://www.nuget.org/packages/fabianmichael%2Fkirby-themekit) | 1.0.0 | Fabian Michael | Tools for color themes |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
