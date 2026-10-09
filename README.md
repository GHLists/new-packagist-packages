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

## Latest list — 2026-10-09 19:21 UTC

New packages created between 2026-10-09 18:19 UTC and 2026-10-09 19:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T19-21-41-431871Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 18:26:39 | [camindo/cms](https://www.nuget.org/packages/camindo%2Fcms) | v9.0.0 |  | camindo CMS - multi-site, multilingual content management in PHP. Installed int… |
| 2026-10-09 18:26:39 | [camindo/project](https://www.nuget.org/packages/camindo%2Fproject) | v9.0.0 |  | camindo CMS project skeleton: composer create-project camindo/project mysite |
| 2026-10-09 18:28:56 | [iranimij/module-base](https://www.nuget.org/packages/iranimij%2Fmodule-base) | v1.0.0 | Iman Aboheydary | Tiny shared base module for Iranimij Magento 2 extensions: a config tab, an ins… |
| 2026-10-09 18:30:23 | [matgro/dify-sdk](https://www.nuget.org/packages/matgro%2Fdify-sdk) | v0.1.0 |  | PHP SDK for the Dify datasets and documents API. |
| 2026-10-09 18:41:30 | [everysize/checkout-oxid](https://www.nuget.org/packages/everysize%2Fcheckout-oxid) | 1.1.3 | everysize GmbH | everysize Checkout – Modul für OXID eShop 7 |
| 2026-10-09 18:41:42 | [hubmais/h-checkout-onboarding](https://www.nuget.org/packages/hubmais%2Fh-checkout-onboarding) | 1.0.1 |  | Plugin to onboarding for HUBMAIS |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
