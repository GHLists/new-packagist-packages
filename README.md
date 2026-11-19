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

## Latest list — 2026-11-19 07:21 UTC

New packages created between 2026-11-19 06:21 UTC and 2026-11-19 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T07-21-29-358856Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 06:52:12 | [muhdaimans/identiq-ekyc](https://www.nuget.org/packages/muhdaimans%2Fidentiq-ekyc) | v0.1.0 |  | Laravel client for the IDentiQ eKYC API: onboarding journeys, results and signe… |
| 2026-11-19 07:07:32 | [toshkq93/laravel-boundaries](https://www.nuget.org/packages/toshkq93%2Flaravel-boundaries) | 0.0.1 | toshkq93 | Modular monolith for Laravel with enforced module boundaries: modules with thei… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
