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

## Latest list — 2026-11-20 05:19 UTC

New packages created between 2026-11-20 04:21 UTC and 2026-11-20 05:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T05-19-09-841186Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 04:30:50 | [stolt/hyde-git-meta](https://www.nuget.org/packages/stolt%2Fhyde-git-meta) | v0.9.1 | Raphael Stolt | Git commit metadata for HydePHP pages and posts at build time. |
| 2026-11-20 04:46:42 | [steinhaug/email_routes_hq](https://www.nuget.org/packages/steinhaug%2Femail_routes_hq) | v0.9.9 | Kim Steinhaug | Transactional email dispatch with MySQL-backed volume limits and delivery histo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
