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

## Latest list — 2026-10-03 06:19 UTC

New packages created between 2026-10-03 05:19 UTC and 2026-10-03 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T06-19-25-269255Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 05:32:48 | [asignua/filament-activity-log-plus](https://www.nuget.org/packages/asignua%2Ffilament-activity-log-plus) | v1.0.1 | Mykhailo Hladchenko | An audit trail for Filament 5 on top of spatie/laravel-activitylog 5: per-langu… |
| 2026-10-03 05:39:22 | [mage2kishan/module-notification-bar](https://www.nuget.org/packages/mage2kishan%2Fmodule-notification-bar) | 1.0.16 | Kishan Savaliya | Panth Notification Bar — display customizable notification bars, promo banners,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
