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

## Latest list — 2026-11-07 11:21 UTC

New packages created between 2026-11-07 10:20 UTC and 2026-11-07 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T11-21-41-665133Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 10:22:40 | [adedsec/nova-translated-labels](https://www.nuget.org/packages/adedsec%2Fnova-translated-labels) | v0.2.1 | Aref Maddah | Translate Laravel Nova menu groups, resources, fields, filters, actions and opt… |
| 2026-11-07 10:26:34 | [syedgalib/plugin-scaffold-cli](https://www.nuget.org/packages/syedgalib%2Fplugin-scaffold-cli) | v0.1.2 |  | Interactive setup command for WP Plugin Scaffold |
| 2026-11-07 10:42:00 | [syedgalib/wp-plugin-scaffold](https://www.nuget.org/packages/syedgalib%2Fwp-plugin-scaffold) | v0.0.1 | Syed Galib |  |
| 2026-11-07 10:47:48 | [deadxfire/srin](https://www.nuget.org/packages/deadxfire%2Fsrin) | v1.0.1 | Arindam Makar | Srin - Lightweight, Secure Core PHP Static Website Engine developed by Arindam… |
| 2026-11-07 11:14:22 | [relicsoftware/barakah-payment-gateway](https://www.nuget.org/packages/relicsoftware%2Fbarakah-payment-gateway) | v1.0.0 |  | The skeleton application for the Laravel framework. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
