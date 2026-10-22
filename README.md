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

## Latest list — 2026-10-22 17:20 UTC

New packages created between 2026-10-22 16:19 UTC and 2026-10-22 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T17-20-55-779648Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 16:23:35 | [jamesthe1/mini-html-builder](https://www.nuget.org/packages/jamesthe1%2Fmini-html-builder) | v2.0.0 | Jamesthe1 | A miniature HTML builder. |
| 2026-10-22 16:48:16 | [filagora/filagora-plugins-security](https://www.nuget.org/packages/filagora%2Ffilagora-plugins-security) | v0.1.0 |  | Security scanning and quarantine for Filagora Plugins: static PHP checks, ClamA… |
| 2026-10-22 16:49:49 | [nodonhq/filament-bodega-lite](https://www.nuget.org/packages/nodonhq%2Ffilament-bodega-lite) | v1.0.0 |  | Bodega Lite: a warm, highly legible Filament theme for shops and small business… |
| 2026-10-22 16:57:43 | [tmonier/sylius-customer-asset-management-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-customer-asset-management-plugin) | v0.1.0 | Thibaut Monier | Customer asset management for Sylius 2: customers declare their equipment fleet… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
