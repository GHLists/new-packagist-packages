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

## Latest list — 2026-10-20 08:21 UTC

New packages created between 2026-10-20 07:20 UTC and 2026-10-20 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T08-21-41-507231Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 07:40:46 | [oleksyuk/apaleo-php](https://www.nuget.org/packages/oleksyuk%2Fapaleo-php) | v0.1.0 | Maks Oleksyuk | Framework-agnostic PHP SDK for the Apaleo hotel PMS API |
| 2026-10-20 07:46:51 | [gopromotional/event-planner](https://www.nuget.org/packages/gopromotional%2Fevent-planner) | v1.0.1 | GoPromotional | Event countdown, planning timeline, giveaway quantities and print order-by date… |
| 2026-10-20 07:46:51 | [gopromotional/mugday](https://www.nuget.org/packages/gopromotional%2Fmugday) | v1.0.1 | GoPromotional | Caffeine tracker with half-life estimate, sleep-ready time and reusable-cup sta… |
| 2026-10-20 07:46:51 | [gopromotional/packlist](https://www.nuget.org/packages/gopromotional%2Fpacklist) | v1.0.1 | GoPromotional | Packing checklists with templates, per-night quantities and a Markdown format. |
| 2026-10-20 07:46:51 | [gopromotional/siplog](https://www.nuget.org/packages/gopromotional%2Fsiplog) | v1.0.1 | GoPromotional | Daily water goal estimate and a simple hydration log with streaks. |
| 2026-10-20 07:48:27 | [szenario/craft-firstlight](https://www.nuget.org/packages/szenario%2Fcraft-firstlight) | 1.0.0 |  | Automatic poster images for video assets. firstlight grabs a frame with ffmpeg,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
