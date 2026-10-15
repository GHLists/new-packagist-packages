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

## Latest list — 2026-10-15 13:22 UTC

New packages created between 2026-10-15 12:23 UTC and 2026-10-15 13:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T13-22-37-380244Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 12:30:50 | [kgaut/healthcheck](https://www.nuget.org/packages/kgaut%2Fhealthcheck) | 1.0.0-beta2 | Kevin Gautreau | Point de santé /health pour Drupal, extensible par plugins : base, Redis, Searc… |
| 2026-10-15 12:32:47 | [softsolutions4u/orocommerce-invoice](https://www.nuget.org/packages/softsolutions4u%2Forocommerce-invoice) | v1.0.0 | Pradeep Elayaraja; Ganesh; So… | Invoice management for OroCommerce Community Edition (CE) 7.0.3: create invoice… |
| 2026-10-15 12:42:07 | [fof/brevo-mail](https://www.nuget.org/packages/fof%2Fbrevo-mail) | 2.0.0 | FriendsOfFlarum | Send your forum mail through the Brevo API |
| 2026-10-15 12:43:28 | [everysize/checkout-jtl-shop5](https://www.nuget.org/packages/everysize%2Fcheckout-jtl-shop5) | v1.0.2 |  | everysize Checkout for JTL-Shop 5: imports everysize orders and reports shippin… |
| 2026-10-15 12:51:03 | [1994/wishlist-statamic](https://www.nuget.org/packages/1994%2Fwishlist-statamic) | v1.0.0 | 1994 | Wishlists for Statamic: let visitors save entries to named lists, kept in flat… |
| 2026-10-15 12:59:02 | [ramlev/dom-onix-parser](https://www.nuget.org/packages/ramlev%2Fdom-onix-parser) | 1.0.1 | Mateusz Domin; Chris Ribal; C… | An ONIX 3.0 Parser |
| 2026-10-15 13:13:02 | [karnoweb/laravel-livewire-kanban](https://www.nuget.org/packages/karnoweb%2Flaravel-livewire-kanban) | 13.0.0 |  | Domain-agnostic enterprise Kanban and List UI for Laravel Livewire |
| 2026-10-15 13:13:47 | [kobaltdigital/pingpong-agent](https://www.nuget.org/packages/kobaltdigital%2Fpingpong-agent) | v1.0.0 | Kobalt Digital | Reports a Laravel app's scheduler and health to PingPong |
| 2026-10-15 13:18:50 | [lizmap/streaming-json-encoder](https://www.nuget.org/packages/lizmap%2Fstreaming-json-encoder) | v2.0.0 | Riikka Kalliomäki; Laurent Jo… | Library for iteratively encoding large JSON documents piece by piece (maintaine… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
