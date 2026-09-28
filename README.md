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

## Latest list — 2026-09-28 12:20 UTC

New packages created between 2026-09-28 11:20 UTC and 2026-09-28 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T12-20-10-768532Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 11:20:36 | [fahadahmadshemul/laravel-qrcode](https://www.nuget.org/packages/fahadahmadshemul%2Flaravel-qrcode) | v1.0.0 | Md. Fahad Hossain | Self-contained QR code generator for Laravel with the QR encoding engine implem… |
| 2026-09-28 11:32:58 | [christianjbrown/api-client](https://www.nuget.org/packages/christianjbrown%2Fapi-client) | v1.0.0 | Christian Brown | A thin, strongly-typed PHP 8.5+ client for JSON and XML APIs that wraps GuzzleH… |
| 2026-09-28 11:33:53 | [christianjbrown/key-value-store](https://www.nuget.org/packages/christianjbrown%2Fkey-value-store) | v1.0.0 | Christian Brown | A thin, strongly-typed PHP 8.5+ library of interchangeable key-value store impl… |
| 2026-09-28 11:35:53 | [christianjbrown/oauth2-client](https://www.nuget.org/packages/christianjbrown%2Foauth2-client) | v1.0.0 | Christian Brown | A thin, strongly-typed PHP 8.5+ OAuth 2.0 client that manages access tokens (re… |
| 2026-09-28 11:37:27 | [securetrading/test_migration_an](https://www.nuget.org/packages/securetrading%2Ftest_migration_an) | 1.0.1 |  | Repo to test migration to gitlab |
| 2026-09-28 11:41:59 | [noirapi/framework](https://www.nuget.org/packages/noirapi%2Fframework) | v1.0.1 | deba12 | Small PHP 8.4 web framework: FastRoute routing, Latte views, noirapi/database m… |
| 2026-09-28 11:42:41 | [andreacolzani/laravel-pgarray](https://www.nuget.org/packages/andreacolzani%2Flaravel-pgarray) | 1.0.0 | Andrea Colzani | PostgreSQL arrays support for Laravel |
| 2026-09-28 11:50:35 | [pandabear/mlm](https://www.nuget.org/packages/pandabear%2Fmlm) | v0.1.0 | chocoalano | Configurable MLM engine plugin for Panda Panel. |
| 2026-09-28 12:08:03 | [christianjbrown/ebay-browse-api-sdk](https://www.nuget.org/packages/christianjbrown%2Febay-browse-api-sdk) | v1.0.0 | Christian Brown | A strongly-typed, read-only PHP 8.5+ client for the eBay Browse API that return… |
| 2026-09-28 12:14:55 | [ismailnakkar/laravel-localization](https://www.nuget.org/packages/ismailnakkar%2Flaravel-localization) | v0.1.0 | Ismail Nakkar | Localized routes and per-visitor language for Laravel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
