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

## Latest list — 2026-10-29 07:21 UTC

New packages created between 2026-10-29 06:19 UTC and 2026-10-29 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T07-21-42-281Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 06:22:20 | [tikobus/php-binlog-async](https://www.nuget.org/packages/tikobus%2Fphp-binlog-async) | v0.1.0 | tikobus | MySQL replication-protocol client: register as a replica over amphp/socket and… |
| 2026-10-29 06:27:25 | [thekaziomar/laravel-smart-upload](https://www.nuget.org/packages/thekaziomar%2Flaravel-smart-upload) | v1.0.0 | Kazi Omar Faruk | A developer-first, zero-database file and chunk upload toolkit for Laravel with… |
| 2026-10-29 06:40:29 | [laramon/agent](https://www.nuget.org/packages/laramon%2Fagent) | v0.1.0 | Mohamed Sheeraz | Laramon agent: ships requests, queries, jobs, exceptions, logs and host resourc… |
| 2026-10-29 06:44:44 | [ahraihan/laravel-steadfast-courier](https://www.nuget.org/packages/ahraihan%2Flaravel-steadfast-courier) | v1.0.0 | AH-Raihan | Steadfast Courier API (18 endpoints) and Webhook integration for Laravel |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
