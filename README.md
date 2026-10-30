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

## Latest list — 2026-10-30 02:19 UTC

New packages created between 2026-10-30 01:20 UTC and 2026-10-30 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T02-19-47-568384Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 01:29:40 | [superroute/slocker](https://www.nuget.org/packages/superroute%2Fslocker) | v0.1.0 |  | sLocker: deliver to Superroute smart lockers. The partner locker delivery API a… |
| 2026-10-30 01:38:41 | [tacraft-social-guild/flarum-login-screen](https://www.nuget.org/packages/tacraft-social-guild%2Fflarum-login-screen) | 1.0.0 | TCS Dev HUB | Customize the login screen for your Flarum forum. |
| 2026-10-30 01:41:06 | [bacink/krw-hub-client](https://www.nuget.org/packages/bacink%2Fkrw-hub-client) | v1.0.0 |  | Client library for BKPSDM HUB: app token, SI-ASN, TTE, SIM-ASN gateway, and SIM… |
| 2026-10-30 01:41:33 | [contenir/contenir-test](https://www.nuget.org/packages/contenir%2Fcontenir-test) | v0.1.0 |  | Test helpers shared by Contenir packages and sites: a PSR-11 container, a fixed… |
| 2026-10-30 02:16:56 | [zeyen/filse](https://www.nuget.org/packages/zeyen%2Ffilse) | v0.0.1 |  | PHP client for the image-hosting / file-uploads gateway: upload, private URL, f… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
