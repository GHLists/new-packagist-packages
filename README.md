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

## Latest list — 2026-09-29 19:21 UTC

New packages created between 2026-09-29 18:20 UTC and 2026-09-29 19:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T19-21-09-520622Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 18:23:17 | [syriable/maintenance-guard](https://www.nuget.org/packages/syriable%2Fmaintenance-guard) | 1.0.0 | Syriable | Dynamic, extensible access control for Laravel's native maintenance mode. |
| 2026-09-29 18:37:28 | [mage2kishan/module-admin-menu-manager](https://www.nuget.org/packages/mage2kishan%2Fmodule-admin-menu-manager) | 1.0.11 | Kishan Savaliya | Customises the Magento 2 backend menu — hide, rename, re-icon, recolor, reorder… |
| 2026-09-29 18:37:30 | [augustash/mna_neo](https://www.nuget.org/packages/augustash%2Fmna_neo) | 1.0.0 |  | Neo Alchemist components shared by MNA sites. |
| 2026-09-29 18:42:56 | [iberfacil/eidas-cert-auth](https://www.nuget.org/packages/iberfacil%2Feidas-cert-auth) | v0.1.1 | Marco Gavilán | Autentica en PHP con certificados eIDAS (FNMT, DNIe y UE), listas de confianza… |
| 2026-09-29 18:46:59 | [mage2kishan/module-advanced-contact-us](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-contact-us) | 1.0.13 |  | Advanced Contact Us Page - Custom fields, bot protection, submission management… |
| 2026-09-29 18:51:30 | [bifrostcrypto/sdk](https://www.nuget.org/packages/bifrostcrypto%2Fsdk) | v0.1.0 |  | Official Bifrost Crypto API client for PHP |
| 2026-09-29 19:03:55 | [mage2kishan/module-advanced-product-grid](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-product-grid) | 1.0.8 | Kishan Savaliya | Advanced Product Grid for Magento 2 admin - inline edit every column (text, sel… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
