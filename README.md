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

## Latest list — 2026-10-25 00:21 UTC

New packages created between 2026-10-24 23:20 UTC and 2026-10-25 00:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T00-21-38-915979Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 23:46:36 | [absolutoffice/xcurl](https://www.nuget.org/packages/absolutoffice%2Fxcurl) | v1.1.0 | Absolut Office | HTTPS transport and policy client with cURL, PHP streams, and direct TLS socket… |
| 2026-10-24 23:46:38 | [se7enxweb/flysystem](https://www.nuget.org/packages/se7enxweb%2Fflysystem) | 1.1.11 | Frank de Jonge | Filesystem abstraction: Many filesystems, one API. |
| 2026-10-25 00:09:33 | [morvy/rector-woocommerce](https://www.nuget.org/packages/morvy%2Frector-woocommerce) | v0.1.0 | morvy | Rector upgrade rules for WooCommerce |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
