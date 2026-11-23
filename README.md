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

## Latest list — 2026-11-23 08:20 UTC

New packages created between 2026-11-23 07:20 UTC and 2026-11-23 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T08-20-16-886593Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 07:23:56 | [php-concept/component-auth-api-token](https://www.nuget.org/packages/php-concept%2Fcomponent-auth-api-token) | v1.0.0 |  | Concept component — Bearer API token authentication scaffold |
| 2026-11-23 07:59:07 | [dmsandhika/ocr-client](https://www.nuget.org/packages/dmsandhika%2Focr-client) | v1.0.1 | dmsandhika | Official PHP Client SDK for OCR Service (KTP, MyKad IC, Passport, and Receipts) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
