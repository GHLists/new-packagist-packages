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

## Latest list — 2026-11-12 11:21 UTC

New packages created between 2026-11-12 10:21 UTC and 2026-11-12 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T11-21-11-070327Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 10:23:22 | [concept24/omnipay-ingwebpay](https://www.nuget.org/packages/concept24%2Fomnipay-ingwebpay) | v1.0.2 | Concept24 | ING WebPay (ING Bank România) driver for the Omnipay payment processing library |
| 2026-11-12 10:40:48 | [codeconjure/sylius-carrier-bundle](https://www.nuget.org/packages/codeconjure%2Fsylius-carrier-bundle) | 0.1.1 |  | Szállító-semleges Sylius-alap a szállító-pluginokhoz (FoxPost, GLS, Packeta): k… |
| 2026-11-12 10:55:06 | [solvebeam/twinfield-connect](https://www.nuget.org/packages/solvebeam%2Ftwinfield-connect) | v0.1.1 | SolveBeam; Remco Tolsma | Log in to Twinfield through Twinfield Connect, without a Twinfield client ID of… |
| 2026-11-12 11:11:13 | [balatd/kern-ux](https://www.nuget.org/packages/balatd%2Fkern-ux) | 1.0.0-beta.4 | Dragan Balatinac | KERN UX-Standard for TYPO3 - accessible Fluid components, Content Blocks and fo… |
| 2026-11-12 11:11:44 | [jaryan-host/proxmox](https://www.nuget.org/packages/jaryan-host%2Fproxmox) | v1.0.1 | Nima Asaadi | A Laravel package for integrating with the Proxmox REST API. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
