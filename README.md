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

## Latest list — 2026-11-12 14:21 UTC

New packages created between 2026-11-12 13:21 UTC and 2026-11-12 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T14-21-18-326601Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 13:23:05 | [pharaonic/laravel-deep-replicate](https://www.nuget.org/packages/pharaonic%2Flaravel-deep-replicate) | 13.0.0 | Moamen Eltouny (Raggi) | Replicate a chosen Eloquent relationship graph into new persisted records, with… |
| 2026-11-12 13:30:29 | [gratlinie/contao-gratreviews](https://www.nuget.org/packages/gratlinie%2Fcontao-gratreviews) | v0.1.1 | Gratlinie | GratReviews – Google-Bewertungen automatisch abrufen und im Stil von GratFrame… |
| 2026-11-12 13:42:11 | [nonini/protocol-netstring](https://www.nuget.org/packages/nonini%2Fprotocol-netstring) | v0.3.0 | Thomas Gelf | Simple NetString stream wrapper |
| 2026-11-12 13:55:02 | [rikthepixel/modeltyper](https://www.nuget.org/packages/rikthepixel%2Fmodeltyper) | v3.15 | rik den breejen | Generate TypeScript interfaces from Laravel Models |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
