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

## Latest list — 2026-10-29 05:20 UTC

New packages created between 2026-10-29 04:20 UTC and 2026-10-29 05:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T05-20-42-523917Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 04:37:40 | [wayancc/wyn-forms](https://www.nuget.org/packages/wayancc%2Fwyn-forms) | v1.0.0 |  | Self-hosted form backend: spam-filtered inbox, notifications and uploads for an… |
| 2026-10-29 04:41:13 | [abetwothree/lang-export](https://www.nuget.org/packages/abetwothree%2Flang-export) | v0.1.0 | Abraham Arango | Export your Laravel translation files as JSON for Vue, React, & Svelte with @to… |
| 2026-10-29 04:54:52 | [tryrelia/relia](https://www.nuget.org/packages/tryrelia%2Frelia) | v0.1.0 |  | Relia for PHP and Laravel: requests, errors, database queries, outgoing calls,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
