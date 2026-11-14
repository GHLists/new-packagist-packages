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

## Latest list — 2026-11-14 10:20 UTC

New packages created between 2026-11-14 09:20 UTC and 2026-11-14 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T10-20-11-788633Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 09:23:16 | [pitchayakit/carbon-buddhist-era](https://www.nuget.org/packages/pitchayakit%2Fcarbon-buddhist-era) | v1.0.0 |  | Makes Carbon's translatedFormat() show the Buddhist Era year (CE + 543) in Thai… |
| 2026-11-14 09:31:07 | [schema-resume/validator](https://www.nuget.org/packages/schema-resume%2Fvalidator) | v1.3.3 | Schema Resume; Tradik | JSON Schema validator for Schema Resume - comprehensive CV/Resume validation wi… |
| 2026-11-14 09:32:14 | [itmosoft/laravel-search](https://www.nuget.org/packages/itmosoft%2Flaravel-search) | v1.0.1 |  | Database-backed model search indexing and querying for Laravel applications. |
| 2026-11-14 10:06:09 | [samt/nass](https://www.nuget.org/packages/samt%2Fnass) | v0.1.0 | Samt Software | Arabic text normalization and diacritic-insensitive search for Quran, hadith an… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
