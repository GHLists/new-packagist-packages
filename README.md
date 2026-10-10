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

## Latest list — 2026-10-10 06:20 UTC

New packages created between 2026-10-10 05:20 UTC and 2026-10-10 06:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T06-20-36-475687Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 05:36:06 | [suvera/winter-modules](https://www.nuget.org/packages/suvera%2Fwinter-modules) | 2.1.6 | Suvera | Winter Boot modules |
| 2026-10-10 06:17:26 | [caiyun/sms](https://www.nuget.org/packages/caiyun%2Fsms) | v1.0.0 |  | Multi-driver SMS package for Laravel supporting Aliyun, Tencent, Huawei, Volcen… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
