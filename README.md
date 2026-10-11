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

## Latest list — 2026-10-11 00:22 UTC

New packages created between 2026-10-10 23:20 UTC and 2026-10-11 00:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T00-22-03-88475Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 23:33:32 | [elephentity/codegen-tsquid](https://www.nuget.org/packages/elephentity%2Fcodegen-tsquid) | v0.1.0 |  | Tsquid manifest builder and standalone PHP initial-data integration. |
| 2026-10-10 23:51:56 | [tusk-framework/framework](https://www.nuget.org/packages/tusk-framework%2Fframework) | v0.3.2 |  | The Tusk Framework - Domain-first PHP application framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
