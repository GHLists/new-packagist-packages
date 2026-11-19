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

## Latest list — 2026-11-19 15:20 UTC

New packages created between 2026-11-19 14:21 UTC and 2026-11-19 15:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T15-20-23-580676Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 14:21:22 | [semsen1/three-d-preview-field](https://www.nuget.org/packages/semsen1%2Fthree-d-preview-field) | v1.0.0 |  | Laravel Nova field: upload and preview 3D models (STL, OBJ, PLY, GLB/GLTF, 3MF,… |
| 2026-11-19 14:23:44 | [daika7ana/innoship-php-sdk](https://www.nuget.org/packages/daika7ana%2Finnoship-php-sdk) | v1.0.0 | Dan-Radu Pana | Typed PHP SDK for the Innoship shipping API. |
| 2026-11-19 14:37:57 | [webservco/encryption](https://www.nuget.org/packages/webservco%2Fencryption) | v0.0.1 | Radu Maier | A PHP component/library. Encrypts secrets for storage with a key from the confi… |
| 2026-11-19 14:46:51 | [kraenkvisuell/statamic-bunny-cache](https://www.nuget.org/packages/kraenkvisuell%2Fstatamic-bunny-cache) | v0.1.2 | Sebastian Hilger | Full static caching for Statamic on the bunny.net CDN: pages are cached at the… |
| 2026-11-19 14:50:57 | [blackbird/billmap-hyva-compatibility](https://www.nuget.org/packages/blackbird%2Fbillmap-hyva-compatibility) | 1.0.0 |  | Blackbird BillMap Payment Gateway Compatibility with Hÿva Checkout check https:… |
| 2026-11-19 15:04:06 | [dorsetdigital/silverstripe-reapit](https://www.nuget.org/packages/dorsetdigital%2Fsilverstripe-reapit) | v1.0.0 |  | Reapit Foundations property import for Silverstripe CMS |
| 2026-11-19 15:05:58 | [hval/scalapay-php](https://www.nuget.org/packages/hval%2Fscalapay-php) | 1.0.0 | Hermann Vallieri | Unofficial PHP library for the Scalapay Buy Now Pay Later payment gateway: orde… |
| 2026-11-19 15:09:42 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.35.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-19 15:10:57 | [iguazoft/yii2-tenancy](https://www.nuget.org/packages/iguazoft%2Fyii2-tenancy) | v1.0.0 | Danny Rios Tolosa | Row-level multi-tenancy for Yii2 ActiveRecord that fails closed: scoped queries… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
