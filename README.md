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

## Latest list — 2026-11-05 05:21 UTC

New packages created between 2026-11-05 04:21 UTC and 2026-11-05 05:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T05-21-42-407112Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 04:58:21 | [themusicdev/eventbrite](https://www.nuget.org/packages/themusicdev%2Feventbrite) | v0.1.0 |  | Eventbrite API v3 client - PSR-18 HTTP, PSR-16 cache, framework agnostic |
| 2026-11-05 05:12:51 | [lara-pack/database-backup](https://www.nuget.org/packages/lara-pack%2Fdatabase-backup) | v1.0.0 | Bhagaskara | Scheduled database backups for Laravel, configured from .env: schedule, retenti… |
| 2026-11-05 05:16:59 | [rimba/knowledge](https://www.nuget.org/packages/rimba%2Fknowledge) | 1.1.0 |  | Controlled documents, learning and qualification for the Rimba application. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
