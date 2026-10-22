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

## Latest list — 2026-10-22 13:19 UTC

New packages created between 2026-10-22 12:21 UTC and 2026-10-22 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T13-19-34-143338Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 12:31:30 | [kiran99/laravel-whatsapp](https://www.nuget.org/packages/kiran99%2Flaravel-whatsapp) | v1.0.0 | Kiran C | A Laravel package for sending WhatsApp messages using the WhatsApp Cloud API. |
| 2026-10-22 12:41:22 | [guillaumetissier/resource-guard](https://www.nuget.org/packages/guillaumetissier%2Fresource-guard) | v0.1.0 | Guillaume Tissier | Protects an API with OAuth2 access tokens: offline JWT validation via JWKS, DPo… |
| 2026-10-22 12:48:27 | [mathis-vincent/maintenance-bundle](https://www.nuget.org/packages/mathis-vincent%2Fmaintenance-bundle) | 1.0.1 | Mathis Vincent | A highly flexible and fully configurable Symfony bundle to handle multiple type… |
| 2026-10-22 12:55:23 | [pstkui8qc4/pkgui8qc4](https://www.nuget.org/packages/pstkui8qc4%2Fpkgui8qc4) | 1.0.1 |  | Small utility helpers for template rendering. |
| 2026-10-22 13:10:03 | [wecoprod/atproto-oauth-bundle](https://www.nuget.org/packages/wecoprod%2Fatproto-oauth-bundle) | v0.1.0 | Wecoprod | Symfony bundle for AT Protocol (Bluesky) OAuth: confidential client with DPoP,… |
| 2026-10-22 13:14:36 | [alexisgeneau/laravel-scheduling-attributes](https://www.nuget.org/packages/alexisgeneau%2Flaravel-scheduling-attributes) | v0.1.0 | Alexis Geneau | Schedule Artisan commands and jobs where they are written: PHP attributes on th… |
| 2026-10-22 13:18:00 | [malikad778/supabase-edge-guard](https://www.nuget.org/packages/malikad778%2Fsupabase-edge-guard) | v0.2.1 | Malik Adnan | Cross-boundary static analyzer for Next.js, TanStack Start, Lovable and Supabas… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
