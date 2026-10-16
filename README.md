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

## Latest list — 2026-10-16 00:20 UTC

New packages created between 2026-10-15 23:20 UTC and 2026-10-16 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T00-20-29-626436Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 23:26:22 | [wilycode/template-translation](https://www.nuget.org/packages/wilycode%2Ftemplate-translation) | v0.1.0 | Simon Piter | Translation and locale formatting filters for WilyCode Template, with view-awar… |
| 2026-10-15 23:48:37 | [wilycode/template-assets](https://www.nuget.org/packages/wilycode%2Ftemplate-assets) | v0.1.0 | Simon Piter | Page-scoped CSS and JavaScript asset collection, versioning, bundling, and mini… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
