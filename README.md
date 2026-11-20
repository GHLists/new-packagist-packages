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

## Latest list — 2026-11-20 11:21 UTC

New packages created between 2026-11-20 10:21 UTC and 2026-11-20 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T11-21-39-0437Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 10:25:47 | [soshopay/sdk](https://www.nuget.org/packages/soshopay%2Fsdk) | v1.0.0 |  | Thin PSR-18 Soshopay API client |
| 2026-11-20 10:37:46 | [masilia/ibexa-icons](https://www.nuget.org/packages/masilia%2Fibexa-icons) | 0.1.0 | MasiliaLabs | The icons of the content types and groups of Ibexa, chosen at run time (registr… |
| 2026-11-20 10:39:12 | [plokko/laravel-bulkgate](https://www.nuget.org/packages/plokko%2Flaravel-bulkgate) | 0.0.1 | Francesco Pellerone | Laravel BulkGate API integration |
| 2026-11-20 10:56:57 | [angeo/module-ai-assist](https://www.nuget.org/packages/angeo%2Fmodule-ai-assist) | 1.0.0 | Ievgenii Gryshkun | Optional AI assistant for the Angeo AEO admin pages in Magento 2. Explains audi… |
| 2026-11-20 11:13:19 | [codeverseindia/tourkinet-travel-app](https://www.nuget.org/packages/codeverseindia%2Ftourkinet-travel-app) | v1.1.0 |  | Tour Kinet Travel Application - Packages, Blogs, Destinations and Inquiries |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
