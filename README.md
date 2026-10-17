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

## Latest list — 2026-10-17 01:19 UTC

New packages created between 2026-10-17 00:19 UTC and 2026-10-17 01:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T01-19-01-765446Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 00:56:45 | [waaiy/api](https://www.nuget.org/packages/waaiy%2Fapi) | 3.3.0 | Omer Selman Anadolulu | Waaiy API Connector |
| 2026-10-17 01:12:30 | [saucal/composer-patches](https://www.nuget.org/packages/saucal%2Fcomposer-patches) | v1.0.0 |  | Re-applies cweagans/composer-patches patches on install/update when patches.loc… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
