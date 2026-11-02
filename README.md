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

## Latest list — 2026-11-02 08:20 UTC

New packages created between 2026-11-02 07:21 UTC and 2026-11-02 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T08-20-23-112616Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 07:39:11 | [laraveladmin/sharding](https://www.nuget.org/packages/laraveladmin%2Fsharding) | 1.0.0 | laraveladmin | Declarative logical table sharding for Hyperf models: time or capacity modes, t… |
| 2026-11-02 07:44:01 | [toppng/png-alpha-benchmark-toolkit](https://www.nuget.org/packages/toppng%2Fpng-alpha-benchmark-toolkit) | v1.0.2 | Islam Gamal | Lossless ISO/IEC 15948 PNG Alpha-Channel Analysis, Scanline Filter Optimization… |
| 2026-11-02 08:11:46 | [anjan-talukdar/laravel-sweep](https://www.nuget.org/packages/anjan-talukdar%2Flaravel-sweep) | v1.0.0 | Anjan Talukdar | A powerful, multi-database, storage-agnostic data purging and sequence reset li… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
