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

## Latest list — 2026-10-30 03:20 UTC

New packages created between 2026-10-30 02:19 UTC and 2026-10-30 03:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T03-20-05-516053Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 02:33:01 | [payene/maintenance-bundle](https://www.nuget.org/packages/payene%2Fmaintenance-bundle) | v1.0.0 | Payene | Mode maintenance pour Symfony avec interface d'administration, whitelist et sto… |
| 2026-10-30 03:16:55 | [sanjayacloud/laravel-plans](https://www.nuget.org/packages/sanjayacloud%2Flaravel-plans) | 0.5.0 | Sanjaya | Free and paid plans for Laravel: feature gating, usage limits, free trials, com… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
