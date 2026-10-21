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

## Latest list — 2026-10-21 01:21 UTC

New packages created between 2026-10-21 00:20 UTC and 2026-10-21 01:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T01-21-36-479082Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 00:22:54 | [gcego/registry](https://www.nuget.org/packages/gcego%2Fregistry) | v1.0.0 | Atangageih Leke Collins | Definition discovery, registration, resolution and production caching for GCEGO… |
| 2026-10-21 00:28:25 | [ad-go/sync](https://www.nuget.org/packages/ad-go%2Fsync) | v1.0.0 | k | Active-active database synchronisation for two CodeIgniter 4 instances over HTT… |
| 2026-10-21 00:58:16 | [clingen-data-model/laravel-schedule-ketchup](https://www.nuget.org/packages/clingen-data-model%2Flaravel-schedule-ketchup) | v1.0.0 |  | Run Laravel scheduled tasks whose scheduled time has passed since they last ran… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
