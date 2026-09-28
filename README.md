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

## Latest list — 2026-09-28 21:22 UTC

New packages created between 2026-09-28 20:20 UTC and 2026-09-28 21:22 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T21-22-24-064025Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 20:22:34 | [n9c/typo3-monitor](https://www.nuget.org/packages/n9c%2Ftypo3-monitor) | 0.3.2 | N9C | N9C Inside Monitor - meldet sicherheitsrelevante Kennzahlen dieser TYPO3-Instan… |
| 2026-09-28 20:54:09 | [kaveraa/slug-history](https://www.nuget.org/packages/kaveraa%2Fslug-history) | v1.0.0 | Augustin Kavera | Garde les anciens slugs et redirige en 301 vers la nouvelle adresse, pour Larav… |
| 2026-09-28 21:08:41 | [pietervanleuven/vitodeploy-bunny](https://www.nuget.org/packages/pietervanleuven%2Fvitodeploy-bunny) | 0.2.0 | Pieter Van Leuven | Bunny.net integration for VitoDeploy: DNS provider, Edge Storage backups and CD… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
