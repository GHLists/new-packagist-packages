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

## Latest list — 2026-11-24 01:21 UTC

New packages created between 2026-11-24 00:19 UTC and 2026-11-24 01:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T01-21-44-822943Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 00:40:04 | [noneo/sdk-pennylane](https://www.nuget.org/packages/noneo%2Fsdk-pennylane) | v1.0.0 | Valentin Goulier; Noneo | SDK pour l'accès à l'API Pennylane |
| 2026-11-24 01:07:24 | [mundosms/sdk](https://www.nuget.org/packages/mundosms%2Fsdk) | v1.0.0 | MundoSMS | Cliente de la API REST v3 de MundoSMS: SMS, WhatsApp, centralita, VozPush y Num… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
