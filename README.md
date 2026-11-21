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

## Latest list — 2026-11-21 23:18 UTC

New packages created between 2026-11-21 22:20 UTC and 2026-11-21 23:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T23-18-54-760262Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 22:44:36 | [ticketbaiws/ticketbaiws-php](https://www.nuget.org/packages/ticketbaiws%2Fticketbaiws-php) | v1.0.0 | Berein Internet S.L. | Cliente PHP oficial de la API de Ticketbai WS: facturas TicketBAI (Araba, Bizka… |
| 2026-11-21 22:49:47 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.44.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-21 22:56:21 | [fake-email-pro/fake-email-php](https://www.nuget.org/packages/fake-email-pro%2Ffake-email-php) | v0.1.0 | fake-email.pro | Official PHP client for the fake-email.pro API: disposable mailboxes, one-time… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
