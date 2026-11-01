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

## Latest list — 2026-11-01 22:20 UTC

New packages created between 2026-11-01 21:18 UTC and 2026-11-01 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T22-20-37-161211Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 21:31:09 | [uams-web/aether-redirects](https://www.nuget.org/packages/uams-web%2Faether-redirects) | v0.1.0 | UAMS Web Services; Josh Daugh… | Redirect rules for Statamic: a redirects global set served on the 404 path, rul… |
| 2026-11-01 21:31:09 | [uams-web/statamic-redirects](https://www.nuget.org/packages/uams-web%2Fstatamic-redirects) | v0.1.0 | UAMS Web Services; Josh Daugh… | Redirect rules for Statamic: a redirects global set served on the 404 path, rul… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
