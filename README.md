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

## Latest list — 2026-10-28 19:19 UTC

New packages created between 2026-10-28 18:21 UTC and 2026-10-28 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T19-19-36-763826Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 18:35:31 | [pollora/wp-rocket](https://www.nuget.org/packages/pollora%2Fwp-rocket) | v0.1.0 | Olivier Gorzalka | WP Rocket for Pollora, the Laravel framework for WordPress: keeps WP Rocket fro… |
| 2026-10-28 18:47:44 | [webx-ui/module-cart](https://www.nuget.org/packages/webx-ui%2Fmodule-cart) | v0.89.0 | WebX UI | A guest cart for WebX UI sites: lines of anything a module sells through the Pu… |
| 2026-10-28 18:48:00 | [webx-ui/module-users](https://www.nuget.org/packages/webx-ui%2Fmodule-users) | v0.89.0 | WebX UI | Visitors of a WebX UI site: their own table and the site guard, sign-in and reg… |
| 2026-10-28 18:51:04 | [novasia-estate/listing-import-guard](https://www.nuget.org/packages/novasia-estate%2Flisting-import-guard) | v1.0.0 | NovAsia Estate | Strict PHP real estate CSV import mapping: explicit currencies, decimal price s… |
| 2026-10-28 18:51:08 | [alexhackney/laravel-zammad](https://www.nuget.org/packages/alexhackney%2Flaravel-zammad) | v1.0.0 | Alex Hackney | Zammad helpdesk API client for Laravel, built on Saloon |
| 2026-10-28 18:51:45 | [omarabdelwahhab30/zatca](https://www.nuget.org/packages/omarabdelwahhab30%2Fzatca) | v1.0.1 |  | ZATCA (FATOORA) e-invoicing integration package: compliance/production onboardi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
