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

## Latest list — 2026-11-14 16:18 UTC

New packages created between 2026-11-14 15:19 UTC and 2026-11-14 16:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T16-18-39-792586Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 15:22:11 | [itmosoft/laravel-loyalty](https://www.nuget.org/packages/itmosoft%2Flaravel-loyalty) | v1.0.0 |  | A configurable loyalty points and rewards ledger for Laravel applications, with… |
| 2026-11-14 15:26:55 | [itmosoft/laravel-gift-cards](https://www.nuget.org/packages/itmosoft%2Flaravel-gift-cards) | v1.0.0 |  | Gift card issuance, balance management, redemption, and transaction ledger for… |
| 2026-11-14 15:34:08 | [itmosoft/laravel-coupons](https://www.nuget.org/packages/itmosoft%2Flaravel-coupons) | v1.0.0 |  | Coupon creation, validation, discount calculation, usage limits, and redemption… |
| 2026-11-14 15:38:00 | [itmosoft/laravel-reports](https://www.nuget.org/packages/itmosoft%2Flaravel-reports) | v1.0.0 |  | Composable database-backed reporting and aggregation tools for Laravel applicat… |
| 2026-11-14 15:41:45 | [itmosoft/laravel-abandoned-carts](https://www.nuget.org/packages/itmosoft%2Flaravel-abandoned-carts) | v1.0.1 |  | Abandoned cart capture, expiry detection, recovery links, and conversion tracki… |
| 2026-11-14 15:44:20 | [psolutions/encrypt-bundle](https://www.nuget.org/packages/psolutions%2Fencrypt-bundle) | v5.1.0 | Francisco Izquierdo | Bundle provides a service for encrypting values via attribute. |
| 2026-11-14 15:46:12 | [delwarhossaindev/laravel-zatca](https://www.nuget.org/packages/delwarhossaindev%2Flaravel-zatca) | v1.0.0 | Delwar Hossain | ZATCA (Fatoora) e-invoicing Phase 1 & Phase 2 for Laravel: onboarding, UBL XML,… |
| 2026-11-14 15:47:57 | [itmosoft/laravel-wishlist-sharing](https://www.nuget.org/packages/itmosoft%2Flaravel-wishlist-sharing) | v1.0.0 |  | Secure, expiring share links and access tracking for Laravel wishlist models. |
| 2026-11-14 15:50:59 | [sneakyx/motis-php-client](https://www.nuget.org/packages/sneakyx%2Fmotis-php-client) | v0.1.0 | André Scholz | PHP client for the MOTIS API (e.g. Transitous): multimodal routing, geocoding,… |
| 2026-11-14 15:51:01 | [itmosoft/laravel-product-questions](https://www.nuget.org/packages/itmosoft%2Flaravel-product-questions) | v1.0.0 |  | Product questions and answers with moderation, customer attribution, and helpfu… |
| 2026-11-14 15:53:58 | [itmosoft/laravel-vendors](https://www.nuget.org/packages/itmosoft%2Flaravel-vendors) | v1.0.0 |  | Vendor profiles, ownership, onboarding status, and moderation for Laravel marke… |
| 2026-11-14 15:57:14 | [itmosoft/laravel-vendor-products](https://www.nuget.org/packages/itmosoft%2Flaravel-vendor-products) | v1.0.0 |  | Associate marketplace vendors with polymorphic product models and manage vendor… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
