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

## Latest list — 2026-10-05 23:20 UTC

New packages created between 2026-10-05 22:22 UTC and 2026-10-05 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T23-20-18-223292Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 22:33:34 | [bkubicki/rabbitmq-playground](https://www.nuget.org/packages/bkubicki%2Frabbitmq-playground) | 1.0 |  | Module testing rabbitmq implemention |
| 2026-10-05 22:38:49 | [skylive/lienzo](https://www.nuget.org/packages/skylive%2Flienzo) | v0.1.1 | Skylive LLC | Landing page builder for Laravel: a visual editor, a validated document format… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
