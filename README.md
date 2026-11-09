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

## Latest list — 2026-11-09 06:21 UTC

New packages created between 2026-11-09 05:20 UTC and 2026-11-09 06:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T06-21-27-958498Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 05:31:11 | [feedshine/gtin](https://www.nuget.org/packages/feedshine%2Fgtin) | v1.0.0 | FeedShine | Validate GTIN, UPC and EAN barcodes: length, GS1 mod-10 check digit and restric… |
| 2026-11-09 06:06:30 | [starbug/db](https://www.nuget.org/packages/starbug%2Fdb) | v0.10.0 | Ali Gangji | Starbug database module. |
| 2026-11-09 06:08:09 | [hipdevteam/ion-mu](https://www.nuget.org/packages/hipdevteam%2Fion-mu) | v3.5.6 | ION | ION MU — WordPress mu-plugin that fire-and-forgets activity events to Site Inte… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
