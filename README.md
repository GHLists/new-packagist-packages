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

## Latest list — 2026-10-28 13:19 UTC

New packages created between 2026-10-28 12:18 UTC and 2026-10-28 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T13-19-05-296134Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 12:50:50 | [edemsky.m/laravel-media-collections](https://www.nuget.org/packages/edemsky.m%2Flaravel-media-collections) | v0.1.0 |  |  |
| 2026-10-28 13:02:22 | [dockcodes/dockaccess-alt-generator-symfony](https://www.nuget.org/packages/dockcodes%2Fdockaccess-alt-generator-symfony) | 1.0.0 | Dock | Symfony bundle for the dockaccess.org AI alt text generator: connection to the… |
| 2026-10-28 13:05:06 | [dockcodes/dockaccess-alt-generator-laravel](https://www.nuget.org/packages/dockcodes%2Fdockaccess-alt-generator-laravel) | 1.0.0 | Dock | Laravel integration of the dockaccess.org AI alt text generator: connection to… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
