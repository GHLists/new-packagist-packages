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

## Latest list — 2026-10-10 13:19 UTC

New packages created between 2026-10-10 12:19 UTC and 2026-10-10 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T13-19-28-675373Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 12:23:18 | [roadrunner/goridge](https://www.nuget.org/packages/roadrunner%2Fgoridge) | 4.5.0 | Anton Titov; Valery Piashchyn… | High-performance PHP-to-Go IPC bridge: the RPC transport between PHP workers an… |
| 2026-10-10 12:26:21 | [esanj/discount-client](https://www.nuget.org/packages/esanj%2Fdiscount-client) | v1.0.0 | Esanj | Laravel client package for the Esanj Discount Microservice (coupons & gift card… |
| 2026-10-10 12:35:30 | [trk/sulu-block-suite-bundle](https://www.nuget.org/packages/trk%2Fsulu-block-suite-bundle) | v1.0.0 | Iskender TOTOGLU | Component block props, visual presets, reusable global blocks, and template lay… |
| 2026-10-10 12:40:38 | [kmerhosting/sdk](https://www.nuget.org/packages/kmerhosting%2Fsdk) | v0.3.1 |  | Official PHP SDK for the KmerHosting API. |
| 2026-10-10 12:47:42 | [roadrunner/api-dto](https://www.nuget.org/packages/roadrunner%2Fapi-dto) | v2.1.0 | Pavel Buchnev; Aleksei Gagari… | Pre-generated PHP DTOs for the RoadRunner API protocol buffers, used to make RP… |
| 2026-10-10 12:47:53 | [davidewastaken/packer](https://www.nuget.org/packages/davidewastaken%2Fpacker) | v0.5.0 |  | Fast 3D cuboid packing with a bundled native engine: boxes, stock, weight, rota… |
| 2026-10-10 12:50:10 | [amarenkov/laravel-mutable-content-daisyui](https://www.nuget.org/packages/amarenkov%2Flaravel-mutable-content-daisyui) | v0.1.0 | Alexey Marenkov | Server-rendered Blade, Livewire and daisyUI screens for laravel-mutable-content… |
| 2026-10-10 12:53:13 | [roadrunner/worker](https://www.nuget.org/packages/roadrunner%2Fworker) | v3.8.0 | Anton Titov; Valery Piashchyn… | Base PHP worker for the RoadRunner application server: receives payloads over G… |
| 2026-10-10 12:59:57 | [roadrunner/http](https://www.nuget.org/packages/roadrunner%2Fhttp) | v4.2.0 | Anton Titov; Valery Piashchyn… | PSR-7 HTTP worker for the RoadRunner application server |
| 2026-10-10 13:00:11 | [sirius/ui](https://www.nuget.org/packages/sirius%2Fui) | v0.1.0 | Sirius: Code; Fathul Husnan | Reusable Laravel Blade and Livewire UI components styled with Tailwind CSS. |
| 2026-10-10 13:02:42 | [roadrunner/metrics](https://www.nuget.org/packages/roadrunner%2Fmetrics) | 3.4.0 | Anton Titov; Pavel Buchnev; A… | Prometheus metrics for PHP workers: declare and update metrics in the RoadRunne… |
| 2026-10-10 13:06:10 | [roadrunner/app-logger](https://www.nuget.org/packages/roadrunner%2Fapp-logger) | 1.3.0 | Kirill Astakhov; RoadRunner C… | Send log messages from PHP workers to the RoadRunner app logger plugin over RPC |
| 2026-10-10 13:07:13 | [roadrunner/version-checker](https://www.nuget.org/packages/roadrunner%2Fversion-checker) | v1.4.0 | Maksim Smakouz; Aleksei Gagar… | Checks that the installed RoadRunner binary matches the version required by the… |
| 2026-10-10 13:13:51 | [roadrunner/services](https://www.nuget.org/packages/roadrunner%2Fservices) | 2.4.0 | Pavel Buchnev; Aleksei Gagari… | Manage RoadRunner services from PHP: create, start, stop and inspect processes… |
| 2026-10-10 13:16:11 | [roadrunner/kv](https://www.nuget.org/packages/roadrunner%2Fkv) | v4.5.0 | Anton Titov; Pavel Buchnev; A… | PSR-16 cache on top of the RoadRunner Key-Value plugin storages (memory, boltdb… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
