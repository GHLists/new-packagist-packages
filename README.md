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

## Latest list — 2026-11-07 09:21 UTC

New packages created between 2026-11-07 08:21 UTC and 2026-11-07 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T09-21-23-016497Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 08:31:03 | [cboxdk/laravel-assistant-client](https://www.nuget.org/packages/cboxdk%2Flaravel-assistant-client) | v0.1.0 |  | Cbox Assistant client for Laravel: signed tools, product support and curated kn… |
| 2026-11-07 09:17:46 | [tribble/emoji](https://www.nuget.org/packages/tribble%2Femoji) | 1.0.1 | Alex Brindley | Fluent emoji for tribble |
| 2026-11-07 09:19:15 | [rapttor/yii2-postar](https://www.nuget.org/packages/rapttor%2Fyii2-postar) | v0.1.0 | Rapttor | Symfony Mailer transport for the Postar mail API (POST /v1/send) for yiisoft/yi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
