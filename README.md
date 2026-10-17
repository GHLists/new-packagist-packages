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

## Latest list — 2026-10-17 23:19 UTC

New packages created between 2026-10-17 22:21 UTC and 2026-10-17 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T23-19-19-897549Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 22:27:36 | [amaggi/module-featured-product](https://www.nuget.org/packages/amaggi%2Fmodule-featured-product) | 1.0.0 |  | Amaggi Featured Product module for Magento 2: featured product box on the homep… |
| 2026-10-17 22:40:35 | [fast-forward/changelog](https://www.nuget.org/packages/fast-forward%2Fchangelog) | v0.1.0 | Felipe Sayao Lobato Abreu | Standalone changelog domain and CLI runtime for Fast Forward PHP packages. |
| 2026-10-17 22:49:01 | [1994/social-images-craft](https://www.nuget.org/packages/1994%2Fsocial-images-craft) | v1.0.1 | 1994 | Social share images for Craft CMS: design Open Graph cards in the control panel… |
| 2026-10-17 22:53:29 | [mohannadelemary/laravel-unique-job-locks](https://www.nuget.org/packages/mohannadelemary%2Flaravel-unique-job-locks) | v0.1.0 | Mohannad Elemary | Find out why a ShouldBeUnique job won't dispatch: list and explain the unique-j… |
| 2026-10-17 22:54:56 | [phoenix1331/laravel-ai-headroom-ledger](https://www.nuget.org/packages/phoenix1331%2Flaravel-ai-headroom-ledger) | v0.1.0 | Darren Williams | Store and query per-request AI token usage and cost from Headroom. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
