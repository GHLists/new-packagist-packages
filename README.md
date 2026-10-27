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

## Latest list — 2026-10-27 04:19 UTC

New packages created between 2026-10-27 03:21 UTC and 2026-10-27 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T04-19-47-341065Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 03:28:36 | [koamishin/auth-php](https://www.nuget.org/packages/koamishin%2Fauth-php) | v1.0.0 | Yukazakiri; Koamishin Core Te… | Official PHP and Laravel SDK for Koamishin Centralized Authentication Portal wi… |
| 2026-10-27 03:38:14 | [hughcube/phpinfo](https://www.nuget.org/packages/hughcube%2Fphpinfo) | v1.0.0 | hugh.li | Restore phpinfo() plain text in CLI/Swoole/Workerman into 1:1 pixel-perfect nat… |
| 2026-10-27 03:51:08 | [klsoft/keycloak-client](https://www.nuget.org/packages/klsoft%2Fkeycloak-client) | 1.0.0 |  | A PHP library that can be used to secure web applications with Keycloak. |
| 2026-10-27 03:52:53 | [fastd/dobee-demo](https://www.nuget.org/packages/fastd%2Fdobee-demo) | v1.1.1 | JanHuang | Demo application package for FastD dobee skeleton |
| 2026-10-27 03:54:35 | [particle-academy/charlotte](https://www.nuget.org/packages/particle-academy%2Fcharlotte) | v0.1.0 |  | Headless website-builder agent kit for Laravel: CMS page tools over fancy-cms d… |
| 2026-10-27 04:10:23 | [contenir/contenir-navigation-mezzio](https://www.nuget.org/packages/contenir%2Fcontenir-navigation-mezzio) | v0.1.0 |  | Draws a Contenir site's managed menus in Mezzio: each live menu as a Laminas Na… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
