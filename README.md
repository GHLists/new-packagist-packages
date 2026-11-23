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

## Latest list — 2026-11-23 06:18 UTC

New packages created between 2026-11-23 05:18 UTC and 2026-11-23 06:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T06-18-34-322754Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 05:28:18 | [js-upup/exploded-view-brief](https://www.nuget.org/packages/js-upup%2Fexploded-view-brief) | v0.1.0 |  | Turn an ordered parts list, layout axis and fixed assemblies into a product ill… |
| 2026-11-23 05:45:10 | [webicorns/pongback](https://www.nuget.org/packages/webicorns%2Fpongback) | 0.9.0 | Michael Blunck; Philipp Thiele | TYPO3 extension for sending and receiving Pingbacks |
| 2026-11-23 06:15:18 | [thb/concurrency](https://www.nuget.org/packages/thb%2Fconcurrency) | v1.0 |  | Webman plugin: multi-port HTTP concurrency workers with round-robin client |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
