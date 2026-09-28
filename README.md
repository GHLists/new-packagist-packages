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

## Latest list — 2026-09-28 09:23 UTC

New packages created between 2026-09-28 08:19 UTC and 2026-09-28 09:23 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T09-23-43-848487Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 08:41:50 | [webx-ui/module-banners](https://www.nuget.org/packages/webx-ui%2Fmodule-banners) | v0.47.0 | WebX UI | Banners for the WebX UI admin panel: a picture (and one for phones), a video, a… |
| 2026-09-28 08:55:04 | [andriichuk/laravel-billing-bluesnap](https://www.nuget.org/packages/andriichuk%2Flaravel-billing-bluesnap) | 0.2.0 | Serhii Andriichuk | Official BlueSnap driver for andriichuk/laravel-billing. |
| 2026-09-28 09:01:34 | [magna-cms/pages](https://www.nuget.org/packages/magna-cms%2Fpages) | v0.1.0-alpha |  | Rendered-frontend plugin for Magna CMS: pages, templates, menus, and the visual… |
| 2026-09-28 09:10:33 | [bytesof/craft-formable](https://www.nuget.org/packages/bytesof%2Fcraft-formable) | 1.0.0-beta.1 | Maria Viviana MUNTEANU | Commercial form builder plugin for Craft CMS 5. |
| 2026-09-28 09:12:21 | [dreamboycx/tp6-secure-middleware](https://www.nuget.org/packages/dreamboycx%2Ftp6-secure-middleware) | v1.0.0 | chenxiang | ThinkPHP6 安全中间件合集(SQL注入检测、CORS跨域、IP黑名单、接口签名) |
| 2026-09-28 09:19:27 | [andriichuk/bluesnap-php-sdk](https://www.nuget.org/packages/andriichuk%2Fbluesnap-php-sdk) | 0.1.0 | Serhii Andriichuk | A framework-agnostic PHP SDK for the BlueSnap Payment API. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
