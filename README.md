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

## Latest list — 2026-10-23 14:19 UTC

New packages created between 2026-10-23 13:20 UTC and 2026-10-23 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T14-19-20-260716Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 13:25:24 | [switchback/laravel-impersonation](https://www.nuget.org/packages/switchback%2Flaravel-impersonation) | v1.0.0 |  | Session-based user impersonation with explicit authorization and customizable B… |
| 2026-10-23 13:33:23 | [maarheeze/compass-client-laravel](https://www.nuget.org/packages/maarheeze%2Fcompass-client-laravel) | 1.1.0 |  | exposes the status of a laravel site to compass |
| 2026-10-23 13:34:26 | [qdrant-labs/qdrant-laravel-scout](https://www.nuget.org/packages/qdrant-labs%2Fqdrant-laravel-scout) | v0.1.2 | Qdrant Team | A Qdrant driver for Laravel Scout with full-text, semantic, and hybrid search. |
| 2026-10-23 13:37:57 | [efabrica/phoenix-scylla](https://www.nuget.org/packages/efabrica%2Fphoenix-scylla) | 1.0.0 |  | Cassandra / ScyllaDB adapter for Phoenix database migrations |
| 2026-10-23 13:40:50 | [amjadiqbal/filament-audience-sync](https://www.nuget.org/packages/amjadiqbal%2Ffilament-audience-sync) | v1.0.0 | Amjad Iqbal | Email-marketing audience sync for Filament 4 and 5: subscribe, unsubscribe, tag… |
| 2026-10-23 13:44:43 | [rohama/koin-sizpay](https://www.nuget.org/packages/rohama%2Fkoin-sizpay) | 2.2.1 | Rohama | Koin — SizPay gateway driver (REST Simple API) |
| 2026-10-23 13:51:09 | [ez-php/event-store-snapshots](https://www.nuget.org/packages/ez-php%2Fevent-store-snapshots) | 2.5.10 | Andreas Uretschnig | Snapshot store for ez-php/event-store streams: PDO and in-memory stores, every-… |
| 2026-10-23 13:51:09 | [ez-php/json-schema-validator](https://www.nuget.org/packages/ez-php%2Fjson-schema-validator) | 2.5.10 | Andreas Uretschnig | Validates decoded JSON against the JSON Schema subset ez-php/json-schema genera… |
| 2026-10-23 13:51:18 | [ez-php/asyncapi](https://www.nuget.org/packages/ez-php%2Fasyncapi) | 2.5.10 | Andreas Uretschnig | AsyncAPI 3.0 document generation for broadcast channels, webhooks and WebSocket… |
| 2026-10-23 13:51:23 | [ez-php/qrcode](https://www.nuget.org/packages/ez-php%2Fqrcode) | 2.5.10 | Andreas Uretschnig | Dependency-free QR code encoder (numeric/alphanumeric/byte, versions 1-40, ECC… |
| 2026-10-23 13:56:26 | [silvershop-suite/decimal-quantity](https://www.nuget.org/packages/silvershop-suite%2Fdecimal-quantity) | 1.0.0 | Remy Vaartjes; SilverShop-Sui… | Per-product decimal / fractional order quantities for SilverShop (CMS 6) — sell… |
| 2026-10-23 14:06:18 | [rohama/koin-zarinpal](https://www.nuget.org/packages/rohama%2Fkoin-zarinpal) | 2.2.1 | Rohama | Koin — Zarinpal gateway driver (classic REST v4, merchant code) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
