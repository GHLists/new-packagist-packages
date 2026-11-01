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

## Latest list — 2026-11-01 21:18 UTC

New packages created between 2026-11-01 20:19 UTC and 2026-11-01 21:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T21-18-53-987448Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 20:45:12 | [proclame/clubplanner-be-php-sdk](https://www.nuget.org/packages/proclame%2Fclubplanner-be-php-sdk) | v1.0.0 |  | PHP SDK for the Club Planner Partner API. |
| 2026-11-01 20:50:23 | [korzen/bot-protection](https://www.nuget.org/packages/korzen%2Fbot-protection) | 1.0.0 | Korzen | Korzen Bot Protection for PHP: asks POST /v1/decide before a protected action a… |
| 2026-11-01 20:54:03 | [gyro/attribute-collector](https://www.nuget.org/packages/gyro%2Fattribute-collector) | v0.9 | Benjamin Eberlei | Collects PHP attribute targets from the root package and from its Composer depe… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
