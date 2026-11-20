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

## Latest list — 2026-11-20 01:21 UTC

New packages created between 2026-11-20 00:19 UTC and 2026-11-20 01:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T01-21-09-17547Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 00:31:19 | [phalcon/volt](https://www.nuget.org/packages/phalcon%2Fvolt) | v1.0.0 | Phalcon Team; Contributors | Phalcon Volt is an HTML template engine for server-side rendering. |
| 2026-11-20 00:35:37 | [inengine/modulus](https://www.nuget.org/packages/inengine%2Fmodulus) | v0.1.0-beta.2 | James Johnson | Modulus — module runtime for InEngine (enable/disable, discovery, lifecycle, do… |
| 2026-11-20 00:36:02 | [inengine/modulus-composer](https://www.nuget.org/packages/inengine%2Fmodulus-composer) | v0.1.0-beta.2 | James Johnson | Modulus Composer — Composer client for InEngine Modulus (require/remove/update,… |
| 2026-11-20 01:05:36 | [inengine/core](https://www.nuget.org/packages/inengine%2Fcore) | 0.1.0-beta.1 |  | InEngine Core — opinionated Laravel-based modular application builder framework |
| 2026-11-20 01:07:51 | [phalcon/phql](https://www.nuget.org/packages/phalcon%2Fphql) | v1.0.0 | Phalcon Team | Phalcon Query Language (PHQL) |
| 2026-11-20 01:15:55 | [dackou/bazi](https://www.nuget.org/packages/dackou%2Fbazi) | v1.0 | dackou | 用于八字（四柱）排盘的 PHP 组件。 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
