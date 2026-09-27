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

## Latest list — 2026-09-27 22:20 UTC

New packages created between 2026-09-27 21:19 UTC and 2026-09-27 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-27T22-20-40-757599Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-27 21:51:59 | [lex-zander/kirby-karbon](https://www.nuget.org/packages/lex-zander%2Fkirby-karbon) | 1.0.0 | Alexander Drießen | Serves a carbon.txt for Kirby sites, editable in the Panel |
| 2026-09-27 22:09:41 | [profmugomes/mgcep](https://www.nuget.org/packages/profmugomes%2Fmgcep) | 2.0.1 | Murilo Gomes | É uma biblioteca leve e simples em PHP para consulta de CEP utilizando a API pú… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
