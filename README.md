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

## Latest list — 2026-10-04 21:21 UTC

New packages created between 2026-10-04 20:20 UTC and 2026-10-04 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T21-21-16-187377Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 20:24:07 | [citomni/image](https://www.nuget.org/packages/citomni%2Fimage) | v1.0.0 | Lars Grove Mortensen | Deterministic, reusable image inspection, transformation and encoding for CitOm… |
| 2026-10-04 20:33:00 | [ibrahimjml/laravel-modules](https://www.nuget.org/packages/ibrahimjml%2Flaravel-modules) | v1.0 |  | Laravel modules generator |
| 2026-10-04 20:46:09 | [justinholtweb/craft-glue](https://www.nuget.org/packages/justinholtweb%2Fcraft-glue) | 5.0.0 | Justin Holt | Merge two entries into one in Craft CMS — pick a winner field by field, combine… |
| 2026-10-04 20:50:16 | [zhandos717/qazaq-inflector](https://www.nuget.org/packages/zhandos717%2Fqazaq-inflector) | v0.5.0 | Zhandos Zhandarbekov | Declension of Kazakh names, full names and pronouns: 7 cases, possessive forms,… |
| 2026-10-04 20:56:33 | [juaniquillo/slate-backend-components](https://www.nuget.org/packages/juaniquillo%2Fslate-backend-components) | v0.1.1 | juaniquillo | Slate backend components for Laravel. |
| 2026-10-04 21:03:09 | [notonfire/php](https://www.nuget.org/packages/notonfire%2Fphp) | v1.0.0 |  | NotOnFire for Laravel and PHP: error tracking with strict privacy defaults and… |
| 2026-10-04 21:10:04 | [mage2kishan/module-banner-slider](https://www.nuget.org/packages/mage2kishan%2Fmodule-banner-slider) | 1.0.18 | Kishan Savaliya | Panth Banner Slider Module - Responsive banner slider widget with Luma and Hyva… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
