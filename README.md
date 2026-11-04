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

## Latest list — 2026-11-04 04:19 UTC

New packages created between 2026-11-04 03:20 UTC and 2026-11-04 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T04-19-59-258252Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 03:38:26 | [tacraft-sociality/flarum-sign-confirm-password](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-sign-confirm-password) | 1.0.0 | Tacraft Sociality | Adds a confirm password field to the sign up modal. |
| 2026-11-04 03:47:16 | [mdestafadilah/cloudflare-d1-php](https://www.nuget.org/packages/mdestafadilah%2Fcloudflare-d1-php) | v1.0.0 | Yorman | A lightweight PHP client for Cloudflare D1 database |
| 2026-11-04 03:54:25 | [webrteu/factura](https://www.nuget.org/packages/webrteu%2Ffactura) | v0.1.0 | WeBRTeu | Laravel provider for webrteu/invoicing that issues invoices through a self-host… |
| 2026-11-04 03:59:23 | [webrteu/invoicing](https://www.nuget.org/packages/webrteu%2Finvoicing) | v2.0.0 | WeBRTeu | Invoicing core for Laravel (Romania): one API for SmartBill and other invoicing… |
| 2026-11-04 04:00:59 | [webrteu/smartbill](https://www.nuget.org/packages/webrteu%2Fsmartbill) | v2.0.0 | WeBRTeu | SmartBill provider for webrteu/invoicing (Romania) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
