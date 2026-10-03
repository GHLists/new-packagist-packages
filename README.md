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

## Latest list — 2026-10-03 04:21 UTC

New packages created between 2026-10-03 03:21 UTC and 2026-10-03 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T04-21-50-868546Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 03:35:21 | [migears/wiring](https://www.nuget.org/packages/migears%2Fwiring) | 2.0.0 | Sam X. Xu | Config-driven container wiring — load a PHP array of factories and register it… |
| 2026-10-03 04:07:58 | [blutrixx/nativephp-pdf-viewer](https://www.nuget.org/packages/blutrixx%2Fnativephp-pdf-viewer) | v0.1.0 |  | PDF preview and native sharing for NativePHP Mobile applications |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
