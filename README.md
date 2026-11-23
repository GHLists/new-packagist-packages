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

## Latest list — 2026-11-23 20:19 UTC

New packages created between 2026-11-23 19:20 UTC and 2026-11-23 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T20-19-53-39659Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 19:38:29 | [soderlind/network-ai-connector](https://www.nuget.org/packages/soderlind%2Fnetwork-ai-connector) | 1.0.0 | Per Søderlind |  |
| 2026-11-23 19:41:46 | [koriym/mini-cache](https://www.nuget.org/packages/koriym%2Fmini-cache) | 1.0.0 | Akihito Koriyama | Simplest cache with no expiration |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
