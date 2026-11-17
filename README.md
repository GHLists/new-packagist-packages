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

## Latest list — 2026-11-17 08:20 UTC

New packages created between 2026-11-17 07:18 UTC and 2026-11-17 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T08-20-46-534586Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 07:22:29 | [reachweb/statamic-resrv-vouchers](https://www.nuget.org/packages/reachweb%2Fstatamic-resrv-vouchers) | v1.0.0 | Iosif Chatzimichail | QR-code voucher generation, email delivery, and CP scanning for Statamic Resrv… |
| 2026-11-17 07:24:46 | [billionverify/billionverify-php](https://www.nuget.org/packages/billionverify%2Fbillionverify-php) | v1.1.0 | BillionVerify | Official BillionVerify PHP SDK for email verification |
| 2026-11-17 07:27:44 | [itmosoft/laravel-email-marketing](https://www.nuget.org/packages/itmosoft%2Flaravel-email-marketing) | v1.0.0 |  | Email audiences, consent-aware subscribers, reusable templates, campaign orches… |
| 2026-11-17 07:31:16 | [itmosoft/laravel-marketing-automation](https://www.nuget.org/packages/itmosoft%2Flaravel-marketing-automation) | v1.0.0 |  | Event-triggered marketing workflows, execution tracking, and pluggable action h… |
| 2026-11-17 07:34:34 | [itmosoft/laravel-campaign-tracking](https://www.nuget.org/packages/itmosoft%2Flaravel-campaign-tracking) | v1.0.1 |  | UTM attribution, campaign touchpoints, conversion recording, and attribution su… |
| 2026-11-17 07:43:18 | [itmosoft/laravel-referrals](https://www.nuget.org/packages/itmosoft%2Flaravel-referrals) | v1.0.0 |  | Referral codes, attribution, qualification, and reward integration for Laravel… |
| 2026-11-17 07:47:51 | [itmosoft/laravel-seo](https://www.nuget.org/packages/itmosoft%2Flaravel-seo) | v1.0.0 |  | SEO metadata, canonical URLs, social sharing tags, and JSON-LD structured data… |
| 2026-11-17 07:55:48 | [itmosoft/laravel-social-publishing](https://www.nuget.org/packages/itmosoft%2Flaravel-social-publishing) | v1.0.1 |  | Social account management, content scheduling, publication tracking, and platfo… |
| 2026-11-17 08:11:29 | [itmosoft/laravel-import-export](https://www.nuget.org/packages/itmosoft%2Flaravel-import-export) | v1.0.0 |  | Streaming CSV import and export utilities with header mapping, row validation,… |
| 2026-11-17 08:14:15 | [itmosoft/laravel-feature-flags](https://www.nuget.org/packages/itmosoft%2Flaravel-feature-flags) | v1.0.0 |  | Database-backed feature flags with deterministic percentage rollouts and subjec… |
| 2026-11-17 08:17:34 | [itmosoft/laravel-localization](https://www.nuget.org/packages/itmosoft%2Flaravel-localization) | v1.0.0 |  | Locale registry, persistent subject preferences, and request locale resolution… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
