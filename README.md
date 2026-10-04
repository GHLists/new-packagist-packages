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

## Latest list — 2026-10-04 22:19 UTC

New packages created between 2026-10-04 21:21 UTC and 2026-10-04 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T22-19-30-134057Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 21:21:48 | [lambda-twelve/one-record-drupal](https://www.nuget.org/packages/lambda-twelve%2Fone-record-drupal) | 1.0.0-beta1 | Nick Andriopoulos | Drupal integration for lambda-twelve/one-record: wires the IATA ONE Record SDK… |
| 2026-10-04 21:23:55 | [justinholtweb/craft-twinsies](https://www.nuget.org/packages/justinholtweb%2Fcraft-twinsies) | 5.0.0 | Justin Holt | Twinfield integration for Craft Commerce — post orders as sales invoices or jou… |
| 2026-10-04 21:35:40 | [g4t/printly](https://www.nuget.org/packages/g4t%2Fprintly) | 0.0.1 | Hussein Alaa | Generate PDFs in Laravel with headless Chrome: first-class Arabic/RTL, custom f… |
| 2026-10-04 21:54:57 | [mage2kishan/module-price-drop-alert](https://www.nuget.org/packages/mage2kishan%2Fmodule-price-drop-alert) | 1.1.5 |  | Price Drop Alert module for Magento 2 - Allows customers to subscribe to price… |
| 2026-10-04 21:59:48 | [dirthara/migration](https://www.nuget.org/packages/dirthara%2Fmigration) | 0.1.0 | Dirthara | Migrations for the Dirthara framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
