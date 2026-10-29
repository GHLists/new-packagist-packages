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

## Latest list — 2026-10-29 22:21 UTC

New packages created between 2026-10-29 21:21 UTC and 2026-10-29 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T22-21-08-69149Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 21:45:55 | [sentinelo/agent-composer](https://www.nuget.org/packages/sentinelo%2Fagent-composer) | v1.1.1 |  | Agent de maintenance Sentinelo pour les applications basées sur Composer — Symf… |
| 2026-10-29 21:51:34 | [jetro-tools/contao-bundle](https://www.nuget.org/packages/jetro-tools%2Fcontao-bundle) | v1.0.1 | INRI Management Consulting Gm… | Jetro: Termine aus Jetro in Contao-Kalender übernehmen |
| 2026-10-29 21:52:47 | [ernestdefoe/festoon](https://www.nuget.org/packages/ernestdefoe%2Ffestoon) | 1.0.1 | Ernest Defoe | A holiday theme that changes with the time of year: holiday colors, moving head… |
| 2026-10-29 22:04:29 | [skorlok/dedicated-server-api](https://www.nuget.org/packages/skorlok%2Fdedicated-server-api) | 1.0.0 | NadeoLive; Skorlok | XML-RPC library to connect to ManiaPlanet server |
| 2026-10-29 22:04:57 | [skorlok/asynchronous-jobs](https://www.nuget.org/packages/skorlok%2Fasynchronous-jobs) | 1.0.0 | Oliver de Cramer; Skorlok | Execute new php instances easily as you would threads. |
| 2026-10-29 22:05:10 | [skorlok/manialive-lib](https://www.nuget.org/packages/skorlok%2Fmanialive-lib) | 1.0.0 | NadeoLive; Skorlok | ManiaLive library |
| 2026-10-29 22:09:02 | [invoapi/invoapi-php](https://www.nuget.org/packages/invoapi%2Finvoapi-php) | v0.1.0 |  | PHP client for the invoapi.de e-invoicing API: create and validate XRechnung, Z… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
