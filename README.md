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

## Latest list — 2026-10-21 08:21 UTC

New packages created between 2026-10-21 07:20 UTC and 2026-10-21 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T08-21-45-96532Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 07:34:48 | [abdulkadiragoliya/spin-to-win](https://www.nuget.org/packages/abdulkadiragoliya%2Fspin-to-win) | 1.0.1 | Abdulkadir Agoliya | Gamified Spin to Win prize wheel and promotional coupon system for Craft CMS an… |
| 2026-10-21 07:40:01 | [amjadiqbal/laravel-ninja-keys](https://www.nuget.org/packages/amjadiqbal%2Flaravel-ninja-keys) | v1.0.0 | Amjad Iqbal | Cmd+K command palette for Laravel: build ninja-keys actions in PHP, filter them… |
| 2026-10-21 07:40:02 | [amjadiqbal/laravel-sonner](https://www.nuget.org/packages/amjadiqbal%2Flaravel-sonner) | v1.0.0 | Amjad Iqbal | Sonner toast notifications for Laravel without React: flash toasts from PHP wit… |
| 2026-10-21 07:46:53 | [amjadiqbal/laravel-sweetalert2](https://www.nuget.org/packages/amjadiqbal%2Flaravel-sweetalert2) | v1.0.0 | Amjad Iqbal | SweetAlert2 for Laravel: flash success, error and toast popups from controllers… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
