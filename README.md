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

## Latest list — 2026-10-29 23:19 UTC

New packages created between 2026-10-29 22:21 UTC and 2026-10-29 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T23-19-59-748785Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 22:22:31 | [olgunozoktas/laravel-trusted-devices](https://www.nuget.org/packages/olgunozoktas%2Flaravel-trusted-devices) | v0.1.0 | Olgun Özoktaş | "Keep me signed in on this machine?" for Laravel: after a two-factor code, a tr… |
| 2026-10-29 22:36:41 | [infrawrench/bulk-instances](https://www.nuget.org/packages/infrawrench%2Fbulk-instances) | 1.0.0 | Infrawrench LLC | AWS EC2 instance attributes and pricing, with full history, from Infrawrench. |
| 2026-10-29 22:44:26 | [strukt/ar](https://www.nuget.org/packages/strukt%2Far) | 1.0.0 | pitsolu | A small query builder and active record ORM for SQL databases. |
| 2026-10-29 23:02:45 | [superroute/sapp](https://www.nuget.org/packages/superroute%2Fsapp) | v0.2.1 | Goodneo Solutions | sApp for PHP: sign-in, the platform app API, Open Platform capabilities and Sup… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
