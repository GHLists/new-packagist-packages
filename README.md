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

## Latest list — 2026-10-23 06:19 UTC

New packages created between 2026-10-23 05:22 UTC and 2026-10-23 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T06-19-59-83837Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 05:25:08 | [projectsaturnstudios/rocketship](https://www.nuget.org/packages/projectsaturnstudios%2Frocketship) | v0.10.0 | Angel Gonzalez; Taylor Otwell | Drop-in replacement for Laravel Octane, with a native server on epoll/kqueue: n… |
| 2026-10-23 05:41:12 | [djouamaah/laravel-algeria-invoice](https://www.nuget.org/packages/djouamaah%2Flaravel-algeria-invoice) | v1.0.0 | Djouamaa | Algerian invoices for Laravel: VAT, cash stamp duty (Finance Law 2025), mandato… |
| 2026-10-23 05:43:24 | [junthink/dcat-admin](https://www.nuget.org/packages/junthink%2Fdcat-admin) | v3.0.0 | jqh; junthink | Maintained Dcat Admin fork for Laravel 13 |
| 2026-10-23 06:08:23 | [rasuvaeff/json-ld](https://www.nuget.org/packages/rasuvaeff%2Fjson-ld) | v0.1.0 | Victor Razuvaev | JSON-LD 1.1 processor for PHP: expand, flatten, node API, RDF and N-Quads |
| 2026-10-23 06:15:51 | [eloquage/filament-horizon](https://www.nuget.org/packages/eloquage%2Ffilament-horizon) | v1.0.0 | Miguel Enes | Filament dashboard pages and widgets for monitoring Laravel Horizon queues. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
