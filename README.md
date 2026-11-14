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

## Latest list — 2026-11-14 18:19 UTC

New packages created between 2026-11-14 17:18 UTC and 2026-11-14 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T18-19-17-016526Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 17:37:43 | [dotsystems/dotapp](https://www.nuget.org/packages/dotsystems%2Fdotapp) | 2.1.0 | Stefan Miscik | DotApp PHP framework - a complete, scalable and efficient tool for web applicat… |
| 2026-11-14 17:40:33 | [reachweb/resrv-payment-eurobank](https://www.nuget.org/packages/reachweb%2Fresrv-payment-eurobank) | v1.0.0 | Iosif Chatzimichail | Eurobank (Greece) payment gateway for Statamic Resrv. |
| 2026-11-14 17:42:05 | [outstand/embeds](https://www.nuget.org/packages/outstand%2Fembeds) | 1.0.0 | Sérgio Santos | Embed Facebook and Instagram posts and videos in the Embed block, and load them… |
| 2026-11-14 17:54:37 | [jalalix/php](https://www.nuget.org/packages/jalalix%2Fphp) | 0.1.0 | Hossein Maklavani | Jalali (Persian / Shamsi) calendar for PHP. Pure PHP, no runtime dependencies. |
| 2026-11-14 17:54:50 | [steddle/seal](https://www.nuget.org/packages/steddle%2Fseal) | v0.1.0 | Steddle Group B.V. | The fingerprint and canonical JSON that Steddle's products store proof with: SH… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
