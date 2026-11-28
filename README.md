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

## Latest list — 2026-11-28 16:20 UTC

New packages created between 2026-11-28 15:22 UTC and 2026-11-28 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T16-20-55-968466Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 15:24:12 | [danilovl/phpstan-rules](https://www.nuget.org/packages/danilovl%2Fphpstan-rules) | v0.0.2 | Vladimir Danilov | Custom PHPStan rules shared by danilovl packages: no array shapes, no call chai… |
| 2026-11-28 15:26:09 | [fiberphp/tracing](https://www.nuget.org/packages/fiberphp%2Ftracing) | v0.1.0 | PangBin | 🔗 FiberPHP 链路追踪 —— 基于 Zipkin，覆盖 HTTP 与数据库查询，支持 trace_id/span_id 自动传播。 |
| 2026-11-28 15:28:04 | [anprsoftware/laravel-sdk](https://www.nuget.org/packages/anprsoftware%2Flaravel-sdk) | v1.0.0 |  | Laravel SDK for ANPR.Software — automatic number plate recognition API |
| 2026-11-28 15:36:16 | [egensolve/realtime-events](https://www.nuget.org/packages/egensolve%2Frealtime-events) | 0.2.0 |  | Realtime Events protocol validation, channel authorization and publication for… |
| 2026-11-28 15:37:48 | [clavia/authzen](https://www.nuget.org/packages/clavia%2Fauthzen) | v0.1.0 | Julien Guittard | An OpenID AuthZEN 1.0 client on PSR-18 and a PSR-15 middleware that enforces it… |
| 2026-11-28 15:38:50 | [danilovl/sqids-bundle](https://www.nuget.org/packages/danilovl%2Fsqids-bundle) | v0.0.1 | Vladimir Danilov | Symfony bundle provides integrates sqids |
| 2026-11-28 15:47:53 | [egensolve/realtime-events-laravel](https://www.nuget.org/packages/egensolve%2Frealtime-events-laravel) | 0.2.0 |  | Transactional Laravel outbox for Realtime Events. |
| 2026-11-28 15:52:21 | [webpatser/livewire-gate](https://www.nuget.org/packages/webpatser%2Flivewire-gate) | v1.0.0 | Christoph Kempen | Captcha gate for Livewire and Blade: check first, then show the form. Turnstile… |
| 2026-11-28 15:58:05 | [ernestdefoe/postcards](https://www.nuget.org/packages/ernestdefoe%2Fpostcards) | 1.0.0 | Ernest Defoe | Postcards: the discussion list as cards. The first picture or video of each dis… |
| 2026-11-28 16:07:19 | [ernestdefoe/astrolabe](https://www.nuget.org/packages/ernestdefoe%2Fastrolabe) | 1.0.0 | Ernest Defoe | Astrolabe: show the whole forum in another calendar and in native numerals. Per… |
| 2026-11-28 16:07:59 | [egensolve/cloud-sdk-http](https://www.nuget.org/packages/egensolve%2Fcloud-sdk-http) | 0.2.0 |  | Shared HTTP transport for Egensolve Cloud PHP SDKs. |
| 2026-11-28 16:08:08 | [egensolve/media](https://www.nuget.org/packages/egensolve%2Fmedia) | 0.2.0 |  | Egensolve Media Storage client for PHP |
| 2026-11-28 16:08:17 | [egensolve/artifacts](https://www.nuget.org/packages/egensolve%2Fartifacts) | 0.2.0 |  | Egensolve Artifact Storage client for PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
