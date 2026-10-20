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

## Latest list — 2026-10-20 03:19 UTC

New packages created between 2026-10-20 02:21 UTC and 2026-10-20 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T03-19-46-85585Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 02:26:03 | [isaech-solutions/sdk](https://www.nuget.org/packages/isaech-solutions%2Fsdk) | v0.0.3 | Isaac Machakata | An SDK for accessing our services via our dedicated api |
| 2026-10-20 02:48:26 | [porro/laravel-connector](https://www.nuget.org/packages/porro%2Flaravel-connector) | v0.1.1 |  | Read-only Porro connector for Laravel: versions, advisories, scheduler, queues,… |
| 2026-10-20 02:48:44 | [stoneholl/module-related-customer-orders](https://www.nuget.org/packages/stoneholl%2Fmodule-related-customer-orders) | v1.0.0 |  | Bounded same-store customer order history for Magento Admin, with optional stri… |
| 2026-10-20 02:50:15 | [porro/filament-connector](https://www.nuget.org/packages/porro%2Ffilament-connector) | v0.1.1 |  | Porro connector for Filament 3–5: Filament, Livewire and plugin versions plus p… |
| 2026-10-20 02:51:19 | [porro/statamic-connector](https://www.nuget.org/packages/porro%2Fstatamic-connector) | v0.1.1 |  | Porro connector for Statamic: Statamic and addon versions plus settings, on top… |
| 2026-10-20 03:08:43 | [tsumiki-labs/extension-builder](https://www.nuget.org/packages/tsumiki-labs%2Fextension-builder) | 1.0.0 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
