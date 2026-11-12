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

## Latest list — 2026-11-12 21:18 UTC

New packages created between 2026-11-12 20:21 UTC and 2026-11-12 21:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T21-18-58-186025Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 20:44:20 | [letterncms/minimal](https://www.nuget.org/packages/letterncms%2Fminimal) | 0.1.0 |  | A home page, an about page and a blog with three posts, on one typeface and a c… |
| 2026-11-12 21:07:22 | [alexxvl/problem-details](https://www.nuget.org/packages/alexxvl%2Fproblem-details) | v0.1.0 |  | RFC 9457 Problem Details for Laravel APIs |
| 2026-11-12 21:13:25 | [davidhirtz/yii2-forms](https://www.nuget.org/packages/davidhirtz%2Fyii2-forms) | 3.0.0 | David Hirtz | Frontend forms with bot protection and mail delivery based on Yii 2.0 framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
