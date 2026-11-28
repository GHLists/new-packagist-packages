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

## Latest list — 2026-11-28 12:20 UTC

New packages created between 2026-11-28 11:20 UTC and 2026-11-28 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T12-20-56-125132Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 11:22:27 | [personyze/personyze](https://www.nuget.org/packages/personyze%2Fpersonyze) | v1.2.0 | Personyze | Server-side personalization and A/B testing with Personyze. One endpoint, no ru… |
| 2026-11-28 11:22:29 | [certles/filament-maps](https://www.nuget.org/packages/certles%2Ffilament-maps) | v1.0.0 |  | Reliable map fields for Filament: location picker with address search, GeoJSON… |
| 2026-11-28 11:36:15 | [baseos/connect-laravel](https://www.nuget.org/packages/baseos%2Fconnect-laravel) | 1.0.0 | BaseOS | BaseOS Connect for Laravel — one-command pairing, HMAC receiver, Eloquent publi… |
| 2026-11-28 11:58:48 | [pkc/sms-gateway](https://www.nuget.org/packages/pkc%2Fsms-gateway) | v1.0.0 | pkc | A multi-provider SMS gateway integration package for Laravel. |
| 2026-11-28 12:00:28 | [sec/promotionimage](https://www.nuget.org/packages/sec%2Fpromotionimage) | 1.0.4 | Stefan Eik Christiansen | Add an image to Shopware promotions and display it in cart and checkout line it… |
| 2026-11-28 12:13:50 | [klsoft/auth-session](https://www.nuget.org/packages/klsoft%2Fauth-session) | 1.0.0 |  | Session based authentication |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
