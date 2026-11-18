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

## Latest list — 2026-11-18 21:22 UTC

New packages created between 2026-11-18 20:19 UTC and 2026-11-18 21:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T21-22-37-210278Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 20:27:35 | [webwizardsusa/filament-resource-browser](https://www.nuget.org/packages/webwizardsusa%2Ffilament-resource-browser) | v0.1.0 | Jamie Holly | Browse, select and create the records of one Filament resource from another, in… |
| 2026-11-18 20:47:24 | [korin/gedcom-cli](https://www.nuget.org/packages/korin%2Fgedcom-cli) | v0.1.0 |  | Command-line tool for GEDCOM files: info, validate, convert and diff, built on… |
| 2026-11-18 21:00:07 | [code-redlich/quick-add-cart](https://www.nuget.org/packages/code-redlich%2Fquick-add-cart) | 1.0.0 | CodeRedlich | Add Products via name or product number to cart in checkout or card modal. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
