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

## Latest list — 2026-10-14 10:21 UTC

New packages created between 2026-10-14 09:22 UTC and 2026-10-14 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T10-21-18-226313Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 09:34:47 | [wexample/symfony-organization](https://www.nuget.org/packages/wexample%2Fsymfony-organization) | 1.0.1 |  |  |
| 2026-10-14 09:41:09 | [caiyun/micro](https://www.nuget.org/packages/caiyun%2Fmicro) | v1.0.0 | 刘骏霖 | Laravel microservice toolkit with pluggable service discovery and registration… |
| 2026-10-14 09:52:17 | [artisan-build/reel-client](https://www.nuget.org/packages/artisan-build%2Freel-client) | v0.1.0 |  | Laravel client for customer-owned Reel session replay. |
| 2026-10-14 09:56:33 | [wexample/symfony-organization-ds](https://www.nuget.org/packages/wexample%2Fsymfony-organization-ds) | 1.0.1 |  |  |
| 2026-10-14 10:02:00 | [ntzrbtr/captainhook-phpstan](https://www.nuget.org/packages/ntzrbtr%2Fcaptainhook-phpstan) | v1.0.0 | Thomas Off | CaptainHook action that runs PHPStan on staged files covered by the project's P… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
