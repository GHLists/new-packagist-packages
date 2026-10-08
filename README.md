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

## Latest list — 2026-10-08 06:20 UTC

New packages created between 2026-10-08 05:19 UTC and 2026-10-08 06:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T06-20-32-173777Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 05:19:34 | [basaltic-sh/sdk-php](https://www.nuget.org/packages/basaltic-sh%2Fsdk-php) | v0.1.3 |  | Official PHP SDK for the Basaltic cloud platform |
| 2026-10-08 05:37:11 | [antevemus/aspecification](https://www.nuget.org/packages/antevemus%2Faspecification) | v1.4.3 | Heliton Junior - CTO @ Anteve… | Enterprise Specification Pattern Framework for PHP 8.2+ (DDD, Notification Patt… |
| 2026-10-08 05:41:40 | [hipdevteam/ion-mu](https://www.nuget.org/packages/hipdevteam%2Fion-mu) | v3.3.1 | ION | ION MU — WordPress mu-plugin that fire-and-forgets activity events to Site Inte… |
| 2026-10-08 05:53:23 | [antlerslabs/ziggy-db](https://www.nuget.org/packages/antlerslabs%2Fziggy-db) | v0.1.0 | eXeis-ixt | Secure, read-only production database pulls for local development with industry… |
| 2026-10-08 06:07:54 | [patrickfischer/deltat](https://www.nuget.org/packages/patrickfischer%2Fdeltat) | 1.0.3 | Patrick Fischer | DeltaT lookup, sourced from https://maia.usno.navy.mil or fallback |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
