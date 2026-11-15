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

## Latest list — 2026-11-15 13:21 UTC

New packages created between 2026-11-15 12:21 UTC and 2026-11-15 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T13-21-06-101538Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 12:24:00 | [laravelazier/laravelazier](https://www.nuget.org/packages/laravelazier%2Flaravelazier) | 2.2.0 | Laravelazier Contributors | Lightweight Laravel package for generating PDF and Excel files with minimal set… |
| 2026-11-15 12:24:56 | [psbits/qa](https://www.nuget.org/packages/psbits%2Fqa) | 0.1.0-alpha |  | Shared QA infrastructure for PSBits TYPO3 extensions: test matrix scripts, Dock… |
| 2026-11-15 12:52:55 | [korin/gedcom](https://www.nuget.org/packages/korin%2Fgedcom) | v0.1.0 |  | Lossless GEDCOM 5.5–7.0 reader, validator, converter and writer for PHP |
| 2026-11-15 12:53:37 | [andicot/log-viewer](https://www.nuget.org/packages/andicot%2Flog-viewer) | v13.0.0 | ARCANEDEV; Andicot | Log viewer for Laravel 13 with daily log browsing and filtering by severity. Fo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
