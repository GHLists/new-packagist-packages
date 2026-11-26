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

## Latest list — 2026-11-26 21:20 UTC

New packages created between 2026-11-26 20:21 UTC and 2026-11-26 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T21-20-54-983358Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 20:34:50 | [addresszen/laravel](https://www.nuget.org/packages/addresszen%2Flaravel) | v0.1.0 | AddressZen | Laravel package for the AddressZen PHP SDK: set your API key in .env, then inje… |
| 2026-11-26 20:34:50 | [addresszen/sdk](https://www.nuget.org/packages/addresszen%2Fsdk) | v0.1.0 | AddressZen | PHP client for the AddressZen API: US address verification, address autocomplet… |
| 2026-11-26 20:39:51 | [jayik/laravel](https://www.nuget.org/packages/jayik%2Flaravel) | v1.0.0 |  | Laravel client for the Jayik Merchant API v2: orders, warehouses, categories, r… |
| 2026-11-26 20:48:53 | [ismailnakkar/laravel-code-sample](https://www.nuget.org/packages/ismailnakkar%2Flaravel-code-sample) | v0.1.0 | Ismail Nakkar | Highlight a code sample written in a Blade slot, server-side with tempest/highl… |
| 2026-11-26 20:54:59 | [ditscheri/laravel-toolkit](https://www.nuget.org/packages/ditscheri%2Flaravel-toolkit) | v0.0.1 | Daniel Albertsen | Opinionated defaults and tools for Laravel. |
| 2026-11-26 21:14:10 | [kgaut/github_api](https://www.nuget.org/packages/kgaut%2Fgithub_api) | 1.0.0 | Kevin Gautreau | Integrates your Drupal site with GitHub through the KnpLabs GitHub API client. |
| 2026-11-26 21:17:31 | [addresszen/symfony-bundle](https://www.nuget.org/packages/addresszen%2Fsymfony-bundle) | v0.1.0 | AddressZen | Symfony bundle for the AddressZen PHP SDK: configure your API key once, inject… |
| 2026-11-26 21:19:30 | [dynamikasolucoesweb/laravel-menu](https://www.nuget.org/packages/dynamikasolucoesweb%2Flaravel-menu) | v1.0.0 | Giordani da Silveira dos Sant… | Menus para Laravel: desktop adaptativo (mega menu) e mobile responsivo, com cac… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
