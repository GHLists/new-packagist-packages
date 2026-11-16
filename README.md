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

## Latest list — 2026-11-16 06:20 UTC

New packages created between 2026-11-16 05:21 UTC and 2026-11-16 06:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T06-20-22-046163Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 05:28:09 | [kafyx-3/permission-gate](https://www.nuget.org/packages/kafyx-3%2Fpermission-gate) | v1.1.0 | kafyx-3 | Lightweight Laravel Gate & Blade directive helper — zero config, zero assumptio… |
| 2026-11-16 05:55:16 | [usualtool/ut-douyin](https://www.nuget.org/packages/usualtool%2Fut-douyin) | v1.0.1 | Huang Hui | UsualTool Framework Extension:Douyin. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
