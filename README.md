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

## Latest list — 2026-10-29 09:21 UTC

New packages created between 2026-10-29 08:21 UTC and 2026-10-29 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T09-21-49-9104Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 08:22:48 | [darvis/laravel-api-key-alert](https://www.nuget.org/packages/darvis%2Flaravel-api-key-alert) | v1.1.0 | Arvid de Jong | Get an email the moment an API key stops working in Laravel: detects rejected k… |
| 2026-10-29 08:28:51 | [ajangsupardi/zkteco-laravel](https://www.nuget.org/packages/ajangsupardi%2Fzkteco-laravel) | v1.0.0 | ᑎᗩᒍ | Laravel package for ZKTeco biometric attendance device integration via TCP 4370 |
| 2026-10-29 08:29:04 | [avonez-tech/avonez-auth-client](https://www.nuget.org/packages/avonez-tech%2Favonez-auth-client) | v1.0.0 | AvonezTech | Package to connect to avonez account |
| 2026-10-29 08:38:04 | [jeremy379/laravel-storage-cli](https://www.nuget.org/packages/jeremy379%2Flaravel-storage-cli) | v1.0.0 |  | Read-only Artisan commands to explore Laravel filesystem disks, inspect files,… |
| 2026-10-29 08:44:40 | [hibira-io/filament](https://www.nuget.org/packages/hibira-io%2Ffilament) | v0.1.0 | Hibira | Live database notifications, an Echo connection light and a live channels widge… |
| 2026-10-29 08:48:05 | [magepow/preview](https://www.nuget.org/packages/magepow%2Fpreview) | 1.0.0 | Magepow | You quick access product fontend from admin. |
| 2026-10-29 08:48:35 | [nightdust/common](https://www.nuget.org/packages/nightdust%2Fcommon) | v1.0.0 |  | Reusable PHP utilities. |
| 2026-10-29 08:52:34 | [mmrtonmoybd/omnipay-sslcommerz](https://www.nuget.org/packages/mmrtonmoybd%2Fomnipay-sslcommerz) | v1.0.0 | Moshiur Rahman; Omnipay SSLCo… | SSLCommerz gateway for the Omnipay PHP payment processing library |
| 2026-10-29 08:54:40 | [peopleinside/festive-decorations](https://www.nuget.org/packages/peopleinside%2Ffestive-decorations) | 1.0.2 | PeopleInside | Decorazioni festive e stagionali per Flarum (titoli, logo, menù, festone, neve,… |
| 2026-10-29 09:12:09 | [daycry/doctrine-codeigniter4](https://www.nuget.org/packages/daycry%2Fdoctrine-codeigniter4) | v6.0.0 |  | CodeIgniter 4 adapter for daycry/doctrine |
| 2026-10-29 09:14:30 | [magepow/animationimage](https://www.nuget.org/packages/magepow%2Fanimationimage) | 1.0.0 | Magepow | Keep GIF animation working on Magento 2 frontend product images. |
| 2026-10-29 09:14:43 | [wpelevator/xhprof](https://www.nuget.org/packages/wpelevator%2Fxhprof) | v2.3.11 |  | XHProf: A Hierarchical Profiler for PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
