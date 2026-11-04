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

## Latest list — 2026-11-04 14:20 UTC

New packages created between 2026-11-04 13:21 UTC and 2026-11-04 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T14-20-47-533253Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 13:26:06 | [cre8-it/creatorsapi-php-sdk](https://www.nuget.org/packages/cre8-it%2Fcreatorsapi-php-sdk) | v2.0.0 | Amazon Creators | Amazon Creators API PHP SDK with Login with Amazon authentication (upstream 1.3… |
| 2026-11-04 13:30:31 | [kommandhub/shipbubble-sw](https://www.nuget.org/packages/kommandhub%2Fshipbubble-sw) | 1.0.0 | Kommandhub Limited | Live Shipbubble courier rates at checkout, shipment booking from the order, tra… |
| 2026-11-04 13:39:47 | [seadragon/laravel-log-alerts](https://www.nuget.org/packages/seadragon%2Flaravel-log-alerts) | v0.0.3 |  | Daily email summaries of recent Laravel application errors. |
| 2026-11-04 13:49:53 | [jason/filament-chat-assistant](https://www.nuget.org/packages/jason%2Ffilament-chat-assistant) | v1.0.0 | Jason.Chen | AI chat assistant dialog plugin for Filament panels |
| 2026-11-04 13:50:00 | [flouviahq/cord](https://www.nuget.org/packages/flouviahq%2Fcord) | v1.1.0 | Flouvia | SDK de PHP para la API de Cord: cotizaciones, facturas, webhooks verificados, t… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
