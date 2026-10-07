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

## Latest list — 2026-10-07 03:21 UTC

New packages created between 2026-10-07 02:22 UTC and 2026-10-07 03:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T03-21-56-869323Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 02:25:34 | [edulazaro/laradomains](https://www.nuget.org/packages/edulazaro%2Flaradomains) | 1.1.0 | Edu Lazaro | Everything you can learn about a domain without visiting it: parsing with the P… |
| 2026-10-07 02:43:26 | [wacafla/subscriber-verify-client](https://www.nuget.org/packages/wacafla%2Fsubscriber-verify-client) | v1.0.0 |  | PHP 8 client for the documented SubscriberVerify API |
| 2026-10-07 02:46:35 | [mage2kishan/module-quickview](https://www.nuget.org/packages/mage2kishan%2Fmodule-quickview) | 1.0.21 | Kishan Savaliya | Smart Quick View & Compare module for Magento 2 with Hyva theme support. Featur… |
| 2026-10-07 03:08:17 | [spiggle/filawarden-core](https://www.nuget.org/packages/spiggle%2Ffilawarden-core) | v1.0.0 | Spiggle | Laravel Operations Intelligence Platform for Filament - Core Edition |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
