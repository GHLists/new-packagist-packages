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

## Latest list — 2026-10-17 17:21 UTC

New packages created between 2026-10-17 16:18 UTC and 2026-10-17 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T17-21-30-939884Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 16:22:08 | [jeffersongoncalves/filament-saved-filter](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-saved-filter) | 2.0.0 |  |  |
| 2026-10-17 16:22:55 | [raingad/webman-storage](https://www.nuget.org/packages/raingad%2Fwebman-storage) | 0.1.0 | Raingad; ShaoBo Wan(無尘) | Webman file storage and upload plugin (local / Aliyun OSS / Tencent COS / Qiniu… |
| 2026-10-17 16:23:51 | [hellotext/magento](https://www.nuget.org/packages/hellotext%2Fmagento) | 1.0.0 |  | Connect Magento Open Source stores to Hellotext: storefront activity, customer… |
| 2026-10-17 16:34:56 | [ernestdefoe/curio](https://www.nuget.org/packages/ernestdefoe%2Fcurio) | v1.0.0 | Ernest Defoe | Members show off what they collect: games, vinyl, books, films, LEGO, cards, an… |
| 2026-10-17 16:52:43 | [helturkey/bidi](https://www.nuget.org/packages/helturkey%2Fbidi) | v1.0.0 |  | Unicode bidirectional text processing and Arabic shaping for PHP |
| 2026-10-17 17:04:06 | [jeffersongoncalves/laravel-saved-filter](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-saved-filter) | 1.0.0 | Jefferson Gonçalves | Saved table filters for Laravel: store, share and restore filters, sort, search… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
