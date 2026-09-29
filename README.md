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

## Latest list — 2026-09-29 22:21 UTC

New packages created between 2026-09-29 21:19 UTC and 2026-09-29 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T22-21-15-105737Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 21:24:34 | [markhamsq/nitpick](https://www.nuget.org/packages/markhamsq%2Fnitpick) | 0.1.0 | Nick Basile | A local QA panel for Laravel: scenarios, one-click persona login and reset, che… |
| 2026-09-29 21:25:26 | [youmad/endurance-activity-postgresql](https://www.nuget.org/packages/youmad%2Fendurance-activity-postgresql) | v0.1.0 |  | Doctrine DBAL adapters and migrations for PostgreSQL activity storage |
| 2026-09-29 21:28:48 | [mage2kishan/module-error-monitor](https://www.nuget.org/packages/mage2kishan%2Fmodule-error-monitor) | 1.5.10 | Kishan Savaliya | Panth Error Monitor - smart, secure error management for Magento 2. Captures PH… |
| 2026-09-29 21:35:38 | [mailhive/mailhive-php](https://www.nuget.org/packages/mailhive%2Fmailhive-php) | v0.1.0 |  | The official PHP SDK for Mailhive Send, with a Laravel mail transport. |
| 2026-09-29 21:36:38 | [dex/curio](https://www.nuget.org/packages/dex%2Fcurio) | 0.1.0 | Eder Soares | A curious way to query Eloquent |
| 2026-09-29 21:44:37 | [reconcilekit/core](https://www.nuget.org/packages/reconcilekit%2Fcore) | v0.1.0 |  | Financial reconciliation for Laravel: compare internal payments with provider d… |
| 2026-09-29 22:02:17 | [mage2kishan/module-extra-fee](https://www.nuget.org/packages/mage2kishan%2Fmodule-extra-fee) | 1.0.10 | Kishan Savaliya | Panth Extra Fee — add configurable extra fees and surcharges to Magento 2 check… |
| 2026-09-29 22:15:07 | [mage2kishan/module-faq](https://www.nuget.org/packages/mage2kishan%2Fmodule-faq) | 1.2.3 | Kishan Savaliya | Advanced FAQ Module with multi-level assignment capabilities |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
