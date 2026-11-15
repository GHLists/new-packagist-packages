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

## Latest list — 2026-11-15 00:22 UTC

New packages created between 2026-11-14 23:21 UTC and 2026-11-15 00:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T00-22-19-353207Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 23:30:08 | [bear/query-repository-graph](https://www.nuget.org/packages/bear%2Fquery-repository-graph) | 0.1.0 | Akihito Koriyama | Static analysis of the cache graph that BEAR.QueryRepository attributes declare |
| 2026-11-14 23:43:40 | [influxit/build-assets](https://www.nuget.org/packages/influxit%2Fbuild-assets) | v0.1.0 |  | Package compiled frontend assets into a ZIP and deploy them with Laravel or pla… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
