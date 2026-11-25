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

## Latest list — 2026-11-25 21:21 UTC

New packages created between 2026-11-25 20:18 UTC and 2026-11-25 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T21-21-19-815467Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 20:30:33 | [kurama/framework](https://www.nuget.org/packages/kurama%2Fframework) | v1.0.0 | berlium | Kurama - a lightweight, standalone PHP micro framework by berlium. |
| 2026-11-25 21:02:39 | [wernerkrauss/silverstripe-contact](https://www.nuget.org/packages/wernerkrauss%2Fsilverstripe-contact) | v0.1.0 |  | Simple contact module for Silverstripe CMS |
| 2026-11-25 21:02:39 | [wernerkrauss/silverstripe-umami](https://www.nuget.org/packages/wernerkrauss%2Fsilverstripe-umami) | v0.1.0 |  | Umami analytics integration for Silverstripe: SiteConfig settings, environment-… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
