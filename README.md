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

## Latest list — 2026-10-21 09:19 UTC

New packages created between 2026-10-21 08:21 UTC and 2026-10-21 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T09-19-27-859279Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 08:25:14 | [wearejust/statamic-form-submission-retention](https://www.nuget.org/packages/wearejust%2Fstatamic-form-submission-retention) | 1.0.0 |  | Configurable retention and cleanup for Statamic form submissions. |
| 2026-10-21 08:26:39 | [the-firehub-project/foundation](https://www.nuget.org/packages/the-firehub-project%2Ffoundation) | v0.1.0 | Danijel Galić | A high-level foundation layer of the FireHub ecosystem, built on top of Runtime… |
| 2026-10-21 08:29:38 | [amjadiqbal/refresher](https://www.nuget.org/packages/amjadiqbal%2Frefresher) | v1.1.0 | Amjad Iqbal | Faster Laravel tests: a drop-in for RefreshDatabase that caches the migrated (a… |
| 2026-10-21 08:34:27 | [the-firehub-project/module](https://www.nuget.org/packages/the-firehub-project%2Fmodule) | v0.1.0 | Danijel Galić | Modular application composition and lifecycle integration for The FireHub Proje… |
| 2026-10-21 08:44:09 | [the-firehub-project/kernel](https://www.nuget.org/packages/the-firehub-project%2Fkernel) | v0.1.0 | Danijel Galić | Application kernel providing bootstrap orchestration, lifecycle management, and… |
| 2026-10-21 08:51:56 | [claudiodekker/laravel-guardrails](https://www.nuget.org/packages/claudiodekker%2Flaravel-guardrails) | v1.0.0 | Claudio Dekker | Deterministic repository checks for Laravel apps, run by a pre-commit hook and… |
| 2026-10-21 08:56:32 | [the-firehub-project/container](https://www.nuget.org/packages/the-firehub-project%2Fcontainer) | v0.1.0 | Danijel Galić | A modular dependency injection container for The FireHub Project, providing ser… |
| 2026-10-21 09:10:13 | [solophp/repository](https://www.nuget.org/packages/solophp%2Frepository) | v1.0.0-RC1 | Vitaliy Olos | Typed PHP repositories with consistent translation fallback and batch-loaded re… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
