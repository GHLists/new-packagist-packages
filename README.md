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

## Latest list — 2026-11-06 16:21 UTC

New packages created between 2026-11-06 15:19 UTC and 2026-11-06 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T16-21-29-315719Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 15:23:20 | [medienbaecker/kirby-og-image](https://www.nuget.org/packages/medienbaecker%2Fkirby-og-image) | 1.0.0 | Thomas Günther | Generated social media cards for Kirby |
| 2026-11-06 15:33:47 | [ee-forge/craft-recurrence](https://www.nuget.org/packages/ee-forge%2Fcraft-recurrence) | 1.0.0 | EE Forge | Recurring dates for native Craft entries, with indexed occurrences, dated URLs,… |
| 2026-11-06 15:44:21 | [lesekloden/lesekloden-screenshots](https://www.nuget.org/packages/lesekloden%2Flesekloden-screenshots) | v1.0.0 | Simen F. Kristoffersen | Capture page sections as PNG screenshots in Laravel using Browsershot. |
| 2026-11-06 15:47:22 | [lesekloden/lesekloden-qr](https://www.nuget.org/packages/lesekloden%2Flesekloden-qr) | v1.0.0 | Simen F. Kristoffersen | Generate branded PNG QR codes from configured URLs in Laravel. |
| 2026-11-06 15:55:47 | [useflex/avatars](https://www.nuget.org/packages/useflex%2Favatars) | v0.1.1 |  | Illustrated profile avatars with a lightweight, self-hosted catalogue. |
| 2026-11-06 16:02:15 | [olgunozoktas/laravel-security-check](https://www.nuget.org/packages/olgunozoktas%2Flaravel-security-check) | v0.1.0 | Olgun Özoktaş | Security checks for Laravel and Livewire apps without AI: `php artisan security… |
| 2026-11-06 16:06:08 | [glavweb/admin-bundle](https://www.nuget.org/packages/glavweb%2Fadmin-bundle) | v1.0.0 | Andrey Nilov; Glavweb Communi… | Sonata Admin extras for Glavweb projects |
| 2026-11-06 16:08:05 | [blutrixx/nativephp-alarms](https://www.nuget.org/packages/blutrixx%2Fnativephp-alarms) | v1.1.0 | Blutrixx | NativePHP Mobile plugin: reminders that fire on time with the app closed. Exact… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
