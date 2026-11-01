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

## Latest list — 2026-11-01 04:20 UTC

New packages created between 2026-11-01 03:19 UTC and 2026-11-01 04:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T04-20-16-51573Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 03:31:56 | [wuwx/sm3](https://www.nuget.org/packages/wuwx%2Fsm3) | v1.0.0 | wuwx | SM3 (GB/T 32905) hash in pure PHP |
| 2026-11-01 03:37:43 | [stougeiro/base-contract](https://www.nuget.org/packages/stougeiro%2Fbase-contract) | v0.1.0 | stougeiro | Runtime-agnostic contracts and abstract bases for modular HTTP applications. |
| 2026-11-01 03:38:13 | [kipchak/driver-nats](https://www.nuget.org/packages/kipchak%2Fdriver-nats) | 1.0 |  | A NATS and JetStream driver for messaging, request/reply, durable streams and k… |
| 2026-11-01 03:55:41 | [coinvello/sdk](https://www.nuget.org/packages/coinvello%2Fsdk) | v0.1.1 | CoinVello | Official CoinVello API client for PHP (non-custodial crypto payments). No Guzzl… |
| 2026-11-01 04:12:59 | [thewonderjoy/gaze-php](https://www.nuget.org/packages/thewonderjoy%2Fgaze-php) | v1.0.0 | thewonderjoy | Framework-agnostic PHP client for Gaze, a fast debug app: gaze() helper, Ray-st… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
