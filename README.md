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

## Latest list — 2026-10-07 04:20 UTC

New packages created between 2026-10-07 03:21 UTC and 2026-10-07 04:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T04-20-31-112952Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 03:47:03 | [cloud-castle/click-house](https://www.nuget.org/packages/cloud-castle%2Fclick-house) | v0.1.0 | CloudCastle | Production-ready PHP 8.1+ package (CloudCastle ClickHouse). |
| 2026-10-07 03:49:32 | [kipchak/middleware-auth-hmac](https://www.nuget.org/packages/kipchak%2Fmiddleware-auth-hmac) | 1.1 |  | The Official HMAC Request Signing Middleware for the Kipchak API Development Ki… |
| 2026-10-07 03:53:38 | [adeguntoro/j2fakit](https://www.nuget.org/packages/adeguntoro%2Fj2fakit) | v1.0.0 | adeguntoro | 2FA gate package: by default every route requires login+2FA, whitelist via conf… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
