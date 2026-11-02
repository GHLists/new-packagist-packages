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

## Latest list — 2026-11-02 00:18 UTC

New packages created between 2026-11-01 23:20 UTC and 2026-11-02 00:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T00-18-30-580556Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 23:37:11 | [vagabit/fos-js-routing-security-bundle](https://www.nuget.org/packages/vagabit%2Ffos-js-routing-security-bundle) | v1.0.0 | Martino Piccinato | Role-filtered and security.yaml access-control-aware route exposure for FOSJsRo… |
| 2026-11-02 00:01:45 | [polidog/rosanna](https://www.nuget.org/packages/polidog%2Frosanna) | v0.1.0 | polidog | Server-side PHP components in the shape of React: H, Element, Renderer and the… |
| 2026-11-02 00:03:08 | [wapplersystems/mapmagic](https://www.nuget.org/packages/wapplersystems%2Fmapmagic) | 14.1.1 | WapplerSystems; TYPO3 Core Te… | TYPO3 Map Magic - Flexible TYPO3 map framework. |
| 2026-11-02 00:03:25 | [polidog/rosanna-defer](https://www.nuget.org/packages/polidog%2Frosanna-defer) | v0.1.1 | polidog | Deferred fragments for Rosanna: placeholders, a GET endpoint, client caching an… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
