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

## Latest list — 2026-11-07 15:20 UTC

New packages created between 2026-11-07 14:19 UTC and 2026-11-07 15:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T15-20-30-916168Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 14:33:23 | [tualo/apachelog](https://www.nuget.org/packages/tualo%2Fapachelog) | 1.0.2 | Thomas Hoffmann | Apache Access/Error-Log Viewer for tualo office |
| 2026-11-07 14:42:43 | [tualo/tualolog](https://www.nuget.org/packages/tualo%2Ftualolog) | 1.0.1 | Thomas Hoffmann | Tualo Application-Log Viewer for tualo office |
| 2026-11-07 15:09:36 | [jeslage/statamic-emojis](https://www.nuget.org/packages/jeslage%2Fstatamic-emojis) | v1.0.0 | Johannes Eslage | Emoji picker for Statamic: Emoji and Emoji Text fieldtypes, a Bard button, shor… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
