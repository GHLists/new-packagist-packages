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

## Latest list — 2026-11-23 17:20 UTC

New packages created between 2026-11-23 16:21 UTC and 2026-11-23 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T17-20-22-577897Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 16:30:35 | [mockcard/mockcard-php](https://www.nuget.org/packages/mockcard%2Fmockcard-php) | v2.0.0 | Arixeva Labs | MockCard SDK for PHP: chaos runs in CI, payment webhook checks and the producti… |
| 2026-11-23 16:30:40 | [davereid/drush-helper](https://www.nuget.org/packages/davereid%2Fdrush-helper) | v0.1.0 |  | Helpful Drush commands. |
| 2026-11-23 16:32:12 | [pharaonic/laravel-api-versioning](https://www.nuget.org/packages/pharaonic%2Flaravel-api-versioning) | 13.0.2 | Moamen Eltouny (Raggi) | Laravel-native API versioning: version groups and constraints on Route, header,… |
| 2026-11-23 16:35:42 | [youmad/endurance-route-fit](https://www.nuget.org/packages/youmad%2Fendurance-route-fit) | v0.1.0 |  | Streaming FIT Course validation and staged Endurance Route mapping |
| 2026-11-23 16:35:45 | [youmad/endurance-route-gpx](https://www.nuget.org/packages/youmad%2Fendurance-route-gpx) | v0.1.0 |  | Selected GPX recorded track geometry for immutable Endurance Route revisions |
| 2026-11-23 16:35:48 | [youmad/endurance-route-kml](https://www.nuget.org/packages/youmad%2Fendurance-route-kml) | v0.1.0 |  | KML path interpretation for immutable Route revisions |
| 2026-11-23 16:35:51 | [youmad/endurance-route-postgresql](https://www.nuget.org/packages/youmad%2Fendurance-route-postgresql) | v0.1.0 |  | PostgreSQL storage for immutable route revisions and bounded streams |
| 2026-11-23 16:44:37 | [kristos80/mule](https://www.nuget.org/packages/kristos80%2Fmule) | v1.0.0 |  | A committed, content-hashed verdict cache for PHP mutation testing: mutate only… |
| 2026-11-23 16:51:31 | [cairophp/laravel-octane](https://www.nuget.org/packages/cairophp%2Flaravel-octane) | v0.1.0 |  | Run Laravel Octane on the Cairo application server |
| 2026-11-23 17:01:31 | [goodport/mail-tracker](https://www.nuget.org/packages/goodport%2Fmail-tracker) | v1.1.0 | Goodport; J David Baker | Log and track outgoing Laravel emails with per-type retention and a built-in ad… |
| 2026-11-23 17:05:52 | [atwx/silverstripe-error-reporting](https://www.nuget.org/packages/atwx%2Fsilverstripe-error-reporting) | v1.0.0 |  | Report real errors of Silverstripe sites to Sentry/GlitchTip: errors and fatals… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
