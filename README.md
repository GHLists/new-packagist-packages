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

## Latest list — 2026-09-30 01:19 UTC

New packages created between 2026-09-30 00:20 UTC and 2026-09-30 01:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T01-19-54-849806Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 00:30:53 | [totara/lightsaml](https://www.nuget.org/packages/totara%2Flightsaml) | 4.1.6.3 |  |  |
| 2026-09-30 00:42:03 | [mage2kishan/module-index-now](https://www.nuget.org/packages/mage2kishan%2Fmodule-index-now) | 1.0.11 | Kishan Savaliya | Panth IndexNow — instantly notify Bing, Yandex and other search engines when co… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
