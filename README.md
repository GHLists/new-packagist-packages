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

## Latest list — 2026-11-01 08:21 UTC

New packages created between 2026-11-01 07:20 UTC and 2026-11-01 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T08-21-05-483434Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 07:21:07 | [kylewlawrence/laravel-betterstack-api](https://www.nuget.org/packages/kylewlawrence%2Flaravel-betterstack-api) | v13.0.0 | KyleWLawrence | Laravel API for BetterStack |
| 2026-11-01 07:21:08 | [kylewlawrence/gravity-forms-laravel](https://www.nuget.org/packages/kylewlawrence%2Fgravity-forms-laravel) | v13.0.0 | KyleWLawrence | Laravel wrapper for kylewlawrence/gravity-forms-api-client-php package |
| 2026-11-01 07:23:49 | [kylewlawrence/laravel-mainwp-api](https://www.nuget.org/packages/kylewlawrence%2Flaravel-mainwp-api) | v13.0.0 | KyleWLawrence | Laravel API for MainWP |
| 2026-11-01 07:26:09 | [kumanphp/kuman](https://www.nuget.org/packages/kumanphp%2Fkuman) | 0.1.0 |  | Long-running PHP microframework on Workerman with Express-style routing. |
| 2026-11-01 07:27:24 | [kylewlawrence/laravel-bunny-api](https://www.nuget.org/packages/kylewlawrence%2Flaravel-bunny-api) | v13.0.0 | KyleWLawrence | Laravel API for Bunny |
| 2026-11-01 07:27:25 | [kylewlawrence/laravel-cloudflare-api](https://www.nuget.org/packages/kylewlawrence%2Flaravel-cloudflare-api) | v13.0.0 | KyleWLawrence | Laravel API for Cloudflare |
| 2026-11-01 07:54:32 | [radebatz/openapi-json-schema](https://www.nuget.org/packages/radebatz%2Fopenapi-json-schema) | 0.1.0 | Martin Rademacher | Describes classes without OpenAPI attributes in the document swagger-php builds… |
| 2026-11-01 07:58:42 | [hipdevteam/ion-mu](https://www.nuget.org/packages/hipdevteam%2Fion-mu) | v3.5.4 | ION | ION MU — WordPress mu-plugin that fire-and-forgets activity events to Site Inte… |
| 2026-11-01 08:01:17 | [eamirgh/basalam-laravel](https://www.nuget.org/packages/eamirgh%2Fbasalam-laravel) | v1.0.0 | Amir Ghaffari | Comprehensive Laravel package for Basalam API Gateway and Core with DTO interfa… |
| 2026-11-01 08:13:07 | [soe-moe/laravel-module-generator](https://www.nuget.org/packages/soe-moe%2Flaravel-module-generator) | 1.0 | Soe Moe Oo | Artisan commands for scaffolding modular Laravel applications, with optional In… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
