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

## Latest list — 2026-10-26 12:23 UTC

New packages created between 2026-10-26 11:21 UTC and 2026-10-26 12:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T12-23-14-189021Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 11:24:51 | [agilepixel/alls-well-php](https://www.nuget.org/packages/agilepixel%2Falls-well-php) | v1.0.1 | Agile Pixel | Connects a PHP application to All's Well as a site: reports versions, packages… |
| 2026-10-26 11:34:39 | [pollora/harness](https://www.nuget.org/packages/pollora%2Fharness) | v0.1.0 | Amphibee | Quality, testing, security and performance harness shared by every Pollora repo… |
| 2026-10-26 11:55:44 | [lucacermenati/simple-csv-import](https://www.nuget.org/packages/lucacermenati%2Fsimple-csv-import) | v0.1.0 | Luca Cermenati | Validate a CSV upload in the request, import it in chunks on the queue, and rec… |
| 2026-10-26 12:08:14 | [dondodano/laravel-avatars](https://www.nuget.org/packages/dondodano%2Flaravel-avatars) | v1.0.0 |  | Self-hosted initials avatar generator (SVG/PNG) with a ui-avatars.com compatibl… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
