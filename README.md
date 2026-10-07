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

## Latest list — 2026-10-07 12:18 UTC

New packages created between 2026-10-07 11:20 UTC and 2026-10-07 12:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T12-18-56-185383Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 11:47:01 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.1.0 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-07 11:53:55 | [cyllene-digital/sylius-advanced-taxon-plugin](https://www.nuget.org/packages/cyllene-digital%2Fsylius-advanced-taxon-plugin) | v1.0.0 | Cyllene | Turns Sylius taxons into merchandising pages: branding, featured content, media… |
| 2026-10-07 12:03:38 | [kareylo/laravel-entity-routing](https://www.nuget.org/packages/kareylo%2Flaravel-entity-routing) | v0.1.0 | Kareylo | Entity routing for Laravel: fill every route placeholder from a single model, a… |
| 2026-10-07 12:11:36 | [wexample/symfony-charts-demo](https://www.nuget.org/packages/wexample%2Fsymfony-charts-demo) | 1.0.1 |  |  |
| 2026-10-07 12:12:19 | [wexample/symfony-charts-ds](https://www.nuget.org/packages/wexample%2Fsymfony-charts-ds) | 1.0.1 |  |  |
| 2026-10-07 12:15:25 | [kefyusuf/laravel-guarded-tools](https://www.nuget.org/packages/kefyusuf%2Flaravel-guarded-tools) | v0.1.0 | Yusuf Kef | Guarded tools and assurance tests for Laravel AI agents: workspace isolation, h… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
