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

## Latest list — 2026-11-09 03:20 UTC

New packages created between 2026-11-09 02:20 UTC and 2026-11-09 03:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T03-20-33-765886Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 02:26:49 | [moztopia/notifications](https://www.nuget.org/packages/moztopia%2Fnotifications) | 0.9.0 |  | Laravel notification history and independently queued FCM and APNs device deliv… |
| 2026-11-09 03:02:12 | [bignall/wp-foundation](https://www.nuget.org/packages/bignall%2Fwp-foundation) | v0.1.0 | Bignall | Lifecycle framework for WordPress plugins: requirement checks, activation, deac… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
