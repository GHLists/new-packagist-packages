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

## Latest list — 2026-09-28 11:20 UTC

New packages created between 2026-09-28 10:26 UTC and 2026-09-28 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T11-20-15-53005Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 10:49:55 | [incident-io/sdk-php](https://www.nuget.org/packages/incident-io%2Fsdk-php) | v1.0.0 | incident.io | PHP client for the incident.io API, generated from the published OpenAPI schema. |
| 2026-09-28 11:08:11 | [christianjbrown/code-quality-scripts](https://www.nuget.org/packages/christianjbrown%2Fcode-quality-scripts) | v1.0.0 | Christian Brown | An opinionated PHP_CodeSniffer standard and PHP CS Fixer rule sets (risky and s… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
