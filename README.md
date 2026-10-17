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

## Latest list — 2026-10-17 18:21 UTC

New packages created between 2026-10-17 17:21 UTC and 2026-10-17 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T18-21-51-071562Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 18:06:36 | [ehundu/andamio-minimo](https://www.nuget.org/packages/ehundu%2Fandamio-minimo) | v0.16.0 |  | Un sitio de presentación de cuatro páginas hecho con Ehundu, para empezar. |
| 2026-10-17 18:06:47 | [ehundu/andamio-blog](https://www.nuget.org/packages/ehundu%2Fandamio-blog) | v0.16.0 |  | Un blog hecho con Ehundu, con lista paginada, etiquetas, feed y entradas que sa… |
| 2026-10-17 18:20:08 | [solvebeam/github-actions-toolkit-php](https://www.nuget.org/packages/solvebeam%2Fgithub-actions-toolkit-php) | v1.0.0 | SolveBeam; Remco Tolsma | PHP toolkit for developing GitHub Actions. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
