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

## Latest list — 2026-10-31 13:19 UTC

New packages created between 2026-10-31 12:20 UTC and 2026-10-31 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T13-19-44-545492Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 12:28:19 | [imazeo/sdk](https://www.nuget.org/packages/imazeo%2Fsdk) | 1.0.0 | Imazeo | Official Imazeo PHP SDK for server-side image, transform, PDF, QR, and barcode… |
| 2026-10-31 12:32:16 | [pjadanowski/atlas](https://www.nuget.org/packages/pjadanowski%2Fatlas) | v0.1.0 | Paweł Jadanowski | Atlas — fast, static, three-column OpenAPI documentation for Laravel Scramble (… |
| 2026-10-31 12:53:33 | [survos/geoboundaries-bundle](https://www.nuget.org/packages/survos%2Fgeoboundaries-bundle) | 2.45.11 |  | Symfony bundle for fetching packaged geoBoundaries (administrative boundary pol… |
| 2026-10-31 12:59:49 | [survos/mapillary](https://www.nuget.org/packages/survos%2Fmapillary) | 2.45.12 |  | Typed read-only Mapillary API v4 image client using Symfony HttpClient and Seri… |
| 2026-10-31 12:59:54 | [survos/mapillary-bundle](https://www.nuget.org/packages/survos%2Fmapillary-bundle) | 2.45.13 |  | Thin Symfony integration for the survos/mapillary API client. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
