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

## Latest list — 2026-10-12 09:23 UTC

New packages created between 2026-10-12 08:21 UTC and 2026-10-12 09:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T09-23-09-616739Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 08:50:23 | [oceancodex/wpsp-lite](https://www.nuget.org/packages/oceancodex%2Fwpsp-lite) | 13.1.61 | OceanCodex | WPSP Framework - WordPress Starter Plugin - Lite |
| 2026-10-12 08:52:01 | [oceancodex/wpsp-core-lite](https://www.nuget.org/packages/oceancodex%2Fwpsp-core-lite) | 13.1.61 | OceanCodex | WPSP Framework - WordPress Starter Plugin - Core - Lite |
| 2026-10-12 08:56:35 | [mabioca/jalali-calendar](https://www.nuget.org/packages/mabioca%2Fjalali-calendar) | v1.0.0 |  | Jalali calendar and Persian numeral support for Flarum. |
| 2026-10-12 09:08:56 | [silarhi/qif-library](https://www.nuget.org/packages/silarhi%2Fqif-library) | 1.0.0 | SILARHI | A PHP library to parse and write QIF (Quicken Interchange Format) files |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
