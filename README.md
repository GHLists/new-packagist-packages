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

## Latest list — 2026-11-04 22:26 UTC

New packages created between 2026-11-04 21:22 UTC and 2026-11-04 22:26 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T22-26-38-282766Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 21:23:04 | [openroam/sdk](https://www.nuget.org/packages/openroam%2Fsdk) | v0.1.0-rc.2 | OpenRoam | Official OpenRoam Partner API client: eSIMs, airtime, utility payments, gift ca… |
| 2026-11-04 21:37:54 | [beziworld/laravel-ml](https://www.nuget.org/packages/beziworld%2Flaravel-ml) | v1.0.0 | Kamil Ćwiertnia | Laravel-first machine learning on Rubix ML: Eloquent datasets, model classes, v… |
| 2026-11-04 21:56:56 | [maxcode/module-faq](https://www.nuget.org/packages/maxcode%2Fmodule-faq) | 1.0.0 |  | FAQ unique et indépendante pour Magento 2 : groupes et questions par vue de mag… |
| 2026-11-04 22:23:27 | [maxcode/module-core](https://www.nuget.org/packages/maxcode%2Fmodule-core) | 1.0.0 |  | EN: Shared foundation of the Maxcode modules for Magento 2: a single admin tab,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
