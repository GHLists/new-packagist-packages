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

## Latest list — 2026-10-04 11:20 UTC

New packages created between 2026-10-04 10:21 UTC and 2026-10-04 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T11-20-54-792517Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 10:26:40 | [erpflow/erpflow-php](https://www.nuget.org/packages/erpflow%2Ferpflow-php) | v1.0.0 |  | Official PHP SDK for the ERPFlow Public API v3 |
| 2026-10-04 10:29:18 | [mage2kishan/module-producttabs](https://www.nuget.org/packages/mage2kishan%2Fmodule-producttabs) | 1.1.6 | Kishan Savaliya | Product detail page tab customization for Magento 2. Supports horizontal/vertic… |
| 2026-10-04 10:38:40 | [daedaloslabs/filament-shelly](https://www.nuget.org/packages/daedaloslabs%2Ffilament-shelly) | v1.0.0 | Michael Mavroforakis | Show live Shelly Cloud sensor stats (temperature, humidity, power, door/window,… |
| 2026-10-04 10:45:55 | [actra/yuf-skeleton](https://www.nuget.org/packages/actra%2Fyuf-skeleton) | v1.0.1 |  | A minimal "Hello World" application to start a new project with the yuf framewo… |
| 2026-10-04 11:01:50 | [mage2kishan/module-advanced-contact-us](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-contact-us) | 1.1.10 |  | Advanced Contact Us Page - Custom fields, bot protection, submission management… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
