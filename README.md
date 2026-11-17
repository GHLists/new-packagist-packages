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

## Latest list — 2026-11-17 04:19 UTC

New packages created between 2026-11-17 03:21 UTC and 2026-11-17 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T04-19-38-241133Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 03:37:40 | [techbaripress/laravel](https://www.nuget.org/packages/techbaripress%2Flaravel) | v1.0.0 |  | News Bridge for Laravel: one command installs the connector that receives auto-… |
| 2026-11-17 03:46:12 | [alibabacloud/qweneduaisuite-20261102](https://www.nuget.org/packages/alibabacloud%2Fqweneduaisuite-20261102) | 1.0.0 | Alibaba Cloud SDK | Alibaba Cloud QwenEduAiSuite (20261102) SDK Library for PHP |
| 2026-11-17 03:47:16 | [alnaggar/laravel-remember-valid-cache](https://www.nuget.org/packages/alnaggar%2Flaravel-remember-valid-cache) | 1.0 | Ahmad Muhammad Rashad | Conditionally refresh Laravel cache values while retaining the last valid value. |
| 2026-11-17 03:51:39 | [jeffersongoncalves/filament-lgpd-vendors](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-lgpd-vendors) | 2.0.0 |  |  |
| 2026-11-17 03:51:40 | [jeffersongoncalves/filament-lgpd-ripd](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-lgpd-ripd) | 2.0.0 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
