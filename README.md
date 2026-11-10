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

## Latest list — 2026-11-10 14:19 UTC

New packages created between 2026-11-10 13:21 UTC and 2026-11-10 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T14-19-32-705216Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 13:43:04 | [sanvalabs/bd-phone-validator](https://www.nuget.org/packages/sanvalabs%2Fbd-phone-validator) | v1.0.1 | Sanvalabs | Validate, format and detect the operator of Bangladeshi mobile numbers in Larav… |
| 2026-11-10 13:53:19 | [decisions-ai/laravel](https://www.nuget.org/packages/decisions-ai%2Flaravel) | v0.1.0 |  | A Laravel client for decisions.site monitoring. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
