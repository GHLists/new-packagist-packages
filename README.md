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

## Latest list — 2026-10-18 08:23 UTC

New packages created between 2026-10-18 07:19 UTC and 2026-10-18 08:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T08-23-00-080382Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 07:38:15 | [tobento/service-renderable](https://www.nuget.org/packages/tobento%2Fservice-renderable) | 2.0 | Tobias Strub | Renderable service for PHP applications. |
| 2026-10-18 07:42:09 | [soml/soml](https://www.nuget.org/packages/soml%2Fsoml) | v0.0.1 | Sindre Sorhus | Read and write SOML, a config format for humans |
| 2026-10-18 07:47:24 | [jobu/json-rpc-client](https://www.nuget.org/packages/jobu%2Fjson-rpc-client) | v1.0.0 |  | Synchronous PHP client for the JobU JSON-RPC Unix socket |
| 2026-10-18 07:48:31 | [trail/storage](https://www.nuget.org/packages/trail%2Fstorage) | 0.4.0 | Alex Brindley | Storage driver addon for trail |
| 2026-10-18 07:52:47 | [trail/images](https://www.nuget.org/packages/trail%2Fimages) | 0.4.0 | Alex Brindley | Image uploads and resizing for trail |
| 2026-10-18 07:53:08 | [mrsafalpiya/strictly-laravel](https://www.nuget.org/packages/mrsafalpiya%2Fstrictly-laravel) | 0.2.0 |  | Strictly Laravel: end-to-end type safety for Laravel + Inertia + React, applied… |
| 2026-10-18 08:05:34 | [whatef/harken](https://www.nuget.org/packages/whatef%2Fharken) | v0.1.0 |  | A long-running, event-driven MQTT client runtime for Laravel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
