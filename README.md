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

## Latest list — 2026-10-20 12:19 UTC

New packages created between 2026-10-20 11:22 UTC and 2026-10-20 12:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T12-19-39-296491Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 11:30:51 | [shipaurora/cms](https://www.nuget.org/packages/shipaurora%2Fcms) | v1.0.2 | Thomas Alrek | Aurora: a content management system for Laravel, built on Filament. |
| 2026-10-20 11:35:45 | [packstub/filament-nitpick](https://www.nuget.org/packages/packstub%2Ffilament-nitpick) | v1.0.0-beta.1 | Ion Caliman; Packstub | Themes for Filament panels: designed looks with a per-panel default, an open re… |
| 2026-10-20 11:37:13 | [epay/magento2-epic-payment-hyva-checkout](https://www.nuget.org/packages/epay%2Fmagento2-epic-payment-hyva-checkout) | 1.0.2 | ePay Payment Solutions A/S | Hyvä Checkout compatibility module for ePay EPIC Payment for Magento 2 |
| 2026-10-20 11:42:32 | [oluwatimilehin/spotify-music-api](https://www.nuget.org/packages/oluwatimilehin%2Fspotify-music-api) | v1.0.0 | Tawose Oluwatimilehin | A PHP SDK wrapper for the Spotify Web API |
| 2026-10-20 11:49:39 | [shipaurora/aurora](https://www.nuget.org/packages/shipaurora%2Faurora) | v1.0.2 |  | A new website on Aurora CMS: a Laravel app with the CMS installed, ready to mak… |
| 2026-10-20 12:09:29 | [beaverphp/skeleton](https://www.nuget.org/packages/beaverphp%2Fskeleton) | v0.1.2 |  | Esqueleto de projecto limpo para o Beaver Framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
