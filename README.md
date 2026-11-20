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

## Latest list — 2026-11-20 18:21 UTC

New packages created between 2026-11-20 17:21 UTC and 2026-11-20 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T18-21-17-670939Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 17:31:42 | [reachbell/reachbell](https://www.nuget.org/packages/reachbell%2Freachbell) | v1.0.0 | DotSpheres Technologies Pvt L… | ReachBell server SDK for PHP: transactional push, email, SMS and WhatsApp, even… |
| 2026-11-20 17:40:38 | [veasin/ff-windows](https://www.nuget.org/packages/veasin%2Fff-windows) | 0.0.1 | V | Windows platform capability layer for ff: net, process, fs, folder, shortcut, c… |
| 2026-11-20 17:56:15 | [el-choco/editorial](https://www.nuget.org/packages/el-choco%2Feditorial) | 0.1.0-alpha.2 | el-choco | Collaborative drafts, revision history and review before publishing a Flarum di… |
| 2026-11-20 17:56:57 | [narek/sharp-php](https://www.nuget.org/packages/narek%2Fsharp-php) | v0.6.0 | Narek | SharpPHP: a C#-like language that compiles to modern PHP. |
| 2026-11-20 18:06:03 | [manadah/data-viewer](https://www.nuget.org/packages/manadah%2Fdata-viewer) | v0.1.0 |  | Contrato Laravel (TableQuery) para o DataViewer: colunas, filtros, ordenação, b… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
