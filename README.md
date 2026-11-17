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

## Latest list — 2026-11-17 18:22 UTC

New packages created between 2026-11-17 17:22 UTC and 2026-11-17 18:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T18-22-04-3495Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 17:35:08 | [msads/agent-sdk-php](https://www.nuget.org/packages/msads%2Fagent-sdk-php) | v0.1.0 | MS TECH IT PRIVATE LIMITED | MS Ads Agent Exchange server SDK (offers, events, HMAC request signing) |
| 2026-11-17 17:44:13 | [pimoudeveldhuis/nova-component-select-database-field](https://www.nuget.org/packages/pimoudeveldhuis%2Fnova-component-select-database-field) | v1.0.1 |  | A Laravel Nova field for editing ordered arrays with selectable options. |
| 2026-11-17 17:50:27 | [teme/contracts](https://www.nuget.org/packages/teme%2Fcontracts) | v1.0.0 |  | Public extension contracts. Semver'd independently of the application. |
| 2026-11-17 17:54:20 | [labyrinthe/labpay-laravel](https://www.nuget.org/packages/labyrinthe%2Flabpay-laravel) | v0.1.0 | Labyrinthe Innovations SARL | Laravel integration of LabPay (Mobile Money across Africa): client, facade, pub… |
| 2026-11-17 17:54:26 | [labyrinthe/labpay-php](https://www.nuget.org/packages/labyrinthe%2Flabpay-php) | v0.1.0 | Labyrinthe Innovations SARL | Official PHP SDK for LabPay: collect and send Mobile Money (M-Pesa, Airtel Mone… |
| 2026-11-17 17:58:07 | [tornado-engine/uploads](https://www.nuget.org/packages/tornado-engine%2Fuploads) | v0.1.0 |  | Tornado Engine core-module: upload files, and give Claude filtered copies (text… |
| 2026-11-17 18:11:10 | [webksde/drowl_upsi](https://www.nuget.org/packages/webksde%2Fdrowl_upsi) | 0.0.1 | webks GmbH | Supports the DROWL Drupal Updateservice: Drush-driven start/finish workflow wit… |
| 2026-11-17 18:14:11 | [tg666/messenger](https://www.nuget.org/packages/tg666%2Fmessenger) | v0.4.0 | Milan Felix Šulc | Fork of contributte/messenger: Symfony Messenger for Nette framework, with hand… |
| 2026-11-17 18:16:25 | [adachsoft/model-pricing-lib](https://www.nuget.org/packages/adachsoft%2Fmodel-pricing-lib) | v0.1.0 |  | Versioned JSON price sheet catalog and BCMath cost estimator implementing adach… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
