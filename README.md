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

## Latest list — 2026-10-10 08:19 UTC

New packages created between 2026-10-10 07:18 UTC and 2026-10-10 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T08-19-20-066463Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 07:39:05 | [the14thsky/filament-sidebar-coscroll](https://www.nuget.org/packages/the14thsky%2Ffilament-sidebar-coscroll) | v1.0.0 | the14thsky | Makes the Filament panel sidebar scroll together with the page |
| 2026-10-10 08:02:08 | [hyperf-apex/apex](https://www.nuget.org/packages/hyperf-apex%2Fapex) | v1.0.0 | lbg-sys | Apex generic infrastructure, API engine and components for Hyperf (Metapackage) |
| 2026-10-10 08:06:50 | [online-efd/online-efd](https://www.nuget.org/packages/online-efd%2Fonline-efd) | v0.0.2 |  | Reusable Laravel package for TRA (Tanzania) VFD/EFD integration: per-tenant cer… |
| 2026-10-10 08:11:12 | [hyperf-apex/metrics](https://www.nuget.org/packages/hyperf-apex%2Fmetrics) | v1.0.0 | lbg-sys | Apex Prometheus metrics and monitoring on Swoole Table for Hyperf |
| 2026-10-10 08:11:12 | [hyperf-apex/websocket](https://www.nuget.org/packages/hyperf-apex%2Fwebsocket) | v1.0.0 | lbg-sys | Apex WebSocket gateway and push service for Hyperf |
| 2026-10-10 08:11:13 | [hyperf-apex/apidoc](https://www.nuget.org/packages/hyperf-apex%2Fapidoc) | v1.0.0 | lbg-sys | Apex OpenAPI 3.1 & Apifox documentation generator for Hyperf |
| 2026-10-10 08:11:13 | [hyperf-apex/core](https://www.nuget.org/packages/hyperf-apex%2Fcore) | v1.0.0 | lbg-sys | Apex generic infrastructure foundation, HTTP engine and security for Hyperf |
| 2026-10-10 08:11:13 | [hyperf-apex/reliability](https://www.nuget.org/packages/hyperf-apex%2Freliability) | v1.0.0 | lbg-sys | Apex reliability suite (RateLimit, Idempotency, Outbox, Notify, Outbound) for H… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
