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

## Latest list — 2026-11-27 18:21 UTC

New packages created between 2026-11-27 17:19 UTC and 2026-11-27 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T18-21-18-92646Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 17:41:09 | [kfriars/filament-pulse-widgets](https://www.nuget.org/packages/kfriars%2Ffilament-pulse-widgets) | v1.0.0 | Kurt Friars | Laravel Pulse cards as Filament v5 widgets, alongside your panel's own widgets. |
| 2026-11-27 17:46:30 | [membergate/membergate-api](https://www.nuget.org/packages/membergate%2Fmembergate-api) | v1.0.0 | Membergate Limited | Client for the Membergate API: signed requests, every API method, hosted sign-i… |
| 2026-11-27 17:46:52 | [kariricode/websocket](https://www.nuget.org/packages/kariricode%2Fwebsocket) | v4.0.0 | Walmir Silva | RFC 6455 WebSocket server for PHP 8.4: strict frame parsing and handshake, clos… |
| 2026-11-27 17:47:50 | [mscode-pl/vocative](https://www.nuget.org/packages/mscode-pl%2Fvocative) | v0.1.0 | Mateusz Sikorski | Address people by first name in their language: vocative case, gender and salut… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
