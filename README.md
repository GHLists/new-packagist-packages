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

## Latest list — 2026-11-23 13:20 UTC

New packages created between 2026-11-23 12:21 UTC and 2026-11-23 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T13-20-41-241971Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 12:25:16 | [tomgould/rsstojson](https://www.nuget.org/packages/tomgould%2Frsstojson) | v2.1.1 | Tom Gould | Universal RSS/Atom/XML parser that outputs clean JSON-compatible arrays. |
| 2026-11-23 12:29:28 | [mirror-and-mountain/meros-email-connectors](https://www.nuget.org/packages/mirror-and-mountain%2Fmeros-email-connectors) | v0.0.1 | tmw-mm | A collection of email connectors for Meros powered WordPress themes. |
| 2026-11-23 12:31:37 | [orboni/bagisto-payment](https://www.nuget.org/packages/orboni%2Fbagisto-payment) | v1.0.0 | Orboni | Crypto payments for Bagisto through Orboni: USDT, USDC, Bitcoin, Ethereum and m… |
| 2026-11-23 12:55:44 | [philipschlender/container-php](https://www.nuget.org/packages/philipschlender%2Fcontainer-php) | 1.0.0 | Philip Schlender | Container |
| 2026-11-23 13:05:50 | [soara/laravel-debugger](https://www.nuget.org/packages/soara%2Flaravel-debugger) | v0.1.0 | Soara | Log viewer and debugging tools for Laravel apps: logs, failed jobs, scheduler,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
