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

## Latest list — 2026-11-01 06:19 UTC

New packages created between 2026-11-01 05:20 UTC and 2026-11-01 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T06-19-13-570307Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 05:41:57 | [epixel/licence-guard](https://www.nuget.org/packages/epixel%2Flicence-guard) | v1.0.0 |  | Checks a signed licence file before a Laravel application opens. |
| 2026-11-01 05:47:36 | [hipdevteam/ion-mu](https://www.nuget.org/packages/hipdevteam%2Fion-mu) | v3.5.3 | ION | ION MU — WordPress mu-plugin that fire-and-forgets activity events to Site Inte… |
| 2026-11-01 06:08:43 | [rulli/laravel-onedrive](https://www.nuget.org/packages/rulli%2Flaravel-onedrive) | v1.0.0 | Rulli Wuji Wijianto | Laravel package untuk OneDrive Personal (Microsoft account) dengan login perman… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
