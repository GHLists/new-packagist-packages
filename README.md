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

## Latest list — 2026-10-21 21:21 UTC

New packages created between 2026-10-21 20:21 UTC and 2026-10-21 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T21-21-11-73155Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 20:33:48 | [hryvinskyi/magento2-admin-action-log](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-admin-action-log) | 1.0.0 | Volodymyr Hryvinskyi | Records admin requests and entity changes (before and after, per field) into th… |
| 2026-10-21 20:51:38 | [solophp/input](https://www.nuget.org/packages/solophp%2Finput) | v1.0.0-RC1 | Vitaliy Olos | Typed, validated input DTOs for PHP 8.3+: immutable classes built through their… |
| 2026-10-21 21:05:22 | [afaztech/linops](https://www.nuget.org/packages/afaztech%2Flinops) | v0.1.0 |  | Production-ready asynchronous PHP library for Linux server management over SSH |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
