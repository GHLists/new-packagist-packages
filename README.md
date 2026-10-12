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

## Latest list — 2026-10-12 03:20 UTC

New packages created between 2026-10-12 02:20 UTC and 2026-10-12 03:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T03-20-19-383404Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 02:39:42 | [proesio/rutalo](https://www.nuget.org/packages/proesio%2Frutalo) | v1.0.0 | Juan Felipe Valencia Murillo | Rutalo - Enrutador en Español. |
| 2026-10-12 02:41:25 | [jewei/app-attest-php](https://www.nuget.org/packages/jewei%2Fapp-attest-php) | v0.1.0 | Jewei Mak | Verify Apple App Attest attestations and assertions in PHP, with no dependencie… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
