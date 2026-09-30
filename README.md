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

## Latest list — 2026-09-30 03:19 UTC

New packages created between 2026-09-30 02:18 UTC and 2026-09-30 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T03-19-27-244256Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 03:06:05 | [mage2kishan/module-notification-bar](https://www.nuget.org/packages/mage2kishan%2Fmodule-notification-bar) | 1.0.11 | Kishan Savaliya | Panth Notification Bar — display customizable notification bars, promo banners,… |
| 2026-09-30 03:14:24 | [mage2kishan/module-ordered-items](https://www.nuget.org/packages/mage2kishan%2Fmodule-ordered-items) | 1.0.9 | Kishan Savaliya | Panth Ordered Items — adds a rich 'Order Items' column to the Magento 2 admin S… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
