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

## Latest list — 2026-10-09 08:18 UTC

New packages created between 2026-10-09 07:19 UTC and 2026-10-09 08:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T08-18-47-939942Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 07:27:24 | [pharaonic/php-smart-enum](https://www.nuget.org/packages/pharaonic%2Fphp-smart-enum) | 8.5.1 | Moamen Eltouny (Raggi) | Smart, lightweight helpers for native PHP enums. |
| 2026-10-09 07:49:36 | [ghijk/mailroom](https://www.nuget.org/packages/ghijk%2Fmailroom) | v1.0.0 |  | A private development and staging email inbox in the Statamic Control Panel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
