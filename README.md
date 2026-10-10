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

## Latest list — 2026-10-10 09:20 UTC

New packages created between 2026-10-10 08:19 UTC and 2026-10-10 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T09-20-21-179299Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 08:21:15 | [itxshakil/laravel-aadhaar-offline](https://www.nuget.org/packages/itxshakil%2Flaravel-aadhaar-offline) | v0.1.0 | Shakil Alam | Read and verify Aadhaar Offline e-KYC (share-code ZIP / signed XML) locally in… |
| 2026-10-10 08:22:27 | [jodeveloper/secure-share](https://www.nuget.org/packages/jodeveloper%2Fsecure-share) | v1.0.0 |  | Passcode-encrypted secret + attachment sharing for Laravel/Filament |
| 2026-10-10 08:46:14 | [surlinio/easycaptchas](https://www.nuget.org/packages/surlinio%2Feasycaptchas) | v1.0.0 | Surlinio B.V. | A lightweight, self-hosted and privacy-friendly CAPTCHA solution for PHP forms. |
| 2026-10-10 08:47:53 | [kwasii/laravel-sql-parser](https://www.nuget.org/packages/kwasii%2Flaravel-sql-parser) | v0.1.0 | Kwasi Sakyi Baidoo | Fast SQL Parser for PHP Laravel |
| 2026-10-10 09:08:56 | [elyar/laravel-service-tokens](https://www.nuget.org/packages/elyar%2Flaravel-service-tokens) | v0.1.0 | Elyar | Token authentication for service-to-service calls between Laravel apps, with pe… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
