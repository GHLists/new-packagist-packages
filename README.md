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

## Latest list — 2026-10-05 02:21 UTC

New packages created between 2026-10-05 01:19 UTC and 2026-10-05 02:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T02-21-27-542303Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 01:27:19 | [mage2kishan/module-testimonials](https://www.nuget.org/packages/mage2kishan%2Fmodule-testimonials) | 1.2.10 |  | Advanced Testimonials module with slider, individual pages, categories, SEO, an… |
| 2026-10-05 01:46:24 | [dirthara/queue-database](https://www.nuget.org/packages/dirthara%2Fqueue-database) | 0.1.0 | Dirthara | Database queue driver for the Dirthara framework |
| 2026-10-05 01:58:12 | [contenir/contenir-workflow](https://www.nuget.org/packages/contenir%2Fcontenir-workflow) | v0.1.0 | Contenir | Database-driven workflow system for Mezzio that generates routes and navigation… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
