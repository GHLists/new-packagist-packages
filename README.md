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

## Latest list — 2026-11-03 20:21 UTC

New packages created between 2026-11-03 19:21 UTC and 2026-11-03 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T20-21-21-046343Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 20:03:02 | [webflixtec/sdk-php-nfsn](https://www.nuget.org/packages/webflixtec%2Fsdk-php-nfsn) | v1.0.0 | a21ns1g4ts; Weslley | SDK PHP das APIs para emissão de Nota Fiscal de Serviço Nacional |
| 2026-11-03 20:11:39 | [smart-dato/asendia-sync-sdk](https://www.nuget.org/packages/smart-dato%2Fasendia-sync-sdk) | 0.0.2 | SmartDato | Laravel SDK for the Asendia Sync shipping API (parcels, labels, manifests, trac… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
