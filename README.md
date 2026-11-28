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

## Latest list — 2026-11-28 01:19 UTC

New packages created between 2026-11-28 00:20 UTC and 2026-11-28 01:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T01-19-57-281509Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 00:28:49 | [pierdolabs/codice-fiscale](https://www.nuget.org/packages/pierdolabs%2Fcodice-fiscale) | v1.0.1 | Pierdomenico Guarnieri | Generazione, validazione e decodifica del codice fiscale italiano, con archivio… |
| 2026-11-28 00:35:20 | [pierdolabs/codice-fiscale-names](https://www.nuget.org/packages/pierdolabs%2Fcodice-fiscale-names) | v1.0.1 | Pierdomenico Guarnieri | Dizionario di nomi e cognomi per paese e provincia italiana (Wikidata + statist… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
