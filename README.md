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

## Latest list — 2026-10-02 21:22 UTC

New packages created between 2026-10-02 20:22 UTC and 2026-10-02 21:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T21-22-31-141244Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 20:49:42 | [milon/fuse](https://www.nuget.org/packages/milon%2Ffuse) | v1.0.0 | Nuruzzaman Milon | HTTP-client-agnostic circuit breaker with optional Laravel and Saloon adapters |
| 2026-10-02 21:13:56 | [justpush/laravel-notification-channel](https://www.nuget.org/packages/justpush%2Flaravel-notification-channel) | v1.0.0 | JustPush.io | JustPush notification channel for Laravel: send push notifications to iOS and A… |
| 2026-10-02 21:17:17 | [portabyte/php](https://www.nuget.org/packages/portabyte%2Fphp) | v0.1.0 |  | Official PHP SDK for Portabyte file infrastructure. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
