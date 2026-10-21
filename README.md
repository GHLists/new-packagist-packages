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

## Latest list — 2026-10-21 17:20 UTC

New packages created between 2026-10-21 16:21 UTC and 2026-10-21 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T17-20-28-474017Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 16:38:09 | [ecuafact/sdk](https://www.nuget.org/packages/ecuafact%2Fsdk) | v1.0.0-beta3 | Ecuanexus | Cliente oficial en PHP del API publico de facturacion electronica Ecuafact (con… |
| 2026-10-21 16:54:38 | [ernestdefoe/longshot](https://www.nuget.org/packages/ernestdefoe%2Flongshot) | 1.0.0 | Ernest Defoe | Longshot — a virtual-points sportsbook for Flarum. Moneylines, spreads, totals… |
| 2026-10-21 16:55:33 | [cpuchalver/filament-starter-kit](https://www.nuget.org/packages/cpuchalver%2Ffilament-starter-kit) | v1.0.1 |  | The skeleton application for the Laravel framework. |
| 2026-10-21 16:56:26 | [j87nl/laravel-error-reporter](https://www.nuget.org/packages/j87nl%2Flaravel-error-reporter) | v0.1.0 | Johan Montenij | Reports Laravel and browser errors to the J87 error collector. |
| 2026-10-21 17:05:31 | [neuron-php/labor-board](https://www.nuget.org/packages/neuron-php%2Flabor-board) | 0.1.0 | Lee Jones | Job queue dashboard for Neuron MVC and CMS applications: pending, delayed, rese… |
| 2026-10-21 17:06:15 | [biru/payhub](https://www.nuget.org/packages/biru%2Fpayhub) | v1.0.0 | Biru Indonesia Creative | Official PHP SDK for Biru PayHub Centralized Multi-Platform Payment Gateway (Mi… |
| 2026-10-21 17:10:50 | [amjadiqbal/filament-change-requests](https://www.nuget.org/packages/amjadiqbal%2Ffilament-change-requests) | v1.0.0 | Amjad Iqbal | Hold record edits in Filament as change requests: field-by-field diff, approve,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
