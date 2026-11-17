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

## Latest list — 2026-11-17 09:20 UTC

New packages created between 2026-11-17 08:20 UTC and 2026-11-17 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T09-20-08-66107Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 08:32:15 | [craftix/php-sms-sender](https://www.nuget.org/packages/craftix%2Fphp-sms-sender) | v1.0.0 |  | A clean and extensible PHP package for sending SMS messages through multiple pr… |
| 2026-11-17 08:36:19 | [rapidez/checkoutviabol](https://www.nuget.org/packages/rapidez%2Fcheckoutviabol) | 5.0.0 | Jade | bol.checkout payment method support for Rapidez |
| 2026-11-17 08:44:49 | [justbetter/magento2-module-checkoutviabol-graphql](https://www.nuget.org/packages/justbetter%2Fmagento2-module-checkoutviabol-graphql) | 0.1.0 | Jade Geels | GraphQL support for the bol.checkout Magento 2 module, for headless frontends |
| 2026-11-17 09:11:22 | [messenger-monitoring/messenger-monitoring](https://www.nuget.org/packages/messenger-monitoring%2Fmessenger-monitoring) | 1.0.0 |  | Symfony Messenger message lifecycle monitoring bundle |
| 2026-11-17 09:14:38 | [moonetix/datacenter-ip-ranges](https://www.nuget.org/packages/moonetix%2Fdatacenter-ip-ranges) | v1.3.0 | Moonetix | Daily cloud, hosting, CDN, Tor, iCloud Private Relay and search/AI crawler IP r… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
