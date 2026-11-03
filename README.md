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

## Latest list — 2026-11-03 08:19 UTC

New packages created between 2026-11-03 07:21 UTC and 2026-11-03 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T08-19-02-424703Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 07:29:46 | [dwiky-danov/business-error-handler](https://www.nuget.org/packages/dwiky-danov%2Fbusiness-error-handler) | v1.0.0 |  | Framework-agnostic global error handling with safe API responses and optional K… |
| 2026-11-03 07:48:43 | [desu-php/shoppingcart](https://www.nuget.org/packages/desu-php%2Fshoppingcart) | v5.0.0 | Rob Gloudemans; Patrick Henni… | Session and database shopping carts for Laravel, with discounts, taxes and mult… |
| 2026-11-03 07:51:42 | [eloquage/laravel-cache-swoole-table](https://www.nuget.org/packages/eloquage%2Flaravel-cache-swoole-table) | v0.1.1 |  | A Laravel Cache driver using Swoole\Table for shared memory storage. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
