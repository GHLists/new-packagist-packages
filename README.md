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

## Latest list — 2026-10-26 11:21 UTC

New packages created between 2026-10-26 10:20 UTC and 2026-10-26 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T11-21-40-088376Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 10:23:30 | [vitamin2/filament-theme](https://www.nuget.org/packages/vitamin2%2Ffilament-theme) | v1.0.0 |  | Shared Filament brand theme for vitamin2 apps |
| 2026-10-26 10:32:18 | [smspva/sdk](https://www.nuget.org/packages/smspva%2Fsdk) | v0.1.0-alpha.1 | SMSPVA | Official PHP SDK for SMSPVA SMS activation, phone number rental and private ema… |
| 2026-10-26 10:33:34 | [rasuvaeff/yii3-idempotency-redis](https://www.nuget.org/packages/rasuvaeff%2Fyii3-idempotency-redis) | v1.0.0 | Victor Razuvaev | Redis-backed idempotency storage for Yii3 APIs |
| 2026-10-26 10:35:32 | [markdoel/laravel-log-insight](https://www.nuget.org/packages/markdoel%2Flaravel-log-insight) | v1.0.0 | Markus Doell | Parse Laravel logs, cluster recurring errors and get AI-powered root cause anal… |
| 2026-10-26 11:01:10 | [vender-demo/first-project](https://www.nuget.org/packages/vender-demo%2Ffirst-project) | 1.5.0 |  | First Profile demo |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
