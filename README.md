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

## Latest list — 2026-10-13 20:19 UTC

New packages created between 2026-10-13 19:21 UTC and 2026-10-13 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T20-19-25-28109Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 19:28:50 | [gavtaylor/sievefolders](https://www.nuget.org/packages/gavtaylor%2Fsievefolders) | v0.1.0 | Gavin Taylor | Keep Sieve filters pointing at the right folder when a folder is renamed or mov… |
| 2026-10-13 19:29:16 | [setechsolutions/eloquent-sales-force](https://www.nuget.org/packages/setechsolutions%2Feloquent-sales-force) | v3.0.0-rc.1 | SETechSolutions; Robert Lester | Work with Salesforce objects as Eloquent models: an Eloquent driver for SOQL an… |
| 2026-10-13 19:34:37 | [poletti/framework](https://www.nuget.org/packages/poletti%2Fframework) | v1.0.1 |  | A lightweight PHP framework |
| 2026-10-13 19:58:55 | [eduardoribeirodev/filament-canvas](https://www.nuget.org/packages/eduardoribeirodev%2Ffilament-canvas) | 0.1.0 |  | Reusable visual document editor for Filament with pluggable persistence, assets… |
| 2026-10-13 20:05:56 | [siratik/package-loader](https://www.nuget.org/packages/siratik%2Fpackage-loader) | v0.1.0 | Built North | Version coordinator for bundled WordPress packages. Ensures the newest copy of… |
| 2026-10-13 20:10:32 | [tezmanian/utils-validate](https://www.nuget.org/packages/tezmanian%2Futils-validate) | v1.0.0 | René Halberstadt | Lightweight PHP validation toolkit: guard assertions, boolean rules, schema val… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
