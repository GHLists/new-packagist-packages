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

## Latest list — 2026-11-26 22:20 UTC

New packages created between 2026-11-26 21:20 UTC and 2026-11-26 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T22-20-07-904098Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 21:25:57 | [directorytree/progress](https://www.nuget.org/packages/directorytree%2Fprogress) | v1.0.1 | Steve Bauman | Track the progress of long-running work in Laravel applications. |
| 2026-11-26 21:41:33 | [adachsoft/workflow-step-social](https://www.nuget.org/packages/adachsoft%2Fworkflow-step-social) | v0.2.0 | Arkadiusz Adach | Social media publishing step for AdachSoft workflows. |
| 2026-11-26 22:02:34 | [portpro/document-reader](https://www.nuget.org/packages/portpro%2Fdocument-reader) | v0.1.0 |  | Self-hosted text, table and labeled-field extraction for documents and images. |
| 2026-11-26 22:07:34 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.52.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
