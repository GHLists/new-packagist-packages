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

## Latest list — 2026-10-18 15:20 UTC

New packages created between 2026-10-18 14:18 UTC and 2026-10-18 15:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T15-20-28-712069Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 14:23:25 | [stoneholl/module-core](https://www.nuget.org/packages/stoneholl%2Fmodule-core) | v1.0.0 |  | Offline shared administration and product registry infrastructure for Stoneholl… |
| 2026-10-18 14:26:47 | [mk-josias/laravel-distributable](https://www.nuget.org/packages/mk-josias%2Flaravel-distributable) | v0.3.0 | Josias Mekontso | The foundations for designing each Laravel module as a microservice: its code r… |
| 2026-10-18 14:41:50 | [mk-josias/laravel-distributable-starter](https://www.nuget.org/packages/mk-josias%2Flaravel-distributable-starter) | v0.3.0 |  | Starter kit for laravel-distributable-modules: a modular monolith deployable as… |
| 2026-10-18 14:50:09 | [dskripchenko/php-pdf-pkcs11](https://www.nuget.org/packages/dskripchenko%2Fphp-pdf-pkcs11) | v1.0.0 | Denis Skripchenko | PKCS#11 signer for dskripchenko/php-pdf: sign PDFs (PAdES, RSA and ECDSA) with… |
| 2026-10-18 14:50:21 | [dskripchenko/php-pdf-cloud-kms](https://www.nuget.org/packages/dskripchenko%2Fphp-pdf-cloud-kms) | v1.0.0 | Denis Skripchenko | Cloud KMS signers for dskripchenko/php-pdf: sign PDFs (PAdES, RSA and ECDSA) wi… |
| 2026-10-18 14:51:46 | [saurabhg/module-buy-now](https://www.nuget.org/packages/saurabhg%2Fmodule-buy-now) | 1.0.0 |  | Buy Now button on product and listing pages that takes the customer straight to… |
| 2026-10-18 15:16:25 | [shankscode/haki](https://www.nuget.org/packages/shankscode%2Fhaki) | v1.0.0 |  | Miniframework PHP simples para APIs REST, com rotas, injeção de dependências, m… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
