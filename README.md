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

## Latest list — 2026-10-20 19:21 UTC

New packages created between 2026-10-20 18:19 UTC and 2026-10-20 19:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T19-21-12-347697Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 18:24:22 | [stougeiro/pdo-database](https://www.nuget.org/packages/stougeiro%2Fpdo-database) | v1.0.0 | stougeiro | A dialect-agnostic PDO model for SQLite, MySQL, MariaDB and PostgreSQL. |
| 2026-10-20 18:43:34 | [edgeinfinity/diy-homepage](https://www.nuget.org/packages/edgeinfinity%2Fdiy-homepage) | v0.1.0 | EdgeInfinity | A configurable, widget-based homepage for Flarum, with a Friends of Flarum Widg… |
| 2026-10-20 18:49:08 | [atriametal/sylius-cookie-consent-plugin](https://www.nuget.org/packages/atriametal%2Fsylius-cookie-consent-plugin) | v0.1.0 | Atriametal | Collects the cookie consent of the visitors of a Sylius shop, blocks scripts an… |
| 2026-10-20 18:56:31 | [hardimpactdev/sync-engine](https://www.nuget.org/packages/hardimpactdev%2Fsync-engine) | v0.1.0 | Nick Retel | Local-first sync for Laravel: a per-scope change feed, a push endpoint and real… |
| 2026-10-20 19:08:31 | [kgkg/sentry-dedupe](https://www.nuget.org/packages/kgkg%2Fsentry-dedupe) | v0.1.0 |  | Fail-closed persistent admission control for Sentry PHP events |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
