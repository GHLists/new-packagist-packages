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

## Latest list — 2026-09-29 21:19 UTC

New packages created between 2026-09-29 20:20 UTC and 2026-09-29 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T21-19-52-444025Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 20:21:14 | [hubmais/h-http-client](https://www.nuget.org/packages/hubmais%2Fh-http-client) | 1.0.0 |  | Http Client to access Api HUBMAIS |
| 2026-09-29 20:21:19 | [mage2kishan/module-cachemanager](https://www.nuget.org/packages/mage2kishan%2Fmodule-cachemanager) | 1.0.7 | Kishan Savaliya | Smart cache invalidation on entity save and automated cache warmup with concurr… |
| 2026-09-29 20:29:24 | [mage2kishan/module-checkout-extended](https://www.nuget.org/packages/mage2kishan%2Fmodule-checkout-extended) | 1.1.4 | Kishan Savaliya | Enhanced one-page checkout for Magento 2 with configurable multi-column layouts… |
| 2026-09-29 20:33:28 | [leeovery/rules-engine](https://www.nuget.org/packages/leeovery%2Frules-engine) | v1.0.0 | Lee Overy | A rules engine for Laravel that resolves values from named rule sets against fa… |
| 2026-09-29 20:36:25 | [mage2kishan/module-checkout-success](https://www.nuget.org/packages/mage2kishan%2Fmodule-checkout-success) | 1.0.8 | Kishan Savaliya | Modern, configurable checkout success page for Magento 2. Replaces the default… |
| 2026-09-29 20:45:12 | [mage2kishan/module-corewebvitals](https://www.nuget.org/packages/mage2kishan%2Fmodule-corewebvitals) | 1.0.11 | Kishan Savaliya | Real-time Core Web Vitals monitoring with LCP, FID, CLS tracking using Performa… |
| 2026-09-29 20:55:52 | [mage2kishan/module-crosslinks](https://www.nuget.org/packages/mage2kishan%2Fmodule-crosslinks) | 1.0.11 |  | Automatic internal crosslinks for Magento 2 (Hyva + Luma). Converts configured… |
| 2026-09-29 21:03:12 | [mage2kishan/module-custom-options](https://www.nuget.org/packages/mage2kishan%2Fmodule-custom-options) | 1.0.8 | Kishan Savaliya | Panth Custom Options — beautifully styled product custom options for Hyva-based… |
| 2026-09-29 21:10:11 | [afaztech/reactor](https://www.nuget.org/packages/afaztech%2Freactor) | v0.1.1 |  | Application skeleton for the Reactor PHP framework |
| 2026-09-29 21:17:51 | [mage2kishan/module-dynamic-forms](https://www.nuget.org/packages/mage2kishan%2Fmodule-dynamic-forms) | 1.1.3 |  | Dynamic Forms module for Magento 2 - Create and manage custom forms with drag-a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
