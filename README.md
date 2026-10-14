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

## Latest list — 2026-10-14 22:22 UTC

New packages created between 2026-10-14 21:20 UTC and 2026-10-14 22:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T22-22-15-132812Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 21:22:17 | [kazistm/laravel-scoped-backup](https://www.nuget.org/packages/kazistm%2Flaravel-scoped-backup) | v0.0.2 | KaziSTM | Laravel backup and recovery package for full-database backups and scoped Eloque… |
| 2026-10-14 21:31:22 | [hometown/estimator](https://www.nuget.org/packages/hometown%2Festimator) | v2026.10.1 | Hometown Workforce, LLC | Price home-service jobs from text, photos or a conversation with the Hometown E… |
| 2026-10-14 21:41:58 | [iranimij/openimport](https://www.nuget.org/packages/iranimij%2Fopenimport) | v1.0.0 | Iman Aboheydary | OpenImport: import and export for Magento 2 with profiles, column mapping, valu… |
| 2026-10-14 22:04:11 | [goldnead/statamic-community](https://www.nuget.org/packages/goldnead%2Fstatamic-community) | v0.1.1 | Adrian Goldner | Community for Statamic: curated rooms, posts, comments and reactions, with a ch… |
| 2026-10-14 22:04:11 | [goldnead/statamic-directory](https://www.nuget.org/packages/goldnead%2Fstatamic-directory) | v0.1.1 | Adrian Goldner | Site-scoped public choir directory profiles for Statamic. |
| 2026-10-14 22:04:11 | [goldnead/statamic-messaging](https://www.nuget.org/packages/goldnead%2Fstatamic-messaging) | v0.1.1 | Adrian Goldner | Messaging for Statamic: conversations between people and teams, with anonymous… |
| 2026-10-14 22:09:11 | [filagora/filagora-compliance](https://www.nuget.org/packages/filagora%2Ffilagora-compliance) | v0.1.0 |  | Cookie consent, policy versions and privacy requests (export and erasure) for F… |
| 2026-10-14 22:10:00 | [marcelofecchio/safe2pay-api](https://www.nuget.org/packages/marcelofecchio%2Fsafe2pay-api) | v0.1.0 | Marcelo Fecchio | Componente PHP enxuto para a API da Safe2Pay: Pix, cartão de crédito (à vista o… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
