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

## Latest list — 2026-10-27 15:20 UTC

New packages created between 2026-10-27 14:21 UTC and 2026-10-27 15:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T15-20-04-41326Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 14:22:54 | [rivalex/lingua](https://www.nuget.org/packages/rivalex%2Flingua) | v3.0.0 | Alessandro Rivolta | Self-hosted Laravel translation manager for the TALL stack: edit, sync, import/… |
| 2026-10-27 14:36:22 | [ipsocode/hypervel-serial](https://www.nuget.org/packages/ipsocode%2Fhypervel-serial) | v0.0.1 | Ipsocode | Serial port connections for Hypervel: named connections over a tty, framed prot… |
| 2026-10-27 14:52:10 | [jfrintrop/env-validator](https://www.nuget.org/packages/jfrintrop%2Fenv-validator) | v1.1.0 | J. Frintrop | Validate your environment variables against a schema — fail fast at boot or in… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
