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

## Latest list — 2026-10-05 01:19 UTC

New packages created between 2026-10-05 00:19 UTC and 2026-10-05 01:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T01-19-11-817668Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 00:26:24 | [mage2kishan/module-smart-badge](https://www.nuget.org/packages/mage2kishan%2Fmodule-smart-badge) | 1.1.8 |  | Smart Product Badge & Label System - Automatically displays beautiful badges on… |
| 2026-10-05 00:29:46 | [boysfromthefactory/groundhog](https://www.nuget.org/packages/boysfromthefactory%2Fgroundhog) | v0.1.0 | Balazs Sebesteny | Declarative recurring Eloquent models backed by RFC 5545 rules. |
| 2026-10-05 01:10:34 | [atlas-auth/atlas-php](https://www.nuget.org/packages/atlas-auth%2Fatlas-php) | v0.1.0 |  | Official PHP backend SDK for Atlas — the secret-key Backend API client plus ses… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
