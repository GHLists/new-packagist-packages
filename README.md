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

## Latest list — 2026-11-24 16:21 UTC

New packages created between 2026-11-24 15:20 UTC and 2026-11-24 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T16-21-57-774352Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 15:23:10 | [zaver/openmage-payment](https://www.nuget.org/packages/zaver%2Fopenmage-payment) | 1.0.1 | Zaver | Zaver Checkout payment module for OpenMage LTS (Magento 1): pay later, instalme… |
| 2026-11-24 15:59:22 | [mrdellimore/rusty-sheet](https://www.nuget.org/packages/mrdellimore%2Frusty-sheet) | 0.1.2 |  | Rust-powered PHP extension for streaming XLSX and CSV: OpenSpout-compatible rea… |
| 2026-11-24 16:03:26 | [rylacdang/formcast](https://www.nuget.org/packages/rylacdang%2Fformcast) | v0.1.0 | Ryan Lester Lacdang | Cast your Laravel FormRequest rules to typed Zod schemas, TypeScript types, and… |
| 2026-11-24 16:12:13 | [eshimischi/vendor-cleanup](https://www.nuget.org/packages/eshimischi%2Fvendor-cleanup) | v2.0.1 | eshimischi | Global CLI tool & Composer plugin to strip tests, docs, and dev files from vend… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
