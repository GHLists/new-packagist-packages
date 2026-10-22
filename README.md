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

## Latest list — 2026-10-22 22:22 UTC

New packages created between 2026-10-22 21:21 UTC and 2026-10-22 22:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T22-22-14-767591Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 21:26:06 | [hypra/laravel](https://www.nuget.org/packages/hypra%2Flaravel) | v0.1.0 |  | Hypra views for Laravel: .hypra pages rendered as HTML, Markdown or JSON |
| 2026-10-22 21:26:06 | [hypra/runtime](https://www.nuget.org/packages/hypra%2Fruntime) | v0.1.0 |  | Runtime for PHP pages compiled by the Hypra compiler |
| 2026-10-22 21:27:16 | [psbits/xlf-editor](https://www.nuget.org/packages/psbits%2Fxlf-editor) | 0.1.0-alpha | Daniel Ablass | Backend module which allows to edit XLF files. Developmental state, not intende… |
| 2026-10-22 21:41:41 | [offmania9/boostack-framework](https://www.nuget.org/packages/offmania9%2Fboostack-framework) | 6.3.91 | Stefano Spagnolo; Alessio Deb… | The Boostack core framework. |
| 2026-10-22 22:07:30 | [siberfx/laravel-rustfs](https://www.nuget.org/packages/siberfx%2Flaravel-rustfs) | 1.0.0 | Selim Görmüş | RustFS for Laravel 13+: S3 data plane (buckets, objects, versioning, object loc… |
| 2026-10-22 22:09:35 | [pteal79/geo-map](https://www.nuget.org/packages/pteal79%2Fgeo-map) | 1.0.0 | Peter Teal | A native map for NativePHP Mobile with coloured markers and shaded circles size… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
