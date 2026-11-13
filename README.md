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

## Latest list — 2026-11-13 07:19 UTC

New packages created between 2026-11-13 06:21 UTC and 2026-11-13 07:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T07-19-16-96707Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 06:31:10 | [liberusoftware/module-accounting-erp](https://www.nuget.org/packages/liberusoftware%2Fmodule-accounting-erp) | 1.0.0 |  | Integrated ERP workflows and the existing application accounting schema. |
| 2026-11-13 06:31:19 | [liberusoftware/module-accounting-erp-filament](https://www.nuget.org/packages/liberusoftware%2Fmodule-accounting-erp-filament) | 1.0.0 |  | Filament resources, pages, widgets, and portal presentation for the ERP runtime. |
| 2026-11-13 06:31:29 | [liberusoftware/module-accounting-erp-http](https://www.nuget.org/packages/liberusoftware%2Fmodule-accounting-erp-http) | 1.0.0 |  | HTTP controllers, API resources, and routes for the ERP runtime. |
| 2026-11-13 06:44:53 | [tinymvc/tinypdf](https://www.nuget.org/packages/tinymvc%2Ftinypdf) | v1.0.0 | Shahin Moyshan | Fast, dependency-free Modern HTML to PDF generator for PHP 8.2+ |
| 2026-11-13 07:00:39 | [jumphp/webrtc](https://www.nuget.org/packages/jumphp%2Fwebrtc) | v0.5.53 |  | WebRTC for JumPHP games and apps: peer-to-peer data channels and screen video,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
