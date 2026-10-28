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

## Latest list — 2026-10-28 12:18 UTC

New packages created between 2026-10-28 11:19 UTC and 2026-10-28 12:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T12-18-43-515934Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 11:24:22 | [biometric-push/laravel-adms](https://www.nuget.org/packages/biometric-push%2Flaravel-adms) | 1.0.0 |  | ZKTeco ADMS / PUSH (iclock) server for Laravel 8-12+: devices connect to your a… |
| 2026-10-28 11:32:27 | [cabuz/laravel-tembo](https://www.nuget.org/packages/cabuz%2Flaravel-tembo) | v1.0.0 | Florin Cabuz | Laravel SDK for the Tembo API: start background coding agents, manage sessions,… |
| 2026-10-28 11:32:34 | [catatsumuri/http-download](https://www.nuget.org/packages/catatsumuri%2Fhttp-download) | v1.0.0 | Michael Wallner; Philippe Jau… | PEAR HTTP_Download, HTTP_Header and HTTP packaged for Composer, unchanged excep… |
| 2026-10-28 11:34:33 | [saraivaruas/mercado-publico](https://www.nuget.org/packages/saraivaruas%2Fmercado-publico) | v1.0.0 | Jorge Luis Saraiva Ruas | Cliente PHP de la API pública de Mercado Público (ChileCompra): licitaciones, ó… |
| 2026-10-28 11:34:52 | [selectika/module-ai-commerce](https://www.nuget.org/packages/selectika%2Fmodule-ai-commerce) | v0.1.0 |  | Selectika AI Commerce for Magento: catalog feeds, storefront experiences and an… |
| 2026-10-28 11:54:09 | [enicore/rivena](https://www.nuget.org/packages/enicore%2Frivena) | 1.0.0 | Enicore Solutions | A PHP framework for admin-focused websites. |
| 2026-10-28 11:59:58 | [webcito/bs-time-duration](https://www.nuget.org/packages/webcito%2Fbs-time-duration) | 1.0.0 | thomas | description |
| 2026-10-28 12:00:02 | [biometric-push/laravel-amt-push](https://www.nuget.org/packages/biometric-push%2Flaravel-amt-push) | v1.0.1 |  | AMT / M50 WebSocket SDK server for Laravel 8-12+: attendance terminals (AMT800,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
