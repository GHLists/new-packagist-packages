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

## Latest list — 2026-10-24 14:19 UTC

New packages created between 2026-10-24 13:19 UTC and 2026-10-24 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T14-19-26-20152Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 13:42:34 | [orangecat/module-mago-ai-image](https://www.nuget.org/packages/orangecat%2Fmodule-mago-ai-image) | 1.0.0 |  | Mago Assistant add-on: AI product images from a gallery image and a prompt, wit… |
| 2026-10-24 14:10:11 | [korioinc/laravel-schema-align](https://www.nuget.org/packages/korioinc%2Flaravel-schema-align) | 1.0.1 | korinc | Laravel Schema Align |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
