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

## Latest list — 2026-11-13 08:20 UTC

New packages created between 2026-11-13 07:19 UTC and 2026-11-13 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T08-20-19-09178Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 07:21:58 | [sandritsch91/php-ntlm](https://www.nuget.org/packages/sandritsch91%2Fphp-ntlm) | 1.0.0 | James Armes; Sandritsch91 | Library for communicating with Microsoft services using NTLM authentication. |
| 2026-11-13 07:29:21 | [wazum/visual-permissions](https://www.nuget.org/packages/wazum%2Fvisual-permissions) | v0.2.0 | Wolfgang Klinger | Edit TYPO3 backend group permissions directly on the relevant screens. |
| 2026-11-13 07:34:58 | [rft/laravel-attachment](https://www.nuget.org/packages/rft%2Flaravel-attachment) | v1.0 |  | Single source of truth transactional file attachment package and Yii2-style att… |
| 2026-11-13 07:36:33 | [mhinspeya/special-promotion](https://www.nuget.org/packages/mhinspeya%2Fspecial-promotion) | 1.0.0 | MHinspeya | Turn Magento Cart Price Rules into clear, on-brand storefront campaign badges —… |
| 2026-11-13 07:40:59 | [initred/laravel-langfuse](https://www.nuget.org/packages/initred%2Flaravel-langfuse) | v1.0.0 | initred | Langfuse PHP SDK for Laravel, built for the Laravel AI SDK |
| 2026-11-13 07:52:28 | [vergil-lai/lexsift-ffi](https://www.nuget.org/packages/vergil-lai%2Flexsift-ffi) | v0.2.0 | Vergil | Rust-powered keyword matching for PHP through FFI, with precompiled native libr… |
| 2026-11-13 08:05:12 | [walkboy/yii2-basic-access](https://www.nuget.org/packages/walkboy%2Fyii2-basic-access) | 1.0.0 | Vitaly Walkboy | Base auth behavior for yii2 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
