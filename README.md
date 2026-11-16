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

## Latest list — 2026-11-16 01:19 UTC

New packages created between 2026-11-16 00:22 UTC and 2026-11-16 01:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T01-19-39-735147Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 00:23:49 | [sailantis/azera-roadrunner](https://www.nuget.org/packages/sailantis%2Fazera-roadrunner) | v0.4.2 | Sailantis | Application-server adapter that lets Azera run on RoadRunner. Serves HTTP and g… |
| 2026-11-16 00:54:53 | [brianhenryie/bh-wp-rate-limiter](https://www.nuget.org/packages/brianhenryie%2Fbh-wp-rate-limiter) | 1.0.0 | BrianHenryIE | Rate limiter using WordPress cache for storage. |
| 2026-11-16 01:10:34 | [qa-tracking/capture-bundle](https://www.nuget.org/packages/qa-tracking%2Fcapture-bundle) | v0.1.0 | Ricardo Ocaña | Adds backend context (trace ID, exception, logs and database rows) to the bug r… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
