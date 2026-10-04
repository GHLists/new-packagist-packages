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

## Latest list — 2026-10-04 17:20 UTC

New packages created between 2026-10-04 16:21 UTC and 2026-10-04 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T17-20-43-333781Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 16:22:03 | [masterlink/mpesa-dependency](https://www.nuget.org/packages/masterlink%2Fmpesa-dependency) | v1.0.0 | Moniz Sitoe | online payment manager using mpesa gateway |
| 2026-10-04 17:01:59 | [mage2kishan/module-crosslinks](https://www.nuget.org/packages/mage2kishan%2Fmodule-crosslinks) | 1.1.5 |  | Automatic internal crosslinks for Magento 2 (Hyva + Luma). Converts configured… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
