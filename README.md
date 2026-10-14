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

## Latest list — 2026-10-14 19:20 UTC

New packages created between 2026-10-14 18:20 UTC and 2026-10-14 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T19-20-06-033665Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 18:25:52 | [myadion/sdk](https://www.nuget.org/packages/myadion%2Fsdk) | v0.2.0 | Adion | Official PHP library for the Adion Cloud API: Adion Pay, SMS and every other en… |
| 2026-10-14 18:41:21 | [pdftoolkit/pdf-to-html](https://www.nuget.org/packages/pdftoolkit%2Fpdf-to-html) | v0.1.1 | Mathias STRASSER | Explicit object-oriented derivation of tagged PDF to semantic HTML for PHP 8.3+ |
| 2026-10-14 18:42:39 | [psbits/crafter](https://www.nuget.org/packages/psbits%2Fcrafter) | 1.0.0 | Daniel Ablass | Code and file generator for TYPO3 extensions |
| 2026-10-14 18:53:38 | [angeo/module-webmcp](https://www.nuget.org/packages/angeo%2Fmodule-webmcp) | 1.0.0 |  | WebMCP for Magento 2 — registers structured tools (product search, product deta… |
| 2026-10-14 19:09:21 | [cloakwp/image-transformations](https://www.nuget.org/packages/cloakwp%2Fimage-transformations) | v0.1.0 |  | Composable, PHP-configured image transformation pipelines for WordPress. |
| 2026-10-14 19:11:29 | [meil/meil-php](https://www.nuget.org/packages/meil%2Fmeil-php) | 0.1.0 | meil.ro | Official PHP client for the meil.ro email API: transactional email and newslett… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
