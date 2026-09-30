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

## Latest list — 2026-09-30 21:21 UTC

New packages created between 2026-09-30 20:21 UTC and 2026-09-30 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T21-21-16-670079Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 20:28:26 | [jacerider/neo_migrate](https://www.nuget.org/packages/jacerider%2Fneo_migrate) | 1.0.0 | Cyle Carlson (JaceRider) | Moves a legacy site (paragraphs, micon, escort, real_favicon, aeon) onto the Ne… |
| 2026-09-30 20:40:07 | [lenorix/datadis-client](https://www.nuget.org/packages/lenorix%2Fdatadis-client) | v0.1.0 | Jesus Hernandez | PHP client for Datadis, the platform where Spanish electricity distributors pub… |
| 2026-09-30 20:40:54 | [chrisreedio/laravel-mdstaff-sdk](https://www.nuget.org/packages/chrisreedio%2Flaravel-mdstaff-sdk) | v1.0.0 | Chris Reed | Laravel SDK for querying the MDStaff (ASM Cloud) API |
| 2026-09-30 20:44:21 | [aimeos/pagible-webhooks](https://www.nuget.org/packages/aimeos%2Fpagible-webhooks) | 0.13.0 |  | Pagible CMS webhook delivery |
| 2026-09-30 20:59:31 | [shellrent/sdk](https://www.nuget.org/packages/shellrent%2Fsdk) | v0.1.0 |  | Official PHP SDK for the Shellrent public API |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
