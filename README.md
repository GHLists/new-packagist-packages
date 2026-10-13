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

## Latest list — 2026-10-13 15:19 UTC

New packages created between 2026-10-13 14:20 UTC and 2026-10-13 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T15-19-53-624019Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 14:20:30 | [teufels/tt3-greetingcard](https://www.nuget.org/packages/teufels%2Ftt3-greetingcard) | 1.0.1 | teufels GmbH | Greeting card service for the TYPO3 form framework with motif selection from a… |
| 2026-10-13 14:29:52 | [pantono/subscriptions](https://www.nuget.org/packages/pantono%2Fsubscriptions) | 1.0.4 | Chris Burton | Subscriptions Module for pantono |
| 2026-10-13 14:30:54 | [fiber-interop/scope](https://www.nuget.org/packages/fiber-interop%2Fscope) | v0.1.0 | Frode Børli | Scope: the identity of the operation (request, job) that code belongs to. PHP e… |
| 2026-10-13 14:30:57 | [fiber-interop/api](https://www.nuget.org/packages/fiber-interop%2Fapi) | v0.1.0 |  | One surface for fiber-based concurrency: go, await, sleep, readable, writable o… |
| 2026-10-13 14:31:01 | [fiber-interop/phasync](https://www.nuget.org/packages/fiber-interop%2Fphasync) | v0.1.0 |  | fiber-interop/api adapter for the phasync event loop. |
| 2026-10-13 14:31:04 | [fiber-interop/revolt](https://www.nuget.org/packages/fiber-interop%2Frevolt) | v0.1.0 |  | Revolt event loop adapter for fiber-interop/api: go, await, sleep, readable, wr… |
| 2026-10-13 14:31:08 | [fiber-interop/amp](https://www.nuget.org/packages/fiber-interop%2Famp) | v0.1.0 |  | Native AMPHP v3 adapter for fiber-interop/api: go() returns an Amp\Future; awai… |
| 2026-10-13 14:31:10 | [fiber-interop/react](https://www.nuget.org/packages/fiber-interop%2Freact) | v0.1.0 |  | ReactPHP adapter for fiber-interop/api: go, await, sleep, readable, writable on… |
| 2026-10-13 14:31:13 | [fiber-interop/swoole](https://www.nuget.org/packages/fiber-interop%2Fswoole) | v0.1.1 |  | Swoole coroutine adapter for fiber-interop/api: go, await, sleep, readable, wri… |
| 2026-10-13 14:43:19 | [nesto/framework](https://www.nuget.org/packages/nesto%2Fframework) | v0.1.2 | Hussein Alaa | Nesto — a PHP framework: modules, dependency injection, guards, pipes, intercep… |
| 2026-10-13 14:45:27 | [knppy/units](https://www.nuget.org/packages/knppy%2Funits) | v0.1.0 | Michael Beers | PHP library to make working with units safer, easier, and fun! |
| 2026-10-13 14:47:22 | [abdulkadiragoliya/commerce-sale-scheduler](https://www.nuget.org/packages/abdulkadiragoliya%2Fcommerce-sale-scheduler) | 1.0.0 | Abdulkadir Agoliya | Dynamic scheduled sales, category promotions, custom promotional tags, and coun… |
| 2026-10-13 14:51:37 | [vos/nativephp-live-activities-free](https://www.nuget.org/packages/vos%2Fnativephp-live-activities-free) | v1.0.1 |  | Free Live Activities and Live Updates for NativePHP Mobile, based on version 1.… |
| 2026-10-13 14:56:51 | [aimanong/laravel](https://www.nuget.org/packages/aimanong%2Flaravel) | 1.0.0 | Aimanong | Aimanong 的 Laravel 12 驱动 —— Eloquent / Blade / 路由 / 认证 / 控制台 / MCP |
| 2026-10-13 15:03:27 | [anis-ly/partners](https://www.nuget.org/packages/anis-ly%2Fpartners) | v2.0.0 | Aniscom for Technical Service… | The PHP SDK for the Anis Partner API — signed requests, verified responses, typ… |
| 2026-10-13 15:07:11 | [gatovel/mail](https://www.nuget.org/packages/gatovel%2Fmail) | v1.0.0 |  | Sistema modular e independente de envio de e-mails para aplicações PHP. |
| 2026-10-13 15:07:17 | [jacerider/neo_seo](https://www.nuget.org/packages/jacerider%2Fneo_seo) | 1.0.0 | Cyle Carlson (JaceRider) | A connected schema.org graph, head tags and on-page SEO for Neo sites. |
| 2026-10-13 15:07:40 | [rikochey/rikochey-php](https://www.nuget.org/packages/rikochey%2Frikochey-php) | 1.2.1 |  | Official PHP client for the Rikochey API: websites, forms, server-side submissi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
