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

## Latest list — 2026-11-22 19:18 UTC

New packages created between 2026-11-22 18:18 UTC and 2026-11-22 19:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T19-18-43-947155Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 18:20:08 | [firasarafah/laronclad](https://www.nuget.org/packages/firasarafah%2Flaronclad) | v0.1.2-alpha | Firas Arafah | Runtime security sensor for Laravel: observes SQL queries and outbound requests… |
| 2026-11-22 19:00:10 | [crabphp/sentry](https://www.nuget.org/packages/crabphp%2Fsentry) | v0.1.0 |  | Error reporting for the Crab framework: errors the application logs, sent to Se… |
| 2026-11-22 19:01:37 | [foresi/skeleton](https://www.nuget.org/packages/foresi%2Fskeleton) | v0.1.0 |  | The starting point of a Foresi application: an open-source business system for… |
| 2026-11-22 19:03:48 | [shipswitch/shipswitch](https://www.nuget.org/packages/shipswitch%2Fshipswitch) | v0.1.0 | Arnaud Nicastro | PHP SDK for ShipSwitch feature flags |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
