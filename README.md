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

## Latest list — 2026-10-25 01:21 UTC

New packages created between 2026-10-25 00:21 UTC and 2026-10-25 01:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T01-21-52-441495Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 00:43:59 | [atannex/scopable](https://www.nuget.org/packages/atannex%2Fscopable) | v1.0.0 | Atanga Leke Collins | Declarative state and date scopes for Laravel Eloquent: published / scheduled /… |
| 2026-10-25 00:44:01 | [atannex/ecosystem](https://www.nuget.org/packages/atannex%2Fecosystem) | v1.0.0 | Atanga Leke Collins | Deep, ranked search for Laravel Eloquent: any relation depth, JSON paths, searc… |
| 2026-10-25 00:44:02 | [atannex/generator](https://www.nuget.org/packages/atannex%2Fgenerator) | v1.0.0 | Atanga Leke Collins | Unique, human-readable codes for Laravel: reference numbers, invoice sequences,… |
| 2026-10-25 00:44:04 | [atannex/matrix](https://www.nuget.org/packages/atannex%2Fmatrix) | v1.0.0 | Atanga Leke Collins | The engagement matrix for Laravel: views, reading time, clicks, reactions, rati… |
| 2026-10-25 00:44:05 | [atannex/retrive](https://www.nuget.org/packages/atannex%2Fretrive) | v1.0.0 | Atanga Leke Collins | Data retrieval layer for Laravel Eloquent models: resource definitions, a fluen… |
| 2026-10-25 00:44:07 | [atannex/workflow](https://www.nuget.org/packages/atannex%2Fworkflow) | v1.0.0 | Atanga Leke Collins | Workflow engine for Laravel Eloquent models: states and transitions, guards, mu… |
| 2026-10-25 01:04:21 | [mapricot/mapricot](https://www.nuget.org/packages/mapricot%2Fmapricot) | v0.2.0 |  | Official client for the Mapricot API: geocoding, places, routing, and IP geoloc… |
| 2026-10-25 01:07:14 | [cursor-style/emoji](https://www.nuget.org/packages/cursor-style%2Femoji) | v1.0.0 | Cursor Style | Original Cursor Style 3D emoji catalog with exact Unicode skin-tone variants an… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
