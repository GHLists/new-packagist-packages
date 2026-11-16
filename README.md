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

## Latest list — 2026-11-16 07:21 UTC

New packages created between 2026-11-16 06:20 UTC and 2026-11-16 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T07-21-42-963555Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 06:32:42 | [citrus-framework/schedule](https://www.nuget.org/packages/citrus-framework%2Fschedule) | v1.0.0 | take64 | php schedule library |
| 2026-11-16 06:44:06 | [antlerslabs/runes-laravel](https://www.nuget.org/packages/antlerslabs%2Frunes-laravel) | v0.1.0 | Antlers Labs | Laravel SDK for Runes error tracking |
| 2026-11-16 07:10:11 | [anjan011/2fa-support](https://www.nuget.org/packages/anjan011%2F2fa-support) | v1.0.0 | Anjan | A Laravel package for TOTP-based 2FA with QR image and backup codes. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
