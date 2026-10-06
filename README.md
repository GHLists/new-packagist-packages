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

## Latest list — 2026-10-06 01:20 UTC

New packages created between 2026-10-06 00:20 UTC and 2026-10-06 01:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T01-20-15-636146Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 00:21:10 | [rohang27/thesportsdb-client](https://www.nuget.org/packages/rohang27%2Fthesportsdb-client) | v0.1.0 | RohanG27 | PHP client for TheSportsDB API v1 and v2: typed models, rate limiting, retries,… |
| 2026-10-06 01:12:42 | [pushinbr/pam-native-charts](https://www.nuget.org/packages/pushinbr%2Fpam-native-charts) | v0.1.0 |  | Native charts for PAM Native: line, area, bar, donut, sparkline and progress ri… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
