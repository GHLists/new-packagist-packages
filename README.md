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

## Latest list — 2026-11-08 14:19 UTC

New packages created between 2026-11-08 13:19 UTC and 2026-11-08 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T14-19-28-848887Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 13:47:31 | [btinet/untis-bundle](https://www.nuget.org/packages/btinet%2Funtis-bundle) | 1.0 |  | Import GPU-Files from Untis. |
| 2026-11-08 13:57:51 | [deburca/phorward](https://www.nuget.org/packages/deburca%2Fphorward) | 0.1.0 | Paddy de Búrca | Offload PHP lint, phpcs, phpstan and phpunit runs to an SSH-reachable server, e… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
