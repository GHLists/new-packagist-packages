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

## Latest list — 2026-10-01 03:20 UTC

New packages created between 2026-10-01 02:19 UTC and 2026-10-01 03:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T03-20-40-377141Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 02:46:53 | [amtgard/environment-loader](https://www.nuget.org/packages/amtgard%2Fenvironment-loader) | v1.0.0 |  | Environment-agnostic PHP include path selection for composition roots (Registry… |
| 2026-10-01 02:58:00 | [starfruit/post-bundle](https://www.nuget.org/packages/starfruit%2Fpost-bundle) | 0.0.1 | Nguyen Hoang Anh | Starfruit Post Bundle |
| 2026-10-01 03:03:19 | [verifaid/verifaid-php](https://www.nuget.org/packages/verifaid%2Fverifaid-php) | v1.0.1 | VerifAID | Official VerifAID PHP SDK for extracting data from Indonesian identity document… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
