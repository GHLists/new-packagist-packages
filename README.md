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

## Latest list — 2026-10-21 22:20 UTC

New packages created between 2026-10-21 21:21 UTC and 2026-10-21 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T22-20-09-161874Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 21:31:38 | [gcego/blueprints](https://www.nuget.org/packages/gcego%2Fblueprints) | v1.0.0 | Atangageih Leke Collins | Declarative feature definitions for GCEGO Admin Studio: Blueprint::define() wit… |
| 2026-10-21 21:55:33 | [ecuafact/sdk](https://www.nuget.org/packages/ecuafact%2Fsdk) | v1.0.0-beta4 | Ecuanexus | Cliente oficial en PHP del API publico de facturacion electronica Ecuafact (con… |
| 2026-10-21 22:05:03 | [considbrs-webdev/modularity-folder-browser](https://www.nuget.org/packages/considbrs-webdev%2Fmodularity-folder-browser) | 1.0.0 | Consid Borås AB | An accessible file and folder browser module for Modularity. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
