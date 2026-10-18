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

## Latest list — 2026-10-18 10:21 UTC

New packages created between 2026-10-18 09:21 UTC and 2026-10-18 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T10-21-10-196778Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 09:45:17 | [forxer/ovh-sdk](https://www.nuget.org/packages/forxer%2Fovh-sdk) | 0.1.0 | Vincent Garnier | An unofficial, modern PHP SDK for the OVHcloud API, built on Saloon, with Larav… |
| 2026-10-18 09:57:06 | [socialdept/atp-appview](https://www.nuget.org/packages/socialdept%2Fatp-appview) | v0.1.0 |  | Build lexicon-driven AT Protocol AppViews in Laravel |
| 2026-10-18 09:58:17 | [tobento/app-renderable](https://www.nuget.org/packages/tobento%2Fapp-renderable) | 2.0 | Tobias Strub | Renderable support for the app, wiring the renderable factory with media, html… |
| 2026-10-18 10:05:43 | [shimonahamed/software-billing](https://www.nuget.org/packages/shimonahamed%2Fsoftware-billing) | v1.0.1 |  | Laravel software billing package |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
