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

## Latest list — 2026-11-10 07:20 UTC

New packages created between 2026-11-10 06:21 UTC and 2026-11-10 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T07-20-59-393535Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 06:25:46 | [anikeen/console](https://www.nuget.org/packages/anikeen%2Fconsole) | 1.0.0 | René Preuß; Maurice Preuß | PHP Anikeen Console API client for Laravel 12+ |
| 2026-11-10 06:30:14 | [totalcms/starter-photographer](https://www.nuget.org/packages/totalcms%2Fstarter-photographer) | v1.0.0 | Joe Workman | Wren Alder: a photographer's site for Total CMS, with projects, session package… |
| 2026-11-10 06:49:48 | [reeyanto/minimvc](https://www.nuget.org/packages/reeyanto%2Fminimvc) | 0.1.0 | Riyanto | A lightweight custom PHP MVC framework with ORM, Query Builder, Relations, and… |
| 2026-11-10 06:50:49 | [solspace/craft-dark-mode](https://www.nuget.org/packages/solspace%2Fcraft-dark-mode) | 1.0.0 | Solspace | Give Craft’s control panel a darker look, with support for your favorite plugin… |
| 2026-11-10 06:51:01 | [lgz2688/mongo-builder](https://www.nuget.org/packages/lgz2688%2Fmongo-builder) | 1.0.0 | lgz2688 | A chainable MongoDB builder with a MySQL-like API, pluggable ID generation and… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
