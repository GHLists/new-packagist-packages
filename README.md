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

## Latest list — 2026-10-30 20:22 UTC

New packages created between 2026-10-30 19:20 UTC and 2026-10-30 20:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T20-22-11-011549Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 19:22:08 | [louigio04/buscador-cursos](https://www.nuget.org/packages/louigio04%2Fbuscador-cursos) | v1.1.0 | louigio04 | Projeto que busca os cursos no site da Alura |
| 2026-10-30 19:32:22 | [ernestdefoe/vantage](https://www.nuget.org/packages/ernestdefoe%2Fvantage) | 0.1.1 | Ernest Defoe | Vantage — account analytics for every member: impressions, engagement, profile… |
| 2026-10-30 19:41:14 | [stejac/zeitangaben](https://www.nuget.org/packages/stejac%2Fzeitangaben) | v0.1.0 | Stefan Jacomeit | Resolves colloquial German time expressions such as Herbstferien, ueber Ostern… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
