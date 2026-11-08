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

## Latest list — 2026-11-08 06:19 UTC

New packages created between 2026-11-08 05:19 UTC and 2026-11-08 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T06-19-45-420783Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 05:26:30 | [dipesh/date](https://www.nuget.org/packages/dipesh%2Fdate) | v1.0.0 | dipesh pokhrel | System-level BS (Bikram Sambat) date value object for PHP: parsing, components,… |
| 2026-11-08 05:36:01 | [fraudnova/fraudnova-php](https://www.nuget.org/packages/fraudnova%2Ffraudnova-php) | v1.0.1 | FraudNova | Official PHP client for the FraudNova fraud-detection API: fraud scores and ris… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
