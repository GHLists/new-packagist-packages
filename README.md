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

## Latest list — 2026-10-27 07:19 UTC

New packages created between 2026-10-27 06:20 UTC and 2026-10-27 07:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T07-19-14-510688Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 06:27:39 | [paymenku/sdk-php](https://www.nuget.org/packages/paymenku%2Fsdk-php) | v0.1.0 |  | SDK PHP untuk API Paymenku |
| 2026-10-27 06:32:52 | [itmosoft/laravel-media](https://www.nuget.org/packages/itmosoft%2Flaravel-media) | v1.0.0 |  | A reusable media management package for Laravel applications. |
| 2026-10-27 06:46:03 | [kianhugh/mtphp](https://www.nuget.org/packages/kianhugh%2Fmtphp) | v1.0.0 | 武汉麦麦心选网络科技有限公司 | mtphp - 高性能、高并发 PHP 框架 |
| 2026-10-27 07:18:26 | [xerxes/eimzo](https://www.nuget.org/packages/xerxes%2Feimzo) | v0.1.0 |  | Reusable headless E-IMZO signing, desktop client and encrypted certificate vault |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
