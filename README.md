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

## Latest list — 2026-10-16 06:22 UTC

New packages created between 2026-10-16 05:21 UTC and 2026-10-16 06:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T06-22-24-536983Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 05:24:14 | [schachbulle/contao-kinderschutzdokumente-bundle](https://www.nuget.org/packages/schachbulle%2Fcontao-kinderschutzdokumente-bundle) | 1.0.0 | Frank Hoppe | Mitglieder reichen Kinderschutz-Unterlagen wie das erweiterte Führungszeugnis o… |
| 2026-10-16 05:24:16 | [1994/reviews-statamic](https://www.nuget.org/packages/1994%2Freviews-statamic) | v1.1.0 | 1994 | Reviews and ratings for Statamic, collected on your own site: a review form for… |
| 2026-10-16 05:34:25 | [pharaonic/php-diff](https://www.nuget.org/packages/pharaonic%2Fphp-diff) | 8.0.0 | Moamen Eltouny (Raggi) | Semantic structured diffs and GitHub-style text diffs for PHP: added, removed,… |
| 2026-10-16 05:47:23 | [hypervel/guzzle-promises](https://www.nuget.org/packages/hypervel%2Fguzzle-promises) | 3.0.2.1 | Graham Campbell; Michael Dowl… | Hypervel's fork of the Guzzle promises library |
| 2026-10-16 06:05:00 | [srako/webman-kms](https://www.nuget.org/packages/srako%2Fwebman-kms) | v0.1.0 |  | Aliyun KMS local-agent (sidecar) secrets client for webman: fetch MySQL/Redis c… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
