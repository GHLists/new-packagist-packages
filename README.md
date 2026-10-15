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

## Latest list — 2026-10-15 01:19 UTC

New packages created between 2026-10-15 00:21 UTC and 2026-10-15 01:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T01-19-29-435109Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 00:21:26 | [pieceofcake2/async-aws](https://www.nuget.org/packages/pieceofcake2%2Fasync-aws) | v1.0.0 |  | AsyncAws integration for CakePHP 2: DynamoDB session handler and cache, Amazon… |
| 2026-10-15 00:34:11 | [ringlesoft/laravel-accounting](https://www.nuget.org/packages/ringlesoft%2Flaravel-accounting) | 0.1.0 | David Ringle | This is my package laravel-accounting |
| 2026-10-15 01:07:21 | [ernestdefoe/marquee](https://www.nuget.org/packages/ernestdefoe%2Fmarquee) | v1.0.0 | Ernest Defoe | Link discussions to movies, TV shows (down to the episode) and games, shown in… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
