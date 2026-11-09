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

## Latest list — 2026-11-09 17:21 UTC

New packages created between 2026-11-09 16:21 UTC and 2026-11-09 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T17-21-30-600716Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 16:27:21 | [vielhuber/healthspace](https://www.nuget.org/packages/vielhuber%2Fhealthspace) | 1.0.1 |  | Personal health dashboard with manual measurements and Google Health integratio… |
| 2026-11-09 16:32:22 | [intragile/laravel-company-lookup](https://www.nuget.org/packages/intragile%2Flaravel-company-lookup) | v1.0.1 | IntrAgile Kft. | Look up companies in free official business registries worldwide through one La… |
| 2026-11-09 16:46:05 | [automattic/jetpack-monetize](https://www.nuget.org/packages/automattic%2Fjetpack-monetize) | v0.1.0 |  | The Monetize dashboard: payments, paid subscribers and ads in wp-admin. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
