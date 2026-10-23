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

## Latest list — 2026-10-23 19:20 UTC

New packages created between 2026-10-23 18:21 UTC and 2026-10-23 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T19-20-13-789727Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 18:22:27 | [backgammon-network/engine](https://www.nuget.org/packages/backgammon-network%2Fengine) | v0.1.0 |  | A framework-free PHP backgammon engine: board, legal moves, dice and a match ta… |
| 2026-10-23 18:23:07 | [amjadiqbal/laravel-pennant-experiments](https://www.nuget.org/packages/amjadiqbal%2Flaravel-pennant-experiments) | v0.1.0 | Amjad Iqbal | A/B and multivariate testing for Laravel Pennant: define experiments with weigh… |
| 2026-10-23 18:24:34 | [42lizard/catppuccin](https://www.nuget.org/packages/42lizard%2Fcatppuccin) | v0.1.1 |  | The four Catppuccin flavours for the TYPO3 v14 backend |
| 2026-10-23 18:52:00 | [tenma/postgres](https://www.nuget.org/packages/tenma%2Fpostgres) | v0.1.0 |  | A Postgres server of the app's own on Tenma: started next to the app through a… |
| 2026-10-23 18:52:24 | [woocommerce/php-stubs](https://www.nuget.org/packages/woocommerce%2Fphp-stubs) | v2026.10.23.1 |  | PHP stub declarations of WooCommerce extensions, for static analysis of code th… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
