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

## Latest list — 2026-11-19 05:19 UTC

New packages created between 2026-11-19 04:21 UTC and 2026-11-19 05:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T05-19-08-036274Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 04:32:07 | [nepdatejs/nepdate](https://www.nuget.org/packages/nepdatejs%2Fnepdate) | v0.1.1 | Shishir Rai | Bikram Sambat (BS) ⇄ AD dates for PHP: conversion, arithmetic, formatting, pars… |
| 2026-11-19 04:46:59 | [frandeone/ecf-sdk](https://www.nuget.org/packages/frandeone%2Fecf-sdk) | v0.1.1 | Frande Connection SRL | SDK PHP de Frande ECF: facturación electrónica (e-CF) DGII República Dominicana |
| 2026-11-19 04:56:45 | [hipdevteam/ion-mu](https://www.nuget.org/packages/hipdevteam%2Fion-mu) | v3.5.8 | ION | ION MU — WordPress mu-plugin that fire-and-forgets activity events to Site Inte… |
| 2026-11-19 04:57:22 | [b4n1/b4n1-secrets](https://www.nuget.org/packages/b4n1%2Fb4n1-secrets) | v0.1.2 | Bani Montoya | Sovereign offline vault — committable encrypted secrets |
| 2026-11-19 05:03:34 | [eii/arqon-forms](https://www.nuget.org/packages/eii%2Farqon-forms) | v1.0.0 |  | A dynamic form builder and submission manager for Laravel 13 and Filament 5. |
| 2026-11-19 05:08:08 | [js-upup/image-input-inspector](https://www.nuget.org/packages/js-upup%2Fimage-input-inspector) | v0.1.0 |  | Inspect local image dimensions and check configurable upload limits |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
