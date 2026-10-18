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

## Latest list — 2026-10-18 18:19 UTC

New packages created between 2026-10-18 17:19 UTC and 2026-10-18 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T18-19-52-667313Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 17:26:52 | [skrull/sylius-quick-edit-bar-plugin](https://www.nuget.org/packages/skrull%2Fsylius-quick-edit-bar-plugin) | 0.1.0 | Simon Krull | Adds a quick edit bar with links into the Sylius admin to the storefront for lo… |
| 2026-10-18 17:34:05 | [xmlvalid/xmlvalid-php](https://www.nuget.org/packages/xmlvalid%2Fxmlvalid-php) | v1.0.0 | xmlvalid | PHP client for the xmlvalid API: validate XML and e-invoices (Peppol, XRechnung… |
| 2026-10-18 17:34:13 | [xmlvalid/xmlvalid-laravel](https://www.nuget.org/packages/xmlvalid%2Fxmlvalid-laravel) | v1.0.0 | xmlvalid | Laravel integration for the xmlvalid API: a validation rule for XML and e-invoi… |
| 2026-10-18 17:34:22 | [xmlvalid/xmlvalid-symfony](https://www.nuget.org/packages/xmlvalid%2Fxmlvalid-symfony) | v1.0.0 | xmlvalid | Symfony bundle for the xmlvalid API: a validator constraint for XML and e-invoi… |
| 2026-10-18 17:34:33 | [1994/ingest-statamic](https://www.nuget.org/packages/1994%2Fingest-statamic) | v1.0.0 | 1994 | Keep Statamic in sync with external feeds: JSON, XML, RSS, CSV, APIs and Google… |
| 2026-10-18 17:46:13 | [digit7s/filament-seo](https://www.nuget.org/packages/digit7s%2Ffilament-seo) | v0.1.0 |  | Polymorphic SEO metadata rendering and Filament components for Laravel. |
| 2026-10-18 18:05:38 | [hasan-deeba/larasaas](https://www.nuget.org/packages/hasan-deeba%2Flarasaas) | v1.0.0 |  | Drop-in SaaS engine for Laravel + React: Stripe billing (Cashier), multi-tenant… |
| 2026-10-18 18:10:44 | [numberotp/numberotp](https://www.nuget.org/packages/numberotp%2Fnumberotp) | v0.1.0 | NumberOTP | Official NumberOTP API client — virtual phone numbers for SMS / OTP verification |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
