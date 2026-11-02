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

## Latest list — 2026-11-02 12:21 UTC

New packages created between 2026-11-02 11:19 UTC and 2026-11-02 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T12-21-17-325537Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 11:19:37 | [filaforge-studio/filaforge-studio](https://www.nuget.org/packages/filaforge-studio%2Ffilaforge-studio) | v0.1.0 |  | RTL-first visual page builder for Filament 5 |
| 2026-11-02 11:49:07 | [solophp/rate-limiter](https://www.nuget.org/packages/solophp%2Frate-limiter) | v1.0.0 | Vitaliy Olos | Atomic per-key rate limits for PHP: fixed or renewable windows in Redis, with a… |
| 2026-11-02 11:50:07 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.4.0 |  | The skeleton application for the Laravel framework. |
| 2026-11-02 12:07:54 | [kirbydesk/kirby-workflow](https://www.nuget.org/packages/kirbydesk%2Fkirby-workflow) | 0.1.0 | Christian Fickinger | Publish content from Staging to the live website, right from the Panel – and mo… |
| 2026-11-02 12:12:09 | [adachsoft/code-graph-contract](https://www.nuget.org/packages/adachsoft%2Fcode-graph-contract) | v0.1.0 | Arkadiusz Adach | Typed graph models and serialization contracts for representing source-code str… |
| 2026-11-02 12:14:59 | [adamb/user](https://www.nuget.org/packages/adamb%2Fuser) | 1.4.2 | Adam Binnersley | A user class |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
