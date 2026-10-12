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

## Latest list — 2026-10-12 19:19 UTC

New packages created between 2026-10-12 18:18 UTC and 2026-10-12 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T19-19-29-863467Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 18:19:16 | [adaa/shipping](https://www.nuget.org/packages/adaa%2Fshipping) | v0.1.0 | AdaaSystem | Framework-agnostic multi-carrier shipping library for PHP with optional Laravel… |
| 2026-10-12 18:21:45 | [adaa/shipping-filament](https://www.nuget.org/packages/adaa%2Fshipping-filament) | v0.2.0 | AdaaSystem | Optional Filament admin UI for adaa/shipping: manage platform and merchant ship… |
| 2026-10-12 18:39:28 | [wilycode/profiler](https://www.nuget.org/packages/wilycode%2Fprofiler) | v0.1.0 | Simon Piter | Framework-independent profiling contracts and value objects for PHP. |
| 2026-10-12 18:55:57 | [manuxi/sulu-glossary-bundle](https://www.nuget.org/packages/manuxi%2Fsulu-glossary-bundle) | v1.0.0 | Manuxi | Glossary bundle for Sulu CMS: abbreviations, acronyms and terms with draft/live… |
| 2026-10-12 18:59:25 | [wilycode/profiler-php](https://www.nuget.org/packages/wilycode%2Fprofiler-php) | v0.1.0 | Simon Piter | Framework-independent PHP profiler with aggregated metrics, traces and Server-T… |
| 2026-10-12 19:03:30 | [reagordi/package-template](https://www.nuget.org/packages/reagordi%2Fpackage-template) | 1.0 |  | Package template for creating repositories |
| 2026-10-12 19:05:05 | [php-io-extensions/box2d](https://www.nuget.org/packages/php-io-extensions%2Fbox2d) | v0.10.5 | Project Saturn Studios, LLC | 1:1 PHP bindings of Box2D 3.1.1, with the library compiled into the extension |
| 2026-10-12 19:07:45 | [khush/india-pincodes](https://www.nuget.org/packages/khush%2Findia-pincodes) | v1.0.0 | Khush | Offline India PIN code lookup: every post office for a PIN with its type, deliv… |
| 2026-10-12 19:09:47 | [stuttter/wp-term-colors](https://www.nuget.org/packages/stuttter%2Fwp-term-colors) | 2.0.0 | John James Jacoby | Pretty colors for categories, tags, and other taxonomy terms |
| 2026-10-12 19:13:26 | [automattic/jetpack-woocommerce-stats](https://www.nuget.org/packages/automattic%2Fjetpack-woocommerce-stats) | v0.1.0 |  | WooCommerce: the WooCommerce section of the Premium Analytics dashboard. |
| 2026-10-12 19:14:10 | [wilycode/router-profiler](https://www.nuget.org/packages/wilycode%2Frouter-profiler) | v0.1.0 | Simon Piter | Optional routing and controller performance diagnostics for WilyCode Router. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
