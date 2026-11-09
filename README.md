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

## Latest list — 2026-11-09 11:20 UTC

New packages created between 2026-11-09 10:20 UTC and 2026-11-09 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T11-20-47-027704Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 10:24:30 | [dzwallet/php-sdk](https://www.nuget.org/packages/dzwallet%2Fphp-sdk) | v0.2.0 |  | Plain PHP SDK for the DzWallet payment API (CIB / Edahabia via SATIM, payment l… |
| 2026-11-09 10:25:51 | [omnibridge/doctrine](https://www.nuget.org/packages/omnibridge%2Fdoctrine) | v1.0.0-rc.1 | Marco Meyer | The storage glue of omnibase sites, framework-free: Doctrine reading the struct… |
| 2026-11-09 10:25:51 | [omnibridge/eloquent](https://www.nuget.org/packages/omnibridge%2Feloquent) | v1.0.0-rc.1 | Marco Meyer | omnibase's entities on Eloquent's database layer, framework-free: illuminate/da… |
| 2026-11-09 10:25:51 | [omnibridge/laravel](https://www.nuget.org/packages/omnibridge%2Flaravel) | v1.0.0-rc.1 | Marco Meyer | The Laravel host of omnisense/omnibase: its Foundation contracts (urls, transla… |
| 2026-11-09 10:25:51 | [omnibridge/symfony](https://www.nuget.org/packages/omnibridge%2Fsymfony) | v1.0.0-rc.1 | Marco Meyer | The Symfony host of omnisense/omnibridge's contracts (urls, translations, acces… |
| 2026-11-09 10:25:51 | [omnibridge/twig](https://www.nuget.org/packages/omnibridge%2Ftwig) | v1.0.0-rc.1 | Marco Meyer | The Twig side of omnibridge: the contract a page rendered with Twig asks of any… |
| 2026-11-09 10:25:51 | [omnisense/omnibase](https://www.nuget.org/packages/omnisense%2Fomnibase) | v5.0.0-rc.1 | Marco Meyer | omnibase: entities, view models, contracts, forms and helpers for any PHP host;… |
| 2026-11-09 10:25:51 | [omnisense/omnibridge](https://www.nuget.org/packages/omnisense%2Fomnibridge) | v1.0.0-rc.1 | Marco Meyer | The core of the omnibridge family: the contracts any host answers for an applic… |
| 2026-11-09 10:32:38 | [phponwheels/phponwheels](https://www.nuget.org/packages/phponwheels%2Fphponwheels) | v0.1.0 | tekki3 | A safe PHP framework that runs identically on its own server, FrankenPHP, nginx… |
| 2026-11-09 10:40:34 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.24.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-09 10:45:53 | [captns/statamic-matomo-chatbots](https://www.nuget.org/packages/captns%2Fstatamic-matomo-chatbots) | v0.0.4 |  | Server-side Matomo tracking for AI chatbot requests |
| 2026-11-09 10:47:30 | [envoice/module-einvoice](https://www.nuget.org/packages/envoice%2Fmodule-einvoice) | v1.1.1 | envoice | File LHDN MyInvois e-invoices for Malaysian Magento and Adobe Commerce stores w… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
