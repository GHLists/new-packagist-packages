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

## Latest list — 2026-11-13 04:19 UTC

New packages created between 2026-11-13 03:22 UTC and 2026-11-13 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T04-19-07-69768Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 03:25:30 | [preflow/publishing](https://www.nuget.org/packages/preflow%2Fpublishing) | v0.71.1 |  | Preflow publishing — drafts and published snapshots of records, revisions, sche… |
| 2026-11-13 03:29:22 | [canhao43/protheus-rest](https://www.nuget.org/packages/canhao43%2Fprotheus-rest) | v0.1.0 | Caio Marques | Cliente PHP para a API REST do TOTVS Protheus: login OAuth2 com renovação de to… |
| 2026-11-13 03:58:16 | [dayal/light-php](https://www.nuget.org/packages/dayal%2Flight-php) | v1.0.1 | Dayal Chandra Roy | A tiny Core PHP framework with routing, controllers, views and helpers. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
