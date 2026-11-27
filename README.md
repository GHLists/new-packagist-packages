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

## Latest list — 2026-11-27 19:19 UTC

New packages created between 2026-11-27 18:21 UTC and 2026-11-27 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T19-19-48-315994Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 18:21:57 | [assetfeed/filament-ai-detector](https://www.nuget.org/packages/assetfeed%2Ffilament-ai-detector) | v0.1.0 |  | A Filament infolist entry that checks a text attribute for AI-written passages… |
| 2026-11-27 18:43:33 | [serkannyildirim/lidio-php-sdk](https://www.nuget.org/packages/serkannyildirim%2Flidio-php-sdk) | v0.1.0 | Serkan Yıldırım | Unofficial PHP SDK for the Lidio payment API (hosted payment page, payment stat… |
| 2026-11-27 18:47:08 | [innoboxrr/zoom-sdk](https://www.nuget.org/packages/innoboxrr%2Fzoom-sdk) | 1.0.0 | Homero Raul | Crea, consulta, actualiza y elimina reuniones de Zoom desde Laravel con la API… |
| 2026-11-27 18:51:24 | [delivrie/delivrie-php](https://www.nuget.org/packages/delivrie%2Fdelivrie-php) | v0.1.0 | Surce Inc | The PHP SDK for Delivrie: send email, manage domains, keys, webhooks, contacts… |
| 2026-11-27 18:55:53 | [eduardogp321/filament-mia-theme-v2](https://www.nuget.org/packages/eduardogp321%2Ffilament-mia-theme-v2) | 1.0.0 | Eduardo Palacios | A warm, editorial theme and design system for Filament PHP with live customizer. |
| 2026-11-27 19:06:34 | [writealt/statamic-writealt](https://www.nuget.org/packages/writealt%2Fstatamic-writealt) | v0.1.0 |  | Native bulk image alt text and same-format compression for Statamic 6. |
| 2026-11-27 19:10:25 | [kariricode/async-primitives](https://www.nuget.org/packages/kariricode%2Fasync-primitives) | v4.1.0 | Walmir Silva | Async building blocks for PHP 8.4 below the event loop: retries with backoff, r… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
