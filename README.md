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

## Latest list — 2026-11-20 19:19 UTC

New packages created between 2026-11-20 18:21 UTC and 2026-11-20 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T19-19-24-77754Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 18:30:48 | [sellissimo/core](https://www.nuget.org/packages/sellissimo%2Fcore) | v1.0.0-beta.24 |  | Sellissimo for Statamic 6. |
| 2026-11-20 18:30:59 | [sellissimo/shipping-flat-rate](https://www.nuget.org/packages/sellissimo%2Fshipping-flat-rate) | v1.0.0-beta.24 |  | Flat Rate Shipping for Sellissimo for Statamic 6. |
| 2026-11-20 18:45:07 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.38.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
