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

## Latest list — 2026-10-31 22:19 UTC

New packages created between 2026-10-31 21:21 UTC and 2026-10-31 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T22-19-30-139244Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 21:25:35 | [nowo-tech/sms-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fsms-kit-bundle) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | SMS sending for Symfony with a provider registry (Twilio, SMS Bridge, log, null… |
| 2026-10-31 21:43:14 | [maxcxam/larsadmin-medialibrary](https://www.nuget.org/packages/maxcxam%2Flarsadmin-medialibrary) | v1.0.1 | Maksym Rudenko | spatie/laravel-medialibrary fields (single file and gallery) for the larsadmin… |
| 2026-10-31 21:52:48 | [nowo-tech/mail-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fmail-kit-bundle) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Runtime-configurable mailer for Symfony on top of Instance Settings: DSN and se… |
| 2026-10-31 22:06:19 | [drivkraft/valkyrie](https://www.nuget.org/packages/drivkraft%2Fvalkyrie) | v1.0.0 | Kim Eric Helle | Role-based authorization for Laravel — roles, permissions and abilities with sc… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
