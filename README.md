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

## Latest list — 2026-11-23 16:21 UTC

New packages created between 2026-11-23 15:22 UTC and 2026-11-23 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T16-21-43-20574Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 15:24:41 | [timbaron/naija-tel](https://www.nuget.org/packages/timbaron%2Fnaija-tel) | v0.1.0 | Timothy Akiode | Nigerian Telecom Intelligence for Laravel |
| 2026-11-23 15:25:47 | [datacircle/gemini-php-tools](https://www.nuget.org/packages/datacircle%2Fgemini-php-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. Four function tools for the Gemini PHP client. The tool… |
| 2026-11-23 15:26:10 | [marshallu/herd-fpp](https://www.nuget.org/packages/marshallu%2Fherd-fpp) | v1.0.0 | Christopher McComas | Focal point picker for WordPress images. |
| 2026-11-23 15:36:32 | [youmad/endurance-activity-analysis](https://www.nuget.org/packages/youmad%2Fendurance-activity-analysis) | v0.1.0 |  | Streaming GPS distance, speed and movement estimates for recorded activities |
| 2026-11-23 15:36:35 | [youmad/endurance-geo](https://www.nuget.org/packages/youmad%2Fendurance-geo) | v0.1.0 |  | Streaming path geometry and spherical distance calculations |
| 2026-11-23 15:38:19 | [youmad/endurance-gpx](https://www.nuget.org/packages/youmad%2Fendurance-gpx) | v0.1.0 |  | Streaming GPX tracks, routes and waypoints for PHP |
| 2026-11-23 15:38:21 | [youmad/endurance-kml](https://www.nuget.org/packages/youmad%2Fendurance-kml) | v0.1.0 |  | Streaming KML 2.2 source inspection |
| 2026-11-23 15:38:25 | [youmad/endurance-workout](https://www.nuget.org/packages/youmad%2Fendurance-workout) | v0.1.0 |  | Immutable workout prescriptions with typed targets and bounded repeat occurrenc… |
| 2026-11-23 15:40:38 | [ignescent/loaded-dice](https://www.nuget.org/packages/ignescent%2Floaded-dice) | 1.0.0 | Michael Cordingley | Utilities for deterministic randomness. |
| 2026-11-23 15:53:40 | [konradmichalik/typo3-outbound](https://www.nuget.org/packages/konradmichalik%2Ftypo3-outbound) | 0.1.0 | Konrad Michalik | Outbound - Declarative API clients for TYPO3: describe external APIs as PHP int… |
| 2026-11-23 16:14:20 | [automattic/jetpack-announcements](https://www.nuget.org/packages/automattic%2Fjetpack-announcements) | v0.1.0 |  | A product-agnostic channel to tell Jetpack users what is new. |
| 2026-11-23 16:16:09 | [youmad/endurance-activity-gpx](https://www.nuget.org/packages/youmad%2Fendurance-activity-gpx) | v0.1.0 |  | GPX recorded tracks mapped to Endurance Activity import streams |
| 2026-11-23 16:16:12 | [youmad/endurance-route](https://www.nuget.org/packages/youmad%2Fendurance-route) | v0.1.0 |  | Routes, immutable content revisions and streaming publication contracts |
| 2026-11-23 16:16:16 | [youmad/endurance-workout-fit](https://www.nuget.org/packages/youmad%2Fendurance-workout-fit) | v0.1.0 |  | Explicit FIT Workout interpretation into immutable Endurance Workout prescripti… |
| 2026-11-23 16:16:19 | [youmad/endurance-workout-postgresql](https://www.nuget.org/packages/youmad%2Fendurance-workout-postgresql) | v0.1.0 |  | Atomic PostgreSQL publication and immutable Workout revision storage |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
