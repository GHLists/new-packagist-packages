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

## Latest list — 2026-11-13 20:23 UTC

New packages created between 2026-11-13 19:21 UTC and 2026-11-13 20:23 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T20-23-14-973322Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 19:29:44 | [ernestdefoe/corkboard](https://www.nuget.org/packages/ernestdefoe%2Fcorkboard) | 1.0.0 | Ernest Defoe | Corkboard: project boards inside your Flarum forum. Columns and cards with chec… |
| 2026-11-13 19:32:46 | [videovv/ini-file](https://www.nuget.org/packages/videovv%2Fini-file) | v1.0.0 |  | A simple, modern INI parser for PHP 8.0+ with support for complex strings. |
| 2026-11-13 19:33:23 | [handcode/yii2-route-access-check](https://www.nuget.org/packages/handcode%2Fyii2-route-access-check) | 1.0.0 | Jens Giessmann |  |
| 2026-11-13 19:35:00 | [ernestdefoe/broadsheet](https://www.nuget.org/packages/ernestdefoe%2Fbroadsheet) | 1.0.0 | Ernestdefoe | Broadsheet — a newspaper front-page theme for Flarum 2. A nameplate, a section… |
| 2026-11-13 19:41:21 | [ernestdefoe/studio](https://www.nuget.org/packages/ernestdefoe%2Fstudio) | 1.0.0 | Ernestdefoe | Studio — an image-first masonry theme for Flarum 2, for photo, art and maker co… |
| 2026-11-13 19:42:47 | [quire/analytics](https://www.nuget.org/packages/quire%2Fanalytics) | v0.3.0 | YorvoLabs | Analytics for Quire: Google Analytics 4, loaded only once visitors allow it, an… |
| 2026-11-13 19:42:47 | [quire/privacy](https://www.nuget.org/packages/quire%2Fprivacy) | v0.3.0 | YorvoLabs | Privacy and cookies for Quire: the services a site uses that visitors are asked… |
| 2026-11-13 19:51:14 | [youvision/think-store-example](https://www.nuget.org/packages/youvision%2Fthink-store-example) | v1.6 | indiboy-create; AI | ThinkPHP 8 示例包：包内视图渲染、layui 静态资源路由与随机抽诗接口。 |
| 2026-11-13 19:54:51 | [ernestdefoe/panels](https://www.nuget.org/packages/ernestdefoe%2Fpanels) | 1.0.0 | Ernest Defoe | Panels: a manga, webtoon and comics library and reader for Flarum 2. Series wit… |
| 2026-11-13 19:55:22 | [handcode/yii2-active-record-typecast-behavior](https://www.nuget.org/packages/handcode%2Fyii2-active-record-typecast-behavior) | 1.0.0 | Jens Giessmann | TypeCast Behavior for yii2 ActiveRecords which can be used to ensure attribute… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
