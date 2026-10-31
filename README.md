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

## Latest list — 2026-10-31 10:19 UTC

New packages created between 2026-10-31 09:21 UTC and 2026-10-31 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T10-19-36-742177Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 09:25:39 | [milwad/pcreators](https://www.nuget.org/packages/milwad%2Fpcreators) | v1.0.0 | Milwad Khosravi | An interactive CLI to scaffold a production-ready PHP/Laravel package in second… |
| 2026-10-31 09:41:25 | [norialabs/approvals](https://www.nuget.org/packages/norialabs%2Fapprovals) | v0.1.2 |  | Maker-checker approvals for Laravel. Holds Eloquent creates, updates and delete… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
