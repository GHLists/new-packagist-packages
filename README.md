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

## Latest list — 2026-10-19 19:20 UTC

New packages created between 2026-10-19 18:23 UTC and 2026-10-19 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T19-20-28-370684Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 18:31:36 | [egsn/module-featured-product](https://www.nuget.org/packages/egsn%2Fmodule-featured-product) | 1.0.0 |  | Egsn Featured Product module for Magento 2: featured product box on the homepag… |
| 2026-10-19 18:33:51 | [gsu-cetloe/gadget-console-php](https://www.nuget.org/packages/gsu-cetloe%2Fgadget-console-php) | v1 | Jeb Barger | Gadget library for Symfony console apps: a logging-aware command base, a shell… |
| 2026-10-19 18:51:03 | [cleanplugins/scoper](https://www.nuget.org/packages/cleanplugins%2Fscoper) | 0.1.0 | CleanPlugins | Scope Composer dependencies and build a production package tree without collisi… |
| 2026-10-19 18:54:35 | [gsu-cetloe/gadget-oracle-php](https://www.nuget.org/packages/gsu-cetloe%2Fgadget-oracle-php) | v1 | Jeb Barger | Gadget library for Oracle Database: Symfony console commands that wrap SQL*Plus… |
| 2026-10-19 18:56:42 | [x-laravel/followable](https://www.nuget.org/packages/x-laravel%2Ffollowable) | v1.0.0 | Mehmet ÖĞMEN | Follows for Eloquent models with polymorphic followers, follow requests, mutual… |
| 2026-10-19 19:00:08 | [manuxi/sulu-content-transfer-bundle](https://www.nuget.org/packages/manuxi%2Fsulu-content-transfer-bundle) | 1.0.0 |  | Export and import of Sulu content (articles) between Sulu systems as a single p… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
