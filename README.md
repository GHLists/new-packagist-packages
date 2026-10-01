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

## Latest list — 2026-10-01 04:20 UTC

New packages created between 2026-10-01 03:20 UTC and 2026-10-01 04:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T04-20-15-600276Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 03:40:52 | [scottchiefbaker/yaml-polyfill](https://www.nuget.org/packages/scottchiefbaker%2Fyaml-polyfill) | v0.1.0 | Scott Baker | Pure-PHP polyfill for the PECL php-yaml extension: yaml_emit(), yaml_parse(), a… |
| 2026-10-01 03:50:29 | [jamescarr/ankusa](https://www.nuget.org/packages/jamescarr%2Fankusa) | v0.3.0 |  | Client SDK for Ankusa deployments: the claim-check gateway client, the route-ma… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
