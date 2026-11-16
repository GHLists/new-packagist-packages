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

## Latest list — 2026-11-16 09:22 UTC

New packages created between 2026-11-16 08:20 UTC and 2026-11-16 09:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T09-22-44-466148Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 08:43:47 | [jevo/jforms](https://www.nuget.org/packages/jevo%2Fjforms) | 1.0.0 |  | Secure Blade form submissions and responses for Evolution CMS |
| 2026-11-16 09:13:12 | [xiaoh0o/queue](https://www.nuget.org/packages/xiaoh0o%2Fqueue) | 1.0.0 |  | PHP queue |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
