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

## Latest list — 2026-10-22 18:20 UTC

New packages created between 2026-10-22 17:20 UTC and 2026-10-22 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T18-20-49-809459Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 17:24:53 | [vattra/laravel-rbac](https://www.nuget.org/packages/vattra%2Flaravel-rbac) | v1.0.0 | Ra Vattra | Fast, config-driven role-based access control for Laravel |
| 2026-10-22 17:29:39 | [jeffersongoncalves/laravel-zapsign](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-zapsign) | 1.0.0 | Jefferson Gonçalves | Laravel client for the ZapSign API (e-signature): documents, templates, signers… |
| 2026-10-22 17:40:15 | [jeffersongoncalves/filament-zapsign](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-zapsign) | 1.0.0 |  |  |
| 2026-10-22 17:40:19 | [market-media/input](https://www.nuget.org/packages/market-media%2Finput) | v1.0.0 |  | Leitura e sanitização de entradas HTTP para PHP 8.5. |
| 2026-10-22 17:54:38 | [preflow/codes](https://www.nuget.org/packages/preflow%2Fcodes) | v0.20.0 |  | Preflow codes — readable and random codes that grant something for one purpose |
| 2026-10-22 17:54:38 | [preflow/rbac](https://www.nuget.org/packages/preflow%2Frbac) | v0.20.0 |  | Preflow RBAC — roles managed in Folio answering can() |
| 2026-10-22 17:59:02 | [ecuafact/sdk](https://www.nuget.org/packages/ecuafact%2Fsdk) | v1.0.0-beta5 | Ecuanexus | Cliente oficial en PHP del API publico de facturacion electronica Ecuafact (con… |
| 2026-10-22 17:59:43 | [nicodevs/weather](https://www.nuget.org/packages/nicodevs%2Fweather) | v0.1.2 |  | Weather for any city, as JSON. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
