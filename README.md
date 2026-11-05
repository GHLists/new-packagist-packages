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

## Latest list — 2026-11-05 20:19 UTC

New packages created between 2026-11-05 19:20 UTC and 2026-11-05 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T20-19-56-90427Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 19:37:31 | [aifinpay/drupal-connector](https://www.nuget.org/packages/aifinpay%2Fdrupal-connector) | v1.0.0 |  | AiFinPay for Drupal: AI agents pay for protected pages (HTTP 402); prepaid rece… |
| 2026-11-05 19:47:45 | [filafly/filament-lucide-icons](https://www.nuget.org/packages/filafly%2Ffilament-lucide-icons) | v1.0.1 | Nolan Nordlund | Lucide icon pack for Filament Icons: replaces every Filament UI icon with Lucide |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
