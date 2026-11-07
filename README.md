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

## Latest list — 2026-11-07 13:19 UTC

New packages created between 2026-11-07 12:19 UTC and 2026-11-07 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T13-19-49-358912Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 12:31:24 | [opscale-co/nova-genbi](https://www.nuget.org/packages/opscale-co%2Fnova-genbi) | 1.0.0 | Opscale | Generative BI for Laravel Nova: chat with an AI that reads your database schema… |
| 2026-11-07 12:58:20 | [fruitcake/magento2-health-check](https://www.nuget.org/packages/fruitcake%2Fmagento2-health-check) | v0.1.0 | Fruitcake | Magento 2 health check endpoint with pluggable checks |
| 2026-11-07 13:01:19 | [sovware/plugin-scaffold-cli](https://www.nuget.org/packages/sovware%2Fplugin-scaffold-cli) | v0.1.0 |  | Interactive setup command for WP Plugin Scaffold |
| 2026-11-07 13:03:04 | [sovware/wp-plugin-scaffold](https://www.nuget.org/packages/sovware%2Fwp-plugin-scaffold) | v0.0.1 | Syed Galib |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
