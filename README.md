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

## Latest list — 2026-11-06 09:21 UTC

New packages created between 2026-11-06 08:21 UTC and 2026-11-06 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T09-21-58-71682Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 08:33:22 | [pixonaut/pixonaut-php](https://www.nuget.org/packages/pixonaut%2Fpixonaut-php) | v1.0.0 |  | PHP SDK for the Pixonaut public API. |
| 2026-11-06 08:48:52 | [rekhu/core](https://www.nuget.org/packages/rekhu%2Fcore) | v0.1.0 | Rekhu | Rekhu Core for Laravel: install Rekhu's knowers (Rekhu Machines first) into you… |
| 2026-11-06 08:51:35 | [mikepagedev/filament-portfolio](https://www.nuget.org/packages/mikepagedev%2Ffilament-portfolio) | v1.0.0 | Mike Page | Portfolio projects and case studies for Filament panels. |
| 2026-11-06 08:57:44 | [sightpress/plugin-articles](https://www.nuget.org/packages/sightpress%2Fplugin-articles) | v1.0.0 |  | The official SightPress plugin for articles, categories, tags, archives and fee… |
| 2026-11-06 08:57:48 | [sightpress/plugin-community-helper](https://www.nuget.org/packages/sightpress%2Fplugin-community-helper) | v1.0.0 |  | The official SightPress plugin for comments, likes, share links and saved pages. |
| 2026-11-06 08:58:04 | [sightpress/plugin-ai-helper](https://www.nuget.org/packages/sightpress%2Fplugin-ai-helper) | v1.0.0 |  | The official SightPress plugin for optional AI assistance. |
| 2026-11-06 08:58:08 | [sightpress/plugin-file-importer](https://www.nuget.org/packages/sightpress%2Fplugin-file-importer) | v1.0.0 |  | The official SightPress plugin for importing content. |
| 2026-11-06 09:06:52 | [crabphp/arc](https://www.nuget.org/packages/crabphp%2Farc) | v0.1.1 |  | Arc, the Crab template engine: components compiled once to plain PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
