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

## Latest list — 2026-09-30 19:21 UTC

New packages created between 2026-09-30 18:20 UTC and 2026-09-30 19:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T19-21-55-708937Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 18:25:02 | [hypnokizer/validator](https://www.nuget.org/packages/hypnokizer%2Fvalidator) | v7.0.0 | Nathan Kizer | Class to validate a dataset. |
| 2026-09-30 18:31:30 | [centralog/error-monitoring-laravel](https://www.nuget.org/packages/centralog%2Ferror-monitoring-laravel) | v0.1.0 |  | Laravel SDK for Centralog error monitoring. Captures exceptions and sends a cop… |
| 2026-09-30 18:40:23 | [sociolink/api-resource-bundle](https://www.nuget.org/packages/sociolink%2Fapi-resource-bundle) | v1.0.0 | Xavier KONGOLO | Génère les ressources API Platform (DTOs, State Processors/Providers, filtres Q… |
| 2026-09-30 18:47:52 | [hypnokizer/comptest](https://www.nuget.org/packages/hypnokizer%2Fcomptest) | v1.0.0 | Nathan Kizer | testing the versioning |
| 2026-09-30 18:55:27 | [sytxlabs/blade-sandbox](https://www.nuget.org/packages/sytxlabs%2Fblade-sandbox) | 1.0.0 | Shaun Lüdeke | A default-deny security sandbox for rendering untrusted Laravel Blade templates… |
| 2026-09-30 19:14:03 | [siberfx/mpesa-payment](https://www.nuget.org/packages/siberfx%2Fmpesa-payment) | 1.0.0 | Selim Görmüş | Modern M-Pesa payment gateway for PHP 8.4+ — Safaricom Daraja (Kenya) and Vodac… |
| 2026-09-30 19:15:46 | [fawno/agencias](https://www.nuget.org/packages/fawno%2Fagencias) | 0.0.1 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
