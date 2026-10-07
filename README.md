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

## Latest list — 2026-10-07 16:23 UTC

New packages created between 2026-10-07 15:19 UTC and 2026-10-07 16:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T16-23-18-48853Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 15:21:20 | [ramir1/laravel-planner](https://www.nuget.org/packages/ramir1%2Flaravel-planner) | v0.1.0 | Vadim Trofimov | Database-backed planner of one-off deferred tasks for Laravel: schedule a task… |
| 2026-10-07 15:26:26 | [wexample/symfony-dev-ds](https://www.nuget.org/packages/wexample%2Fsymfony-dev-ds) | 2.0.0 | weeger | Design-system side of symfony-dev: the development menu entry reloading the dem… |
| 2026-10-07 15:28:48 | [alphabalex/payment-made-easy](https://www.nuget.org/packages/alphabalex%2Fpayment-made-easy) | v1.0.0 | Balogun Abdulquddus | A Laravel package for handling payments with multiple gateways (Paystack, Flutt… |
| 2026-10-07 15:46:20 | [skeeks/cms-mobile](https://www.nuget.org/packages/skeeks%2Fcms-mobile) | 0.1.1 |  | Интеграция SkeekS CMS с мобильными приложениями: устройства и push-уведомления |
| 2026-10-07 15:50:09 | [wasil/integrations](https://www.nuget.org/packages/wasil%2Fintegrations) | 0.1.0 |  | Server-side PHP SDK for Wasil delivery integrations |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
