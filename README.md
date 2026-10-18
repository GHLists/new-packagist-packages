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

## Latest list — 2026-10-18 11:21 UTC

New packages created between 2026-10-18 10:21 UTC and 2026-10-18 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T11-21-11-307379Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 10:33:56 | [ehundu/andamio-documentacion](https://www.nuget.org/packages/ehundu%2Fandamio-documentacion) | v0.16.0 |  | Una documentación hecha con Ehundu, con menú por secciones, índice de cada pági… |
| 2026-10-18 10:40:15 | [lsr/translations](https://www.nuget.org/packages/lsr%2Ftranslations) | 0.1.0 | Tomáš Vojík | Framework-neutral native gettext localization runtime with optional Laravel int… |
| 2026-10-18 10:42:09 | [coretsia/platform-cli](https://www.nuget.org/packages/coretsia%2Fplatform-cli) | v0.9.0 | Vladyslav Mudrichenko | Coretsia CLI runtime package: tag-first command discovery, Kernel operations, a… |
| 2026-10-18 10:53:09 | [ehundu/andamio-portfolio](https://www.nuget.org/packages/ehundu%2Fandamio-portfolio) | v0.16.0 |  | Un portfolio personal hecho con Ehundu, con proyectos destacados, una ficha por… |
| 2026-10-18 10:58:50 | [hanzala-afzal/laravel-dynamic-throttle](https://www.nuget.org/packages/hanzala-afzal%2Flaravel-dynamic-throttle) | v0.1.0-beta.1 | Hanzala Afzal | Runtime-managed, identity-aware rate limiting for Laravel: change limits withou… |
| 2026-10-18 11:05:31 | [molokaistudiocom/magento2-log-viewer](https://www.nuget.org/packages/molokaistudiocom%2Fmagento2-log-viewer) | v1.0.0 |  | Read-only viewer for the var/log files in the Magento 2 admin: tail, page back,… |
| 2026-10-18 11:15:43 | [ehundu/andamio-negocio](https://www.nuget.org/packages/ehundu%2Fandamio-negocio) | v0.16.0 |  | Un sitio para un negocio local hecho con Ehundu, con servicios, horarios con ex… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
