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

## Latest list — 2026-10-08 07:19 UTC

New packages created between 2026-10-08 06:20 UTC and 2026-10-08 07:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T07-19-10-064631Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 06:26:34 | [venusian/build](https://www.nuget.org/packages/venusian%2Fbuild) | 0.10.1 | Angel Gonzalez | Compiles a Venusian app into a native executable. Installed by venusian install… |
| 2026-10-08 06:30:46 | [gecka/wp-admin-menu](https://www.nuget.org/packages/gecka%2Fwp-admin-menu) | v1.0.0 | Laurent Dinclaux | A top-level WordPress admin menu several plugins share: pages made of tabs each… |
| 2026-10-08 07:01:15 | [wpstarter/o-canvas-core](https://www.nuget.org/packages/wpstarter%2Fo-canvas-core) | v2.0 |  | Code Generators Builder for Laravel Applications and Packages |
| 2026-10-08 07:06:50 | [drakelid/librenms-ups-battery](https://www.nuget.org/packages/drakelid%2Flibrenms-ups-battery) | v1.0.0 |  | LibreNMS plugin: rank devices by a selected sensor class (UPS runtime, load, ch… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
