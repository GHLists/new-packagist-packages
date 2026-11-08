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

## Latest list — 2026-11-08 01:21 UTC

New packages created between 2026-11-08 00:21 UTC and 2026-11-08 01:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T01-21-25-92046Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 01:09:56 | [peterwilsoncc/code-bin-block](https://www.nuget.org/packages/peterwilsoncc%2Fcode-bin-block) | 1.1.0 | Peter Wilson | Code Bin Block. |
| 2026-11-08 01:16:48 | [tribble/core](https://www.nuget.org/packages/tribble%2Fcore) | 1.0.0 | Alex Brindley | The core package for tribble |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
