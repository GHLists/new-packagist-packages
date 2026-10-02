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

## Latest list — 2026-10-02 09:18 UTC

New packages created between 2026-10-02 08:21 UTC and 2026-10-02 09:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T09-18-55-924912Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 08:26:30 | [marrow/ui](https://www.nuget.org/packages/marrow%2Fui) | v1.0.0 | Aure Dulvresse | A ready-to-use Tailwind + Alpine.js component library for Marrow — 30+ componen… |
| 2026-10-02 08:30:19 | [purplespider/silverstripe-elemental-draft-lock](https://www.nuget.org/packages/purplespider%2Fsilverstripe-elemental-draft-lock) | 1.0.0 | James Cocker | Lets editors lock an individual Elemental block as draft, so publishing the pag… |
| 2026-10-02 08:36:31 | [bee-interactive/boomerang](https://www.nuget.org/packages/bee-interactive%2Fboomerang) | v0.1.0 | Yves Engetschwiler | Boomerang notifier for the Laravel PHP framework. Monitor and report Laravel er… |
| 2026-10-02 08:51:36 | [magicoli/opensim-engine](https://www.nuget.org/packages/magicoli%2Fopensim-engine) | 3.0.0-beta.1 | Gudule Lapointe | OpenSimulator Engine - Framework-agnostic core functionality for OpenSim grids |
| 2026-10-02 09:06:00 | [codecorner/laravel-datagrid](https://www.nuget.org/packages/codecorner%2Flaravel-datagrid) | v1.0.0 |  | Extensible, queue-powered data grid for Laravel with a backend-defined schema,… |
| 2026-10-02 09:12:07 | [cjph96/php-core](https://www.nuget.org/packages/cjph96%2Fphp-core) | v0.1.0 | Cristian J. Pérez Hernández | A small, framework-independent PHP foundation for shared technical primitives. |
| 2026-10-02 09:14:59 | [goldnead/statamic-bard-footnotes](https://www.nuget.org/packages/goldnead%2Fstatamic-bard-footnotes) | v1.0.0 | Adrian Goldner | Footnotes for Bard: type [1] in the text, keep the sources in a grid, get super… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
