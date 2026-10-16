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

## Latest list — 2026-10-16 07:20 UTC

New packages created between 2026-10-16 06:22 UTC and 2026-10-16 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T07-20-02-264806Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 06:27:29 | [prantiksoft/laravel-mfs-sms-gateway](https://www.nuget.org/packages/prantiksoft%2Flaravel-mfs-sms-gateway) | v1.0.0 | PRANTIK-SOFT | Automated Bangladeshi MFS (bKash, Nagad, Rocket) SMS Forwarding Payment Gateway… |
| 2026-10-16 06:37:09 | [webwerkwien/contao-consho-licensecheck-bundle](https://www.nuget.org/packages/webwerkwien%2Fcontao-consho-licensecheck-bundle) | v0.1.0 | Michael Morgenbesser | Consho licence check - checks signed licence keys and daily confirmations in th… |
| 2026-10-16 06:39:17 | [webwerkwien/contao-consho-bundle](https://www.nuget.org/packages/webwerkwien%2Fcontao-consho-bundle) | v0.1.0 | Michael Morgenbesser | Consho - E-commerce for Contao. Multi-shop, API-first, built for EU compliance. |
| 2026-10-16 06:42:42 | [nowo-tech/chat-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fchat-kit-bundle) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Floating LinkedIn-style chat for Symfony: direct messages, channels and a suppo… |
| 2026-10-16 07:13:20 | [qiangvei/magento2-theme-amazon](https://www.nuget.org/packages/qiangvei%2Fmagento2-theme-amazon) | 1.0.0 |  | Amazon style theme for Magento 2.4 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
