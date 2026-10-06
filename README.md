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

## Latest list — 2026-10-06 20:20 UTC

New packages created between 2026-10-06 19:20 UTC and 2026-10-06 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T20-20-20-695896Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 19:30:31 | [indianos/alt-dto](https://www.nuget.org/packages/indianos%2Falt-dto) | 1.0.0 |  | Framework-agnostic DTO hydration and serialization library |
| 2026-10-06 19:41:10 | [dirthara/cache](https://www.nuget.org/packages/dirthara%2Fcache) | 0.1.0 | Dirthara | PSR-6 and PSR-16 caching for PHP and the Dirthara framework |
| 2026-10-06 19:43:01 | [letkode/config-publisher](https://www.nuget.org/packages/letkode%2Fconfig-publisher) | 1.0.0 |  | Publishes the example config files that letkode/* packages ship, with a single… |
| 2026-10-06 19:49:52 | [freepeace13/inertia-live-laravel](https://www.nuget.org/packages/freepeace13%2Finertia-live-laravel) | v0.1.0 |  | Live Inertia pages driven by Spatie Event Sourcing projections. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
