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

## Latest list — 2026-10-08 21:21 UTC

New packages created between 2026-10-08 20:22 UTC and 2026-10-08 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T21-21-26-812126Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 20:32:08 | [d9-technologies/matcher](https://www.nuget.org/packages/d9-technologies%2Fmatcher) | v1.0.0 | Ethan Elshyeb; James Haynes | levenshtein example |
| 2026-10-08 20:32:20 | [d9-technologies/textract](https://www.nuget.org/packages/d9-technologies%2Ftextract) | v1.0.0 | Ethan Elshyeb; James Haynes |  |
| 2026-10-08 20:50:39 | [4oh3/live-files](https://www.nuget.org/packages/4oh3%2Flive-files) | 1.0.0 |  | Serves images (and optionally other public files) from the live site instead of… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
