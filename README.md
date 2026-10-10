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

## Latest list — 2026-10-10 15:19 UTC

New packages created between 2026-10-10 14:22 UTC and 2026-10-10 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T15-19-44-851501Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 14:27:41 | [sewlore/measurement-calculators](https://www.nuget.org/packages/sewlore%2Fmeasurement-calculators) | v1.0.0 |  | Local fabric stretch and recovery, button-centre spacing, and length conversion… |
| 2026-10-10 14:36:33 | [burhan15/office-pack](https://www.nuget.org/packages/burhan15%2Foffice-pack) | v0.1.0 |  | Universal Office Document SDK (PHP) — first-party engines |
| 2026-10-10 14:40:42 | [astrophp/trail](https://www.nuget.org/packages/astrophp%2Ftrail) | v0.1.0 | Melih Ucar | Tracing, cost tracking, and an observability dashboard for the Laravel AI SDK. |
| 2026-10-10 14:53:45 | [pivotphp/security](https://www.nuget.org/packages/pivotphp%2Fsecurity) | v0.1.0 | Caio Alberto Fernandes | Security middlewares for PivotPHP and any PSR-15 pipeline: CORS, trusted proxie… |
| 2026-10-10 15:02:51 | [jotham-lec/statamic-penang](https://www.nuget.org/packages/jotham-lec%2Fstatamic-penang) | v1.0.0 |  |  |
| 2026-10-10 15:17:27 | [agusedyc/yii-admin](https://www.nuget.org/packages/agusedyc%2Fyii-admin) | v0.1.0 | Agus Dyc | RBAC admin panel and authorization helpers for Yii3. Non-backward-compatible po… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
