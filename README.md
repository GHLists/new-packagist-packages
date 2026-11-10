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

## Latest list — 2026-11-10 10:21 UTC

New packages created between 2026-11-10 09:20 UTC and 2026-11-10 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T10-21-59-754523Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 09:22:33 | [shortcutmediaro/yii2-recaptcha-widget](https://www.nuget.org/packages/shortcutmediaro%2Fyii2-recaptcha-widget) | 1.0.1 | Shortcutmediaro | Yii2 Google reCAPTCHA v2 and v3 widget - this is a fork from himiklab |
| 2026-11-10 09:42:19 | [youwilllikeit/silverstripe-elements](https://www.nuget.org/packages/youwilllikeit%2Fsilverstripe-elements) | 2.0.0 |  | Basic, layout-free content blocks for silverstripe/elemental 6 (Hero, TextMedia… |
| 2026-11-10 09:54:22 | [hschottm/contao-newsletter-export](https://www.nuget.org/packages/hschottm%2Fcontao-newsletter-export) | 1.0.0 | Helmut Schottmüller | Export active Contao newsletter subscribers as a plain-text BCC address list. |
| 2026-11-10 10:03:31 | [grinet/module-billing-address-at-shipping](https://www.nuget.org/packages/grinet%2Fmodule-billing-address-at-shipping) | 1.0.0 | Hidayet OK @ grinet | Billing address below shipping with optional restricted HTML descriptions |
| 2026-11-10 10:03:43 | [sanvalabs/bangla-converter](https://www.nuget.org/packages/sanvalabs%2Fbangla-converter) | v1.0.0 | Sanvalabs | Convert numbers and dates to Bangla in Laravel. |
| 2026-11-10 10:04:11 | [paymongo/module-magento2-paymongo](https://www.nuget.org/packages/paymongo%2Fmodule-magento2-paymongo) | 2.0.1 | DevTeam | PayMongo payment gateway integration for Magento 2 — supports cards, GCash, Gra… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
