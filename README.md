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

## Latest list — 2026-10-12 12:21 UTC

New packages created between 2026-10-12 11:18 UTC and 2026-10-12 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T12-21-30-171626Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 11:54:55 | [yourbureau/api-client](https://www.nuget.org/packages/yourbureau%2Fapi-client) | v1.0.1 | indual | PHP client for the yourBureau REST API v3 |
| 2026-10-12 11:56:25 | [ontob/moonwatch-laravel](https://www.nuget.org/packages/ontob%2Fmoonwatch-laravel) | v0.1.0 |  | Reports a Laravel application's errors to Moonwatch. |
| 2026-10-12 12:17:09 | [zeimoto/icons](https://www.nuget.org/packages/zeimoto%2Ficons) | v0.1.0 | zeimoto | Shared icons for the Kirby Panel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
