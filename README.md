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

## Latest list — 2026-10-27 06:20 UTC

New packages created between 2026-10-27 05:21 UTC and 2026-10-27 06:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T06-20-54-598329Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 05:33:28 | [mujahidabbas/laravel-umpire](https://www.nuget.org/packages/mujahidabbas%2Flaravel-umpire) | v1.0.0 | Mujahid Abbas | Per-tool Gate authorization, tool-call audit events and a safe stale-client pur… |
| 2026-10-27 05:49:18 | [plasgos/crm-sdk](https://www.nuget.org/packages/plasgos%2Fcrm-sdk) | v2.0.0 | Plasgos | Official PHP SDK for the Plasgos CRM Api Integration API. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
