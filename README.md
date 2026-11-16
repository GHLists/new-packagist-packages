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

## Latest list — 2026-11-16 02:22 UTC

New packages created between 2026-11-16 01:19 UTC and 2026-11-16 02:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T02-22-16-584406Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 01:52:50 | [mgamadeus/ddd-site-insights](https://www.nuget.org/packages/mgamadeus%2Fddd-site-insights) | 0.1.0-rc.2 | Marius-Eugen Gerdan | Search Console insights for mgamadeus/ddd: reads Google Search Console through… |
| 2026-11-16 01:58:25 | [thebeardedbear/urssaf-tierce-declaration-cesu](https://www.nuget.org/packages/thebeardedbear%2Furssaf-tierce-declaration-cesu) | v0.1.0 | The Bearded Bear | Client and domain model for the URSSAF "API Tierce Déclaration CESU" (third-par… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
