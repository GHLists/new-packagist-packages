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

## Latest list — 2026-10-29 08:21 UTC

New packages created between 2026-10-29 07:21 UTC and 2026-10-29 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T08-21-06-09546Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 07:22:21 | [didit-protocol/sdk-php](https://www.nuget.org/packages/didit-protocol%2Fsdk-php) | v1.0.0 | Didit | The official Didit PHP library: identity verification (KYC), business verificat… |
| 2026-10-29 07:24:10 | [bluefairy/module-order-comments-hyva](https://www.nuget.org/packages/bluefairy%2Fmodule-order-comments-hyva) | v1.2.2 |  | BlueFairy Order Comments — Hyva Checkout companion module |
| 2026-10-29 07:31:02 | [firstlightui/local-ai](https://www.nuget.org/packages/firstlightui%2Flocal-ai) | v1.0.0-alpha1 |  | On-device text generation for NativePHP Mobile using the operating system's bui… |
| 2026-10-29 07:34:53 | [contenir/contenir-preview-mezzio](https://www.nuget.org/packages/contenir%2Fcontenir-preview-mezzio) | v0.1.0 |  | Mezzio renderer for the Contenir preview protocol: answers the CMS's signed pre… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
