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

## Latest list — 2026-11-21 05:20 UTC

New packages created between 2026-11-21 04:19 UTC and 2026-11-21 05:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T05-20-32-272753Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 04:40:17 | [pennweb/penn_global_metatags](https://www.nuget.org/packages/pennweb%2Fpenn_global_metatags) | 1.0.0 |  | Structured data and social sharing defaults for Penn Drupal sites: Organization… |
| 2026-11-21 05:01:18 | [westonruter/phpstan-diff](https://www.nuget.org/packages/westonruter%2Fphpstan-diff) | v1.0.0 | Weston Ruter | Run PHPStan and report only the errors on lines changed relative to a base bran… |
| 2026-11-21 05:06:47 | [pennweb/penn_upstream_social](https://www.nuget.org/packages/pennweb%2Fpenn_upstream_social) | 1.0.0 |  | Social sharing images for sites on the Penn upstream: each content type's own i… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
