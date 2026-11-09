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

## Latest list — 2026-11-09 12:18 UTC

New packages created between 2026-11-09 11:20 UTC and 2026-11-09 12:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T12-18-29-926469Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 11:25:50 | [checkslip/sdk](https://www.nuget.org/packages/checkslip%2Fsdk) | v0.1.0 | Checkslip | Official PHP SDK for the Checkslip API: look up Thai bank transfers from a slip… |
| 2026-11-09 11:39:03 | [varypilot/sdk-php](https://www.nuget.org/packages/varypilot%2Fsdk-php) | v0.1.0 |  | Varypilot PHP 7.0+ SDK: local assignment, persistent configuration cache and co… |
| 2026-11-09 11:43:32 | [shoplygg/shoply-php](https://www.nuget.org/packages/shoplygg%2Fshoply-php) | v0.10.0 |  | Shoply's API from your own server: every route as a method, safe retries, pages… |
| 2026-11-09 11:49:45 | [ssmiff/mezzio-authentication-tokens](https://www.nuget.org/packages/ssmiff%2Fmezzio-authentication-tokens) | v0.1.0 | Scott Smith | Personal access token authentication for Mezzio APIs: a mezzio-authentication a… |
| 2026-11-09 12:09:33 | [yet-another-pim/yap](https://www.nuget.org/packages/yet-another-pim%2Fyap) | 0.8.0 | Stephan Altmann | Yet Another PIM - Manage structured product data, multilingual content, and pro… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
