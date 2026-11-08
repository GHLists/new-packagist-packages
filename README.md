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

## Latest list — 2026-11-08 19:21 UTC

New packages created between 2026-11-08 18:20 UTC and 2026-11-08 19:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T19-21-05-48633Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 18:25:45 | [utafitilabs/imap-bundle](https://www.nuget.org/packages/utafitilabs%2Fimap-bundle) | v0.1.0 | Ezekiel Mjema | Read-only IMAP mailbox watching for Symfony: an IMAP IDLE client, an RFC 822/MI… |
| 2026-11-08 18:41:00 | [apartejs/laravel](https://www.nuget.org/packages/apartejs%2Flaravel) | v0.1.0 |  | aparté for Laravel: an AI chat for Blade, Livewire and Filament, wired to the L… |
| 2026-11-08 18:47:03 | [szabrob/laravel-billingo](https://www.nuget.org/packages/szabrob%2Flaravel-billingo) | v0.1.0 | Szabó Róbert | Laravel integration for the Billingo API - create, send and manage invoices, pa… |
| 2026-11-08 18:53:05 | [smronju/nativephp-geolocation](https://www.nuget.org/packages/smronju%2Fnativephp-geolocation) | 1.0.0 | Mohammad Shoriful Islam Ronju | Implements NativePHP Mobile's Geolocation::getCurrentPosition(), checkPermissio… |
| 2026-11-08 19:03:01 | [variant/magento-extension](https://www.nuget.org/packages/variant%2Fmagento-extension) | v1.0.1 | Variant | Variant for Magento Open Source / Adobe Commerce: loads Variant's storefront ru… |
| 2026-11-08 19:03:33 | [goodport/laravel-js-error-logger](https://www.nuget.org/packages/goodport%2Flaravel-js-error-logger) | v0.0.1 | goodport | Capture browser JavaScript errors and write them to a Laravel log channel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
