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

## Latest list — 2026-11-23 00:18 UTC

New packages created between 2026-11-22 23:21 UTC and 2026-11-23 00:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T00-18-47-963811Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 00:01:00 | [zunix/notification-lab](https://www.nuget.org/packages/zunix%2Fnotification-lab) | v0.1.0 |  | Test Firebase Cloud Messaging in your browser and inspect Laravel database noti… |
| 2026-11-23 00:06:22 | [orboni/craft-commerce-orboni](https://www.nuget.org/packages/orboni%2Fcraft-commerce-orboni) | 1.0.0 | Orboni | Crypto payments for Craft Commerce: USDT, USDC, Bitcoin and more, paid straight… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
