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

## Latest list — 2026-11-07 10:20 UTC

New packages created between 2026-11-07 09:21 UTC and 2026-11-07 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T10-20-29-72071Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 09:48:51 | [php-concept/brick-view-plates](https://www.nuget.org/packages/php-concept%2Fbrick-view-plates) | v1.1.2 |  | Concept stack brick: Plates view engine |
| 2026-11-07 09:48:51 | [php-concept/brick-view-twig](https://www.nuget.org/packages/php-concept%2Fbrick-view-twig) | v1.1.2 |  | Concept stack brick: Twig view engine |
| 2026-11-07 10:00:30 | [undpaul/guzzle-oauth2-plugin](https://www.nuget.org/packages/undpaul%2Fguzzle-oauth2-plugin) | 4.0.1 | Bojan Zivanovic; Damien Tourn… | An OAuth2 middleware for Guzzle based on commerceguys/guzzle-oauth2-plugin |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
