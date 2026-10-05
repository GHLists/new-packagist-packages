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

## Latest list — 2026-10-05 04:22 UTC

New packages created between 2026-10-05 03:21 UTC and 2026-10-05 04:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T04-22-00-385229Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 03:34:03 | [mage2kishan/module-error-monitor](https://www.nuget.org/packages/mage2kishan%2Fmodule-error-monitor) | 1.6.4 | Kishan Savaliya | Panth Error Monitor - smart, secure error management for Magento 2. Captures PH… |
| 2026-10-05 04:10:22 | [zhandos717/moonshine-monitoring](https://www.nuget.org/packages/zhandos717%2Fmoonshine-monitoring) | v1.3.0 | Zhandos | Server monitoring for MoonShine with real-time resource usage tracking |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
