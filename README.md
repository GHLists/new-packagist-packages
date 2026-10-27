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

## Latest list — 2026-10-27 21:20 UTC

New packages created between 2026-10-27 20:21 UTC and 2026-10-27 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T21-20-56-662592Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 20:45:41 | [xdiego1st/laravel-mapku](https://www.nuget.org/packages/xdiego1st%2Flaravel-mapku) | v1.0.1 | Rasyid Abdul Halim | Enterprise-grade Reusable GIS & Interactive Mapping Package for Laravel based o… |
| 2026-10-27 20:50:53 | [tryhackx/flarum-homepage-blocks](https://www.nuget.org/packages/tryhackx%2Fflarum-homepage-blocks) | 2.13.0 | TryHackX | Customizable homepage blocks for tracker-style Flarum forums featuring dual sta… |
| 2026-10-27 21:03:10 | [snb4crazy/laravel-magic-link-auth](https://www.nuget.org/packages/snb4crazy%2Flaravel-magic-link-auth) | v1.0.0 |  | Magic link authentication package for Laravel APIs with Sanctum support. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
