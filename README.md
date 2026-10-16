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

## Latest list — 2026-10-16 22:18 UTC

New packages created between 2026-10-16 21:18 UTC and 2026-10-16 22:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T22-18-48-247677Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 21:32:34 | [eduardoribeirodev/filament-kanban](https://www.nuget.org/packages/eduardoribeirodev%2Ffilament-kanban) | v1.0.0 | Eduardo Ribeiro | Kanban boards for Filament with native filters, actions, infolists, drag and dr… |
| 2026-10-16 21:37:06 | [arodu/cakephp-admin-tools](https://www.nuget.org/packages/arodu%2Fcakephp-admin-tools) | v1.0.0 |  |  |
| 2026-10-16 21:43:00 | [sparkhire/ai-detection](https://www.nuget.org/packages/sparkhire%2Fai-detection) | 9.9.9 |  |  |
| 2026-10-16 21:52:30 | [openthc/cre-adapter](https://www.nuget.org/packages/openthc%2Fcre-adapter) | 420.26.288 |  | OpenTHC Cannabis Reporting Engine API Adapters |
| 2026-10-16 21:58:37 | [arodu/cakephp-modal-form](https://www.nuget.org/packages/arodu%2Fcakephp-modal-form) | v2.0.0 |  | ModalForm plugin for CakePHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
