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

## Latest list — 2026-10-06 13:22 UTC

New packages created between 2026-10-06 12:20 UTC and 2026-10-06 13:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T13-22-15-636434Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 12:34:14 | [rafalmasiarek/mailer](https://www.nuget.org/packages/rafalmasiarek%2Fmailer) | v0.1.0 |  | From-scratch SMTP client + MIME builder (no PHPMailer dependency) with native P… |
| 2026-10-06 12:35:42 | [mage2kishan/module-price-drop-alert](https://www.nuget.org/packages/mage2kishan%2Fmodule-price-drop-alert) | 1.1.6 |  | Price Drop Alert module for Magento 2 - Allows customers to subscribe to price… |
| 2026-10-06 12:40:02 | [djessy/nl-tools](https://www.nuget.org/packages/djessy%2Fnl-tools) | v1.0.0 | Djessy van Drunen | A PHP Composer package with useful utilities for Dutch developers. |
| 2026-10-06 12:40:10 | [skynettechnologies/typo3-cookiesregtech](https://www.nuget.org/packages/skynettechnologies%2Ftypo3-cookiesregtech) | 1.0.0 | SKYNET TECHNOLOGIES USA LLC | CookiesRegTech cookie consent: guided connect, consent banner with automatic tr… |
| 2026-10-06 12:40:28 | [upmind/provision-provider-ssl](https://www.nuget.org/packages/upmind%2Fprovision-provider-ssl) | v1.0.0 | Harry Lewis | This provision category contains the common functions used in provisioning flow… |
| 2026-10-06 12:41:42 | [mage2kishan/module-low-stock-notification](https://www.nuget.org/packages/mage2kishan%2Fmodule-low-stock-notification) | 1.1.8 |  | Magento 2 Low Stock Notification module - allows customers to subscribe for bac… |
| 2026-10-06 12:46:59 | [mage2kishan/module-faq](https://www.nuget.org/packages/mage2kishan%2Fmodule-faq) | 1.3.10 | Kishan Savaliya | Advanced FAQ Module with multi-level assignment capabilities |
| 2026-10-06 12:56:00 | [mage2kishan/module-smart-badge](https://www.nuget.org/packages/mage2kishan%2Fmodule-smart-badge) | 1.1.9 |  | Smart Product Badge & Label System - Automatically displays beautiful badges on… |
| 2026-10-06 12:58:35 | [boss/laravel-district-access](https://www.nuget.org/packages/boss%2Flaravel-district-access) | v1.0.0 | Boss | Configurable district-based query scoping and access control for Laravel applic… |
| 2026-10-06 13:08:24 | [vortech/laravel-unit-conversions](https://www.nuget.org/packages/vortech%2Flaravel-unit-conversions) | v1.0.0 | Mate Papp | Fluent, immutable unit conversions for Laravel. |
| 2026-10-06 13:11:50 | [majistar/module-product-labels](https://www.nuget.org/packages/majistar%2Fmodule-product-labels) | 1.0.0 | Majistar | Text and image product labels for Magento 2 and Mage-OS with a Hyvä storefront:… |
| 2026-10-06 13:18:15 | [mage2kishan/module-whatsapp](https://www.nuget.org/packages/mage2kishan%2Fmodule-whatsapp) | 1.0.19 | Kishan Savaliya | WhatsApp Integration for Magento 2 — floating chat button, product page inquiry… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
