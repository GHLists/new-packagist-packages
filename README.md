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

## Latest list — 2026-10-09 16:20 UTC

New packages created between 2026-10-09 15:23 UTC and 2026-10-09 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T16-20-57-398649Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 15:27:39 | [saola/compiler](https://www.nuget.org/packages/saola%2Fcompiler) | v1.0.2 | SaoLabs | Saola Compiler - biên dịch .sao sang Blade (SSR) và JavaScript (CSR) |
| 2026-10-09 15:27:39 | [saola/core](https://www.nuget.org/packages/saola%2Fcore) | v1.0.2 | SaoLabs Team | Saola — Laravel Core Library for building reactive full-stack applications |
| 2026-10-09 15:38:00 | [litetable/litetable](https://www.nuget.org/packages/litetable%2Flitetable) | v1.0.0 | Ortiz | Lightweight, high-performance database access for PHP using native PDO and asso… |
| 2026-10-09 15:39:28 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.4.9 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-09 15:55:39 | [verifyblind/verifyblind-php](https://www.nuget.org/packages/verifyblind%2Fverifyblind-php) | v1.0.0 |  | Server-side verification of VerifyBlind result tokens and webhooks (RSA-PSS SHA… |
| 2026-10-09 15:56:08 | [ml-solutions/nova-logs-view](https://www.nuget.org/packages/ml-solutions%2Fnova-logs-view) | v1.1.0 |  | Read-only Laravel Nova log explorer with filtering, recurring diagnostics and s… |
| 2026-10-09 16:01:25 | [coercive/ajax](https://www.nuget.org/packages/coercive%2Fajax) | 1.0.0 | Anthony Moral | Coercive Ajax |
| 2026-10-09 16:02:17 | [netresearch/nr-http-guard](https://www.nuget.org/packages/netresearch%2Fnr-http-guard) | v0.1.0 | Netresearch DTT GmbH | HTTP Guard - Controlled outbound HTTP protection for qualified TYPO3 client com… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
