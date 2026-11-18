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

## Latest list — 2026-11-18 17:19 UTC

New packages created between 2026-11-18 16:19 UTC and 2026-11-18 17:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T17-19-43-709243Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 16:45:53 | [keyring/keyring](https://www.nuget.org/packages/keyring%2Fkeyring) | v0.1.0 |  | Factor-driven authentication for Laravel: many authenticators per user, devices… |
| 2026-11-18 16:48:58 | [okarabudka/laravel-base](https://www.nuget.org/packages/okarabudka%2Flaravel-base) | v1.0.0 |  | Laravel 12 project template with Docker (PHP-FPM, Nginx, Mailpit), Pest, Pint,… |
| 2026-11-18 16:49:21 | [erag/laravel-orphan-files](https://www.nuget.org/packages/erag%2Flaravel-orphan-files) | v0.0.1 | Er Amit Gupta | Find the uploaded files your Laravel app no longer uses, like old avatars and i… |
| 2026-11-18 16:49:54 | [particle-academy/fancy-service-token](https://www.nuget.org/packages/particle-academy%2Ffancy-service-token) | v0.1.0 | Particle Academy | Short-lived HMAC-SHA256 service tokens from a Laravel app to its sidecar: a sig… |
| 2026-11-18 16:50:15 | [hds-solutions/laravel-appsync-events](https://www.nuget.org/packages/hds-solutions%2Flaravel-appsync-events) | v0.1.0 | Hermann D. Schimpf | AWS AppSync Events broadcasting driver for Laravel, with a Laravel Echo connect… |
| 2026-11-18 17:03:47 | [mageenv/module-e-invoice-hyva](https://www.nuget.org/packages/mageenv%2Fmodule-e-invoice-hyva) | 1.0.0 |  | Hyva storefront templates for MageEnv XRechnung & ZUGFeRD E-Invoicing: e-invoic… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
