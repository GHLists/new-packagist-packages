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

## Latest list — 2026-10-17 09:19 UTC

New packages created between 2026-10-17 08:19 UTC and 2026-10-17 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T09-19-06-608049Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 08:39:50 | [egough/laravel-github](https://www.nuget.org/packages/egough%2Flaravel-github) | v1.0.2 |  | GitHub App connections, repository browsing and pull request search for Laravel. |
| 2026-10-17 08:59:09 | [ssmiff/mezzio-container-helpers](https://www.nuget.org/packages/ssmiff%2Fmezzio-container-helpers) | v0.1.0 | Scott Smith | Attribute-driven constructor injection for Mezzio and Laminas service manager f… |
| 2026-10-17 09:07:48 | [ssmiff/mezzio-doctrine](https://www.nuget.org/packages/ssmiff%2Fmezzio-doctrine) | v0.1.0 | Scott Smith | Doctrine DBAL, ORM and Migrations for Mezzio with named connections selectable… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
