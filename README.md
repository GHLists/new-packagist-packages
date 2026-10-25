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

## Latest list — 2026-10-25 06:21 UTC

New packages created between 2026-10-25 05:20 UTC and 2026-10-25 06:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T06-21-18-566159Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 05:30:02 | [exsited/exsited](https://www.nuget.org/packages/exsited%2Fexsited) | v4.0.0 | Ashiq Rahman | PHP SDK for the Exsited v4 REST API. |
| 2026-10-25 05:32:27 | [atannex/routing](https://www.nuget.org/packages/atannex%2Frouting) | v1.1.0 | Atanga Leke Collins | Attribute routing for Laravel: declare routes on the controllers themselves and… |
| 2026-10-25 06:00:27 | [skarner2016/rbac](https://www.nuget.org/packages/skarner2016%2Frbac) | v0.1.0 | skarner2016 | Framework-agnostic RBAC for PHP: role-only permissions with menu, route and but… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
