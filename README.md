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

## Latest list — 2026-10-17 11:21 UTC

New packages created between 2026-10-17 10:20 UTC and 2026-10-17 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T11-21-05-956017Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 10:32:01 | [chatsong/voice-note](https://www.nuget.org/packages/chatsong%2Fvoice-note) | v1.0.2 |  | Voice note recorder for Chatsong |
| 2026-10-17 10:36:07 | [raqmeyat/smart-orm](https://www.nuget.org/packages/raqmeyat%2Fsmart-orm) | v0.1.0 | Loai Kanou | Request-driven smart field selection and smart filters for Eloquent, with data-… |
| 2026-10-17 11:03:48 | [shannonllc/avacast](https://www.nuget.org/packages/shannonllc%2Favacast) | v0.1.0 | SHANNON LIMITED LIABILITY COM… | PHP SDK for avacast realtime avatars: create sessions, make the avatar speak an… |
| 2026-10-17 11:12:28 | [shannonllc/sealgate](https://www.nuget.org/packages/shannonllc%2Fsealgate) | v0.1.0 | SHANNON LIMITED LIABILITY COM… | PHP SDK for SealGate: passkey registration and login, users and passkeys, recov… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
