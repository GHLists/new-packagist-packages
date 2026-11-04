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

## Latest list — 2026-11-04 17:20 UTC

New packages created between 2026-11-04 16:21 UTC and 2026-11-04 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T17-20-02-857903Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 16:22:51 | [beziworld/laravel-serwersms](https://www.nuget.org/packages/beziworld%2Flaravel-serwersms) | v1.0.0 | Kamil Ćwiertnia | Laravel integration for SerwerSMS.pl: SMS, MMS and voice sending, notification… |
| 2026-11-04 16:23:04 | [beziworld/laravel-smsplanet](https://www.nuget.org/packages/beziworld%2Flaravel-smsplanet) | v1.0.0 | Kamil Ćwiertnia | Laravel integration for SMSPlanet.pl: SMS and MMS sending, notification channel… |
| 2026-11-04 16:23:17 | [beziworld/laravel-allegro](https://www.nuget.org/packages/beziworld%2Flaravel-allegro) | v1.0.0 | Kamil Ćwiertnia | Allegro REST API client for Laravel: OAuth2 (code with PKCE, device flow, clien… |
| 2026-11-04 16:36:20 | [sursolver/sursolver](https://www.nuget.org/packages/sursolver%2Fsursolver) | v0.1.0 | SurSolver | Official PHP client for the SurSolver captcha solver API. Solve reCAPTCHA v3, C… |
| 2026-11-04 16:48:17 | [beziworld/laravel-previo](https://www.nuget.org/packages/beziworld%2Flaravel-previo) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the whole Previo hotel PMS API (XML, REST, POS, EQC): hotels… |
| 2026-11-04 16:49:57 | [beziworld/laravel-krs](https://www.nuget.org/packages/beziworld%2Flaravel-krs) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the Polish National Court Register (KRS) open API: company e… |
| 2026-11-04 16:51:43 | [beziworld/laravel-cpanel](https://www.nuget.org/packages/beziworld%2Flaravel-cpanel) | v1.0.0 | Kamil Ćwiertnia | Laravel client for cPanel UAPI and WHM API 1: accounts, packages, domains, DNS,… |
| 2026-11-04 16:51:59 | [beziworld/laravel-plesk](https://www.nuget.org/packages/beziworld%2Flaravel-plesk) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the Plesk REST API and XML API: customers, domains, DNS, dat… |
| 2026-11-04 16:52:16 | [beziworld/laravel-cloudflare](https://www.nuget.org/packages/beziworld%2Flaravel-cloudflare) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the Cloudflare API v4: zones, DNS records, cache purge, SSL/… |
| 2026-11-04 17:01:31 | [unicom360/unicom360-php](https://www.nuget.org/packages/unicom360%2Funicom360-php) | v0.1.0 | Techrode Solutions Limited | Official PHP SDK for the Unicom360 SMS, email and WhatsApp messaging API |
| 2026-11-04 17:18:14 | [beziworld/laravel-ceidg](https://www.nuget.org/packages/beziworld%2Flaravel-ceidg) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the official CEIDG API v3: look up Polish sole proprietorshi… |
| 2026-11-04 17:18:30 | [beziworld/laravel-gls](https://www.nuget.org/packages/beziworld%2Flaravel-gls) | v1.0.0 | Kamil Ćwiertnia | GLS Poland (ADE-Plus WebAPI) client for Laravel: consignments, labels, pickup c… |
| 2026-11-04 17:19:48 | [fractionroyalty/fraction-royalty-calc](https://www.nuget.org/packages/fractionroyalty%2Ffraction-royalty-calc) | 1.0.0 | Fraction Royalty | Tiny helpers for oil and gas fraction royalty calculations |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
