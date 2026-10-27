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

## Latest list — 2026-10-27 01:18 UTC

New packages created between 2026-10-27 00:19 UTC and 2026-10-27 01:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T01-18-47-338223Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 00:23:51 | [karelwintersky/arris.auth](https://www.nuget.org/packages/karelwintersky%2Farris.auth) | 0.2.0 | Karel Wintersky | Arris µFramework: standalone authentication with session cookies and bearer tok… |
| 2026-10-27 00:37:03 | [contenir/contenir-site-token](https://www.nuget.org/packages/contenir%2Fcontenir-site-token) | v0.1.0 |  | Signed one-time tokens between the Contenir CMS and a site: compact HS256 token… |
| 2026-10-27 00:55:22 | [yukazakiri/starterkit-updater](https://www.nuget.org/packages/yukazakiri%2Fstarterkit-updater) | v0.1.0 | Nejc Cotic; yukazakiri | Sync Laravel starter-kit projects with their upstream repositories |
| 2026-10-27 00:59:56 | [aanggakrishna/laravel-browser-cache-manager](https://www.nuget.org/packages/aanggakrishna%2Flaravel-browser-cache-manager) | v1.0.0 |  | Safe, opt-in browser cache version management for Laravel applications. |
| 2026-10-27 01:10:49 | [lumynus/lumy](https://www.nuget.org/packages/lumynus%2Flumy) | v1.0.0 | Weleny | MicroORM from Lumynus |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
