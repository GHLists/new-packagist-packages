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

## Latest list — 2026-10-16 01:21 UTC

New packages created between 2026-10-16 00:20 UTC and 2026-10-16 01:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T01-21-37-981219Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 01:04:29 | [rawand201/kurdish-escpos](https://www.nuget.org/packages/rawand201%2Fkurdish-escpos) | v0.1.0 | RawanD201 | Print correctly shaped Kurdish (Sorani and Badini), Arabic and English receipts… |
| 2026-10-16 01:10:38 | [fewchurs/laravel](https://www.nuget.org/packages/fewchurs%2Flaravel) | v1.0.0 | Fewchurs | Drop a Fewchurs feature-request board into any Laravel app. |
| 2026-10-16 01:14:15 | [moduref/moduref](https://www.nuget.org/packages/moduref%2Fmoduref) | v0.1.0 | Muhamad Syamsudin | Lightweight referral engine based on existing user UUIDs with transactional row… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
