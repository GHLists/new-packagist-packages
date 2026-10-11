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

## Latest list — 2026-10-11 21:19 UTC

New packages created between 2026-10-11 20:18 UTC and 2026-10-11 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T21-19-04-679357Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 20:20:06 | [zenky/undermine-frontpad](https://www.nuget.org/packages/zenky%2Fundermine-frontpad) | v3.0.0 | tzurbaev | Undermine Frontpad SDK Package |
| 2026-10-11 20:26:14 | [kusikusicms/admin](https://www.nuget.org/packages/kusikusicms%2Fadmin) | v13.0.1 |  | Admin UI for managing content in KusikusiCMS. |
| 2026-10-11 20:26:20 | [kusikusicms/media](https://www.nuget.org/packages/kusikusicms%2Fmedia) | v13.0.1 |  | Media manager for KusikusiCMS. |
| 2026-10-11 20:26:21 | [kusikusicms/models](https://www.nuget.org/packages/kusikusicms%2Fmodels) | v13.0.1 |  | Core Eloquent models for KusikusiCMS. |
| 2026-10-11 20:26:24 | [kusikusicms/website](https://www.nuget.org/packages/kusikusicms%2Fwebsite) | v13.0.1 |  | Website/router manager for KusikusiCMS. |
| 2026-10-11 20:35:17 | [cable8mm/portone-php](https://www.nuget.org/packages/cable8mm%2Fportone-php) | v0.1.0 |  | PortOne V2 server SDK for PHP. |
| 2026-10-11 20:37:00 | [robyajo/pasak](https://www.nuget.org/packages/robyajo%2Fpasak) | v1.2.4 | Roby | Pasak - enterprise-grade headless self-hosted WAF, threat detection engine, zer… |
| 2026-10-11 20:55:27 | [vivutio/payment-module](https://www.nuget.org/packages/vivutio%2Fpayment-module) | v0.1.0 | Ezekiel Mjema | Payments for vivutio: what the organization is owed for its bookings and ticket… |
| 2026-10-11 21:00:30 | [afaztech/reactor-force-join](https://www.nuget.org/packages/afaztech%2Freactor-force-join) | v0.1.0 | Abolfazl Majidi (Afaz) | Force-join (mandatory channel subscription) middleware for Reactor bots. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
