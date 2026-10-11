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

## Latest list — 2026-10-11 15:21 UTC

New packages created between 2026-10-11 14:19 UTC and 2026-10-11 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T15-21-20-129565Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 14:57:02 | [tobiasnagel/flux-breadcrumbs](https://www.nuget.org/packages/tobiasnagel%2Fflux-breadcrumbs) | v1.0.0 |  | Route-driven breadcrumbs for Laravel applications rendered with Flux UI. |
| 2026-10-11 15:07:32 | [neos/contentgraph-doctrinedbaladapter-compatibility](https://www.nuget.org/packages/neos%2Fcontentgraph-doctrinedbaladapter-compatibility) | 9.2.0 |  | Forward compatibility layer to allow smooth upgrades to Neos version which prov… |
| 2026-10-11 15:07:32 | [neos/contentgraph-doctrinedbaladapter-forward-compatibility](https://www.nuget.org/packages/neos%2Fcontentgraph-doctrinedbaladapter-forward-compatibility) | 9.2.0 |  | Forward compatibility layer to allow smooth upgrades to Neos version which prov… |
| 2026-10-11 15:10:24 | [survos/otio-bundle](https://www.nuget.org/packages/survos%2Fotio-bundle) | 2.36.5 |  | Symfony integration scaffold for the Survos OpenTimelineIO library. |
| 2026-10-11 15:10:27 | [survos/otio](https://www.nuget.org/packages/survos%2Fotio) | 2.36.5 |  | Planned PHP OpenTimelineIO subset for editorial documents, timing and playback… |
| 2026-10-11 15:11:49 | [hoceineel/filament-sidebar-editor](https://www.nuget.org/packages/hoceineel%2Ffilament-sidebar-editor) | v0.1.0 | Hoceine El Idrissi | Let each tenant, user or panel hide, show and reorder Filament navigation group… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
