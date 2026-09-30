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

## Latest list — 2026-09-30 18:20 UTC

New packages created between 2026-09-30 17:22 UTC and 2026-09-30 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T18-20-54-92036Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 17:32:28 | [hypnokizer/formbuilder](https://www.nuget.org/packages/hypnokizer%2Fformbuilder) | v7.0.0 | Nathan Kizer | Class to build HTML forms |
| 2026-09-30 17:34:09 | [uverify/uverify-php](https://www.nuget.org/packages/uverify%2Fuverify-php) | v0.1.0 | Elasto Web Services Limited | Official PHP library for the UVerify API: BVN, NIN and ID checks, liveness, fac… |
| 2026-09-30 17:53:58 | [goldnead/statamic-bard-assist](https://www.nuget.org/packages/goldnead%2Fstatamic-bard-assist) | v1.0.0 | Adrian Goldner | Suggests which Bard set each paragraph should become, and fills its fields. |
| 2026-09-30 17:54:06 | [hypnokizer/validator](https://www.nuget.org/packages/hypnokizer%2Fvalidator) | v7.0.0 | Nathan Kizer | Class to validate a dataset. |
| 2026-09-30 18:05:57 | [hypnokizer/database](https://www.nuget.org/packages/hypnokizer%2Fdatabase) | v7.0.0 | Nathan Kizer | Class to execute queries using PDO and SQLite3 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
