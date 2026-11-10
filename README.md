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

## Latest list — 2026-11-10 16:20 UTC

New packages created between 2026-11-10 15:21 UTC and 2026-11-10 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T16-20-52-146105Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 15:25:49 | [filafly/filament-remix-icons](https://www.nuget.org/packages/filafly%2Ffilament-remix-icons) | v1.0.0 | Nolan Nordlund | Remix Icon pack for Filament Icons: replaces every Filament UI icon with Remix… |
| 2026-11-10 15:31:35 | [thepublicgood/analytics](https://www.nuget.org/packages/thepublicgood%2Fanalytics) | v0.1.0 |  | Send page views, requests and custom events to thepublicgood.analytics from PHP… |
| 2026-11-10 16:06:41 | [ernestdefoe/bingo](https://www.nuget.org/packages/ernestdefoe%2Fbingo) | 1.0.0 | Ernest Defoe | Bingo: play along with live events. Each member gets their own shuffled 5×5 car… |
| 2026-11-10 16:07:35 | [ernestdefoe/tier-lists](https://www.nuget.org/packages/ernestdefoe%2Ftier-lists) | 1.0.0 | Ernest Defoe | Tier Lists: members rank anything by dragging it into S to F rows, remix each o… |
| 2026-11-10 16:14:29 | [shusaura85/odoo-json2-php](https://www.nuget.org/packages/shusaura85%2Fodoo-json2-php) | v1.0.1 | Shu Saura | Simple PHP client library for Odoo JSON-2 API (Odoo 19+) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
