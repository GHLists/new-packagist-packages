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

## Latest list — 2026-10-19 02:22 UTC

New packages created between 2026-10-19 01:22 UTC and 2026-10-19 02:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T02-22-33-185946Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 01:52:56 | [pieceofcake2/security-headers](https://www.nuget.org/packages/pieceofcake2%2Fsecurity-headers) | v1.0.0 |  | CakePHP 2 plugin that adds the security headers to every response of an applica… |
| 2026-10-19 02:07:30 | [lesterkaufungen/suggestedtests](https://www.nuget.org/packages/lesterkaufungen%2Fsuggestedtests) | v0.1.0 | Lester K. | PHPUnit helpers for PHP 7.4+: performance and memory budgets backed by a native… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
