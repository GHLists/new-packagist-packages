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

## Latest list — 2026-10-06 02:20 UTC

New packages created between 2026-10-06 01:20 UTC and 2026-10-06 02:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T02-20-10-318253Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 01:29:28 | [contenir/contenir-resource-laminas-mvc](https://www.nuget.org/packages/contenir%2Fcontenir-resource-laminas-mvc) | v2.0.0-RC1 |  | laminas-mvc adapter for contenir/contenir-resource: workflow routing and naviga… |
| 2026-10-06 01:30:22 | [servicem8/servicem8-php](https://www.nuget.org/packages/servicem8%2Fservicem8-php) | v1.3.0 |  | PHP SDK for the ServiceM8 API |
| 2026-10-06 01:45:37 | [siberfx/netgsm](https://www.nuget.org/packages/siberfx%2Fnetgsm) | 5.1.0 | Selim Görmüş | NetGsm SMS, OTP, reporting, balance and IYS integration for Laravel |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
