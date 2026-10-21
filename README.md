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

## Latest list — 2026-10-21 23:19 UTC

New packages created between 2026-10-21 22:20 UTC and 2026-10-21 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T23-19-38-148669Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 22:36:28 | [ranfury/silverstripe-cms-styles](https://www.nuget.org/packages/ranfury%2Fsilverstripe-cms-styles) | 1.0.0 | Ranfury | A fresh, modern style for the Silverstripe CMS. Blocks the core CMS styles and… |
| 2026-10-21 23:04:42 | [wielorzeczownik/phalcon-inertia](https://www.nuget.org/packages/wielorzeczownik%2Fphalcon-inertia) | v0.1.0 | wielorzeczownik | Inertia.js server adapter for Phalcon 3.4 to 5, with Ziggy style named routes f… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
