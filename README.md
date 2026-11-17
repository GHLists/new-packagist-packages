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

## Latest list — 2026-11-17 20:20 UTC

New packages created between 2026-11-17 19:22 UTC and 2026-11-17 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T20-20-24-0497Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 19:32:27 | [backdrop-dev/template-helpers](https://www.nuget.org/packages/backdrop-dev%2Ftemplate-helpers) | v1.0.1 | Benjamin Lu | Backdrop Template Helpers is set a helper functions for setting the path, locat… |
| 2026-11-17 19:42:19 | [backdrop-dev/tools](https://www.nuget.org/packages/backdrop-dev%2Ftools) | v1.0.0 | Benjamin Lu | Backdrop Tools is a collection of helper classes and functions for developing t… |
| 2026-11-17 19:49:28 | [backdrop-dev/template-hierarchy](https://www.nuget.org/packages/backdrop-dev%2Ftemplate-hierarchy) | v1.0.0 | Benjamin Lu | A smarter and flexible template hierarchy. |
| 2026-11-17 19:50:10 | [jeffersongoncalves/filament-ccpa](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-ccpa) | 2.0.0 |  |  |
| 2026-11-17 19:51:55 | [jeffersongoncalves/filament-ccpa-opt-out](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-ccpa-opt-out) | 2.0.0 |  |  |
| 2026-11-17 19:53:38 | [jeffersongoncalves/filament-ccpa-requests](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-ccpa-requests) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-ccpa-requests: handle CCPA consumer requests to kno… |
| 2026-11-17 19:55:12 | [jeffersongoncalves/filament-ccpa-retention](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-ccpa-retention) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-ccpa-retention: CCPA retention run from your panel:… |
| 2026-11-17 19:56:46 | [jeffersongoncalves/filament-ccpa-audit-log](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-ccpa-audit-log) | 1.0.0 |  |  |
| 2026-11-17 19:58:24 | [jeffersongoncalves/filament-ccpa-notices](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-ccpa-notices) | 2.0.0 |  |  |
| 2026-11-17 20:00:00 | [jeffersongoncalves/filament-ccpa-vendors](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-ccpa-vendors) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-ccpa-vendors: your CCPA service providers, contract… |
| 2026-11-17 20:01:17 | [tencentcloud/makers](https://www.nuget.org/packages/tencentcloud%2Fmakers) | 3.0.1701 | tencentcloudapi | TencentCloudApi php sdk makers |
| 2026-11-17 20:01:37 | [jeffersongoncalves/filament-ccpa-risk-assessments](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-ccpa-risk-assessments) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-ccpa-risk-assessments: CCPA risk assessments in you… |
| 2026-11-17 20:03:14 | [jeffersongoncalves/filament-ccpa-breaches](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-ccpa-breaches) | 2.0.0 |  |  |
| 2026-11-17 20:04:52 | [jeffersongoncalves/filament-ccpa-minors](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-ccpa-minors) | 1.0.0 |  |  |
| 2026-11-17 20:14:25 | [backdrop-dev/pagination](https://www.nuget.org/packages/backdrop-dev%2Fpagination) | v1.0.0 | Benjamin Lu | Enhanced pagination add-on for the Backdrop framework. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
