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

## Latest list — 2026-10-15 12:23 UTC

New packages created between 2026-10-15 11:22 UTC and 2026-10-15 12:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T12-23-02-213915Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 11:26:49 | [getkirby/rector](https://www.nuget.org/packages/getkirby%2Frector) | 1.0.0 |  | Rector rules to upgrade Kirby sites and plugins |
| 2026-10-15 11:48:18 | [amarenkov/laravel-mutable-content-tasks](https://www.nuget.org/packages/amarenkov%2Flaravel-mutable-content-tasks) | v0.1.0 | Alexey Marenkov | Task domain for laravel-mutable-content: tasks, participants and time tracking… |
| 2026-10-15 11:48:24 | [amarenkov/laravel-mutable-content-finance](https://www.nuget.org/packages/amarenkov%2Flaravel-mutable-content-finance) | v0.1.0 | Alexey Marenkov | Personal finance domain for laravel-mutable-content: accounts, operations split… |
| 2026-10-15 12:08:19 | [makaira/oxid-connect-demodata-fix](https://www.nuget.org/packages/makaira%2Foxid-connect-demodata-fix) | 1.1.0 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
