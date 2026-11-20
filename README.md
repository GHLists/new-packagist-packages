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

## Latest list — 2026-11-20 12:19 UTC

New packages created between 2026-11-20 11:21 UTC and 2026-11-20 12:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T12-19-55-831138Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 11:34:36 | [empiricompany/maho-onepage-checkout-stylish](https://www.nuget.org/packages/empiricompany%2Fmaho-onepage-checkout-stylish) | 1.0.0 |  | One-step checkout style presets for Maho: every step in the left column, the or… |
| 2026-11-20 11:48:44 | [mapsight/pulp-ogc](https://www.nuget.org/packages/mapsight%2Fpulp-ogc) | v1.0.0 | Paul Golmann | Read OGC Web Feature Services (WFS) as GeoJSON in Pulp pipelines, with paging a… |
| 2026-11-20 12:03:35 | [winglet/core](https://www.nuget.org/packages/winglet%2Fcore) | v0.13.0-RC4 | Winglet | Winglet Core Framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
