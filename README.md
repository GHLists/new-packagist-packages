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

## Latest list — 2026-11-07 23:19 UTC

New packages created between 2026-11-07 22:20 UTC and 2026-11-07 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T23-19-21-983228Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 22:25:23 | [faghy/laracashbook](https://www.nuget.org/packages/faghy%2Flaracashbook) | v1.0.1 | Serafino Christian | A simple Laravel cash book: track income and expenses for several entities, wit… |
| 2026-11-07 22:29:56 | [nirgendheim/frontend-focusbox](https://www.nuget.org/packages/nirgendheim%2Ffrontend-focusbox) | 0.1.1 |  | Focusbox: Fotobooth- und Galerie-Layout fuer das fremeo Frontend. |
| 2026-11-07 22:36:55 | [ernestdefoe/lectern](https://www.nuget.org/packages/ernestdefoe%2Flectern) | 1.0.0 | Ernest Defoe | Lectern — read PDFs, Word documents and spreadsheets right inside the post: thu… |
| 2026-11-07 22:42:50 | [fvildoso/sii-dte-php](https://www.nuget.org/packages/fvildoso%2Fsii-dte-php) | v2026.11.07-4242190… | Felipe E. Vildoso Castillo | Librería PHP para integración con DTE (Documentos Tributarios Electrónicos) del… |
| 2026-11-07 23:03:32 | [jeslage/statamic-emojis](https://www.nuget.org/packages/jeslage%2Fstatamic-emojis) | v1.0.0 | Johannes Eslage | Emoji picker for Statamic: Emoji and Emoji Text fieldtypes, a Bard button, shor… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
