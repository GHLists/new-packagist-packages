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

## Latest list — 2026-11-23 02:19 UTC

New packages created between 2026-11-23 01:19 UTC and 2026-11-23 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T02-19-05-334011Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 01:26:09 | [sightpress/theme-template](https://www.nuget.org/packages/sightpress%2Ftheme-template) | 0.1.0 |  | A starting point for a SightPress theme: SightPress is a powerful CMS for every… |
| 2026-11-23 01:51:02 | [acerdp/acerdp](https://www.nuget.org/packages/acerdp%2Facerdp) | v1.1.0 |  | Client for the AceRDP API: Windows RDP and Linux VPS servers. |
| 2026-11-23 02:01:33 | [fiberphp/database](https://www.nuget.org/packages/fiberphp%2Fdatabase) | v0.1.0 | PangBin | 🗄️ FiberPHP 数据库组件 —— 基于 PDO 的连接池、查询构造器、驱动抽象层、协程安全。 |
| 2026-11-23 02:14:21 | [thebeardedbear/urssaf-dpae](https://www.nuget.org/packages/thebeardedbear%2Furssaf-dpae) | v0.1.0 | The Bearded Bear | Client and domain model for the URSSAF "API DPAE" (Déclaration Préalable À l'Em… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
