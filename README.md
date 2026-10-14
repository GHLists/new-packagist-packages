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

## Latest list — 2026-10-14 14:23 UTC

New packages created between 2026-10-14 13:21 UTC and 2026-10-14 14:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T14-23-30-677765Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 13:50:30 | [x-laravel/username](https://www.nuget.org/packages/x-laravel%2Fusername) | v1.0.0 | Mehmet ÖĞMEN | Configurable username validation, reserved-name checking and username generatio… |
| 2026-10-14 13:54:16 | [arout/rhapsody-app](https://www.nuget.org/packages/arout%2Frhapsody-app) | v1.0.0 | Andrew Rout | The skeleton application for the Rhapsody Framework |
| 2026-10-14 13:55:05 | [kitaris/environment-indicator](https://www.nuget.org/packages/kitaris%2Fenvironment-indicator) | v1.0.0 | Kitaris | Shows which environment a WordPress site is running as (local, development, sta… |
| 2026-10-14 14:13:03 | [mikhailmelnikov/laravel-jobs-monitor](https://www.nuget.org/packages/mikhailmelnikov%2Flaravel-jobs-monitor) | v1.0.0 | Mikhail Melnikov | Admin-agnostic core for monitoring Laravel scheduled tasks and database queue j… |
| 2026-10-14 14:13:21 | [vinkius/ai-connect-sdk-laravel](https://www.nuget.org/packages/vinkius%2Fai-connect-sdk-laravel) | v0.1.0 | Vinkius | Laravel integration for @vinkius/connect. Give every user of your AI app their… |
| 2026-10-14 14:13:21 | [vinkius/connect-laravel](https://www.nuget.org/packages/vinkius%2Fconnect-laravel) | v0.1.0 | Vinkius | Laravel integration for @vinkius/connect. Give every user of your AI app their… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
