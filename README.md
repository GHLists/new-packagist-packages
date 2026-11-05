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

## Latest list — 2026-11-05 23:20 UTC

New packages created between 2026-11-05 22:20 UTC and 2026-11-05 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T23-20-50-619056Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 22:47:06 | [webwizardsusa/filament-rich-editor-plus](https://www.nuget.org/packages/webwizardsusa%2Ffilament-rich-editor-plus) | v0.1.0 | Jamie Holly | A plugin-driven, TipTap based rich editor for Filament with a Gutenberg style b… |
| 2026-11-05 22:56:56 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.19.0 |  | The skeleton application for the Laravel framework. |
| 2026-11-05 23:03:07 | [rzkhrv/php-wallet-core-protobuf](https://www.nuget.org/packages/rzkhrv%2Fphp-wallet-core-protobuf) | 4.8.7 |  | PHP Protobuf classes generated from Trust Wallet Core schemas |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
