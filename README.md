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

## Latest list — 2026-10-01 17:21 UTC

New packages created between 2026-10-01 16:20 UTC and 2026-10-01 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T17-21-36-089149Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 16:21:35 | [mage2kishan/module-testimonials](https://www.nuget.org/packages/mage2kishan%2Fmodule-testimonials) | 1.2.4 |  | Advanced Testimonials module with slider, individual pages, categories, SEO, an… |
| 2026-10-01 16:24:46 | [mage2kishan/module-notification-bar](https://www.nuget.org/packages/mage2kishan%2Fmodule-notification-bar) | 1.0.13 | Kishan Savaliya | Panth Notification Bar — display customizable notification bars, promo banners,… |
| 2026-10-01 16:25:32 | [lucas-simas/wm-nfe](https://www.nuget.org/packages/lucas-simas%2Fwm-nfe) | v3.7.3 | Equipe WebmaniaBR; Lucas Simas | Fork do PHP SDK da REST API de NF-e da WebmaniaBR, com timeout configuravel |
| 2026-10-01 17:16:27 | [mage2kishan/module-mega-menu](https://www.nuget.org/packages/mage2kishan%2Fmodule-mega-menu) | 1.0.15 | Kishan Savaliya | Advanced mega menu for Magento 2 — works on Hyva and Luma. Drag-and-drop tree b… |
| 2026-10-01 17:20:30 | [mage2kishan/module-blog](https://www.nuget.org/packages/mage2kishan%2Fmodule-blog) | 1.3.4 | Kishan Savaliya | Panth_Blog - SEO-grade blog module for Magento 2 with first-class AEO/AIO suppo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
