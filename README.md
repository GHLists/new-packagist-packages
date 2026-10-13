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

## Latest list — 2026-10-13 03:19 UTC

New packages created between 2026-10-13 02:20 UTC and 2026-10-13 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T03-19-30-306877Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 02:53:34 | [shimomo/autorace-news-collector](https://www.nuget.org/packages/shimomo%2Fautorace-news-collector) | 0.1.0 | shimomo | Collects the latest AutoRace news from official feeds and APIs. |
| 2026-10-13 03:08:26 | [imagewize/woo-og-product-tags](https://www.nuget.org/packages/imagewize%2Fwoo-og-product-tags) | v1.0.0 | Imagewize | Prints the Open Graph product tags (product:price:amount, product:price:currenc… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
