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

## Latest list — 2026-10-12 16:19 UTC

New packages created between 2026-10-12 15:22 UTC and 2026-10-12 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T16-19-35-887403Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 15:27:26 | [tmonier/sylius-container-fill-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-container-fill-plugin) | v1.0.0 | Thibaut Monier | Pallet & Truckload Builder for Sylius 2: container types, logistics data per va… |
| 2026-10-12 15:27:26 | [wazum/visual-permissions](https://www.nuget.org/packages/wazum%2Fvisual-permissions) | v0.1.1 | Wolfgang Klinger | Edit TYPO3 backend group permissions directly on the relevant screens. |
| 2026-10-12 15:29:04 | [tmonier/sylius-company-accounts-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-company-accounts-plugin) | v1.0.0 | Thibaut Monier | B2B company accounts for Sylius 2: companies with members and roles (admin, buy… |
| 2026-10-12 15:40:15 | [inupress/editor-ckeditor](https://www.nuget.org/packages/inupress%2Feditor-ckeditor) | v0.1.0 |  | CKEditor 5 for the Inupress admin: replaces the built-in editor in every conten… |
| 2026-10-12 15:41:58 | [gatovel/queue](https://www.nuget.org/packages/gatovel%2Fqueue) | v1.0.0 |  | Sistema de filas e processamento de jobs para aplicações PHP. |
| 2026-10-12 15:59:16 | [johnykvsky/quidam](https://www.nuget.org/packages/johnykvsky%2Fquidam) | v0.0.1 | Johny Kvsky | Dummy / fake data generator for PHP 8.4+ - DummyGenerator architecture (contain… |
| 2026-10-12 15:59:45 | [trisnawan/php-rss-client](https://www.nuget.org/packages/trisnawan%2Fphp-rss-client) | 1.0.0 | Trisnawan | Ambil dan posting artikel dari RSS |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
