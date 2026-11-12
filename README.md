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

## Latest list — 2026-11-12 08:21 UTC

New packages created between 2026-11-12 07:21 UTC and 2026-11-12 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T08-21-20-390552Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 07:26:03 | [magetu/module-turnstile](https://www.nuget.org/packages/magetu%2Fmodule-turnstile) | 1.0.0 | Magetu | Registers Cloudflare Turnstile as a native captcha type for Magento Open Source… |
| 2026-11-12 07:40:07 | [toshkq93/laravel-outbox](https://www.nuget.org/packages/toshkq93%2Flaravel-outbox) | 0.0.1 | toshkq93 | Reliable messaging for Laravel: transactional outbox with a SKIP LOCKED relay,… |
| 2026-11-12 07:49:49 | [maxim-tsatsura/filament-cad-blueprint](https://www.nuget.org/packages/maxim-tsatsura%2Ffilament-cad-blueprint) | v1.0.0 | Maxim Tsatsura | 2D CAD blueprint viewer and editor integration for Filament 5 |
| 2026-11-12 07:52:28 | [reavideo/shotlist](https://www.nuget.org/packages/reavideo%2Fshotlist) | v1.0.0 |  | Parse a plain-text shot list into shots, timings and cut statistics. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
