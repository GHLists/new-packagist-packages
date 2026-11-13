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

## Latest list — 2026-11-13 17:20 UTC

New packages created between 2026-11-13 16:22 UTC and 2026-11-13 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T17-20-14-275624Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 16:29:59 | [nowo-tech/migrations-kit-contracts](https://www.nuget.org/packages/nowo-tech%2Fmigrations-kit-contracts) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Contracts a bundle implements to declare its identity and access-key columns, s… |
| 2026-11-13 16:35:17 | [slaver/laravel-sluggable-redirect](https://www.nuget.org/packages/slaver%2Flaravel-sluggable-redirect) | 2.1.0 | Viacheslav Radionov; Freerk v… | Creates sluggable-history if slug created from laravel-sluggable-package by Spa… |
| 2026-11-13 16:54:17 | [solverr/solverr-php](https://www.nuget.org/packages/solverr%2Fsolverr-php) | v0.1.0 |  | Server SDK for the Solverr crypto payment API. |
| 2026-11-13 17:05:24 | [moncash-php/moncash-php](https://www.nuget.org/packages/moncash-php%2Fmoncash-php) | v0.1.0 |  | Unofficial PHP SDK for the Digicel MonCash API (Haiti) — OAuth, payment creatio… |
| 2026-11-13 17:11:36 | [verdient/data-fetch-planner](https://www.nuget.org/packages/verdient%2Fdata-fetch-planner) | 1.0.0 |  | Plans date-range queries across daily, monthly and yearly aggregates. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
