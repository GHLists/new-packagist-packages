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

## Latest list — 2026-10-24 16:22 UTC

New packages created between 2026-10-24 15:19 UTC and 2026-10-24 16:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T16-22-10-301559Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 15:44:12 | [saola/admin](https://www.nuget.org/packages/saola%2Fadmin) | v0.1.0-alpha.1 |  | Reusable Saola admin shell, source publishing, database translations and schema… |
| 2026-10-24 15:59:01 | [drupal/varbase_ai_media_base](https://www.nuget.org/packages/drupal%2Fvarbase_ai_media_base) | 1.0.0-alpha1 | Vardot | Generate images and SVGs with AI from the Media Library on Varbase 11, with the… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
