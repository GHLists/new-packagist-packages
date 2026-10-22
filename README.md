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

## Latest list — 2026-10-22 00:19 UTC

New packages created between 2026-10-21 23:19 UTC and 2026-10-22 00:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T00-19-40-537156Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 23:24:59 | [widgetic/api-sdk-php](https://www.nuget.org/packages/widgetic%2Fapi-sdk-php) | 1.11.66 | Widgetic | API documentation for the Widgetic API Gateway |
| 2026-10-21 23:56:27 | [phpsyntax/phpsyntax](https://www.nuget.org/packages/phpsyntax%2Fphpsyntax) | v1.0.0 | David Grudl | 🌳 PhpSyntax: a lossless concrete syntax tree (CST) for PHP. Every token, space… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
