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

## Latest list — 2026-10-25 04:18 UTC

New packages created between 2026-10-25 03:19 UTC and 2026-10-25 04:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T04-18-57-479664Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 03:37:41 | [gtpyyx/phpdb](https://www.nuget.org/packages/gtpyyx%2Fphpdb) | v1.0.0 | gtpeyy | php db tools for pdo |
| 2026-10-25 04:03:48 | [seatschart/seatschart-php](https://www.nuget.org/packages/seatschart%2Fseatschart-php) | v0.1.0 | SeatsChart | Official SeatsChart PHP SDK for the SeatsChart seating API: seat maps, holds, r… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
