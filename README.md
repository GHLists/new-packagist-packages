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

## Latest list — 2026-10-27 16:18 UTC

New packages created between 2026-10-27 15:20 UTC and 2026-10-27 16:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T16-18-49-052781Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 15:26:09 | [borders-dev/craft-imagor](https://www.nuget.org/packages/borders-dev%2Fcraft-imagor) | v1.1.0 | Borders Web Development | Hands Craft's image transforms to imagor (libvips), so the site's server never… |
| 2026-10-27 15:32:07 | [dartmoon/prestashop-installer](https://www.nuget.org/packages/dartmoon%2Fprestashop-installer) | v1.0.0 | Dartmoon | Global CLI installer for Dartmoon PrestaShop modules |
| 2026-10-27 15:32:14 | [ttpryg/comment-engine](https://www.nuget.org/packages/ttpryg%2Fcomment-engine) | v1.0.0 | Toto | A framework-agnostic standalone comment engine library for PHP. |
| 2026-10-27 15:33:24 | [dartmoon/prestashop-module-toolkit](https://www.nuget.org/packages/dartmoon%2Fprestashop-module-toolkit) | v1.0.0 |  | Module development components for PrestaShop 9.2 |
| 2026-10-27 15:36:50 | [3brs/sentry-throttle-bundle](https://www.nuget.org/packages/3brs%2Fsentry-throttle-bundle) | v1.0.0 | 3BRS | Symfony bundle that throttles Sentry events per fingerprint and per application… |
| 2026-10-27 15:46:42 | [pollora/woocommerce](https://www.nuget.org/packages/pollora%2Fwoocommerce) | v0.1.0 | Amphibee | WooCommerce for Pollora: its Blade templates, its template resolution, the Comi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
