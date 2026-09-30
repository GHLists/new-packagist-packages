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

## Latest list — 2026-09-30 07:19 UTC

New packages created between 2026-09-30 06:21 UTC and 2026-09-30 07:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T07-19-39-493197Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 06:28:00 | [pixelfix/pixelfix](https://www.nuget.org/packages/pixelfix%2Fpixelfix) | 0.1.0 |  | PixelFix application starter |
| 2026-09-30 06:36:44 | [mage2kishan/module-quickview](https://www.nuget.org/packages/mage2kishan%2Fmodule-quickview) | 1.0.11 | Kishan Savaliya | Smart Quick View & Compare module for Magento 2 with Hyva theme support. Featur… |
| 2026-09-30 06:39:56 | [mage2kishan/module-smart-badge](https://www.nuget.org/packages/mage2kishan%2Fmodule-smart-badge) | 1.0.10 |  | Smart Product Badge & Label System - Automatically displays beautiful badges on… |
| 2026-09-30 06:43:29 | [mage2kishan/module-zipcode-validation](https://www.nuget.org/packages/mage2kishan%2Fmodule-zipcode-validation) | 1.0.8 | Kishan Savaliya | Panth ZipcodeValidation — validates ZIP/PIN codes at checkout against configura… |
| 2026-09-30 06:59:20 | [resvg-php/resvg](https://www.nuget.org/packages/resvg-php%2Fresvg) | v0.1.0+resvg.0.48.1 | Fojle Rabbi (Rabib) | Render SVG to PNG in-process, backed by a statically linked build of resvg |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
