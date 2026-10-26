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

## Latest list — 2026-10-26 09:21 UTC

New packages created between 2026-10-26 08:21 UTC and 2026-10-26 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T09-21-01-826964Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 08:31:28 | [osticket/mail](https://www.nuget.org/packages/osticket%2Fmail) | v0.1.0 | JediKev | Framework-agnostic mail engine for osTicket 2.0 (RFC message build, transports,… |
| 2026-10-26 08:33:56 | [aotr/laravel-animated-icons](https://www.nuget.org/packages/aotr%2Flaravel-animated-icons) | v1.0.0 | Animesh Chakraborty | Plug-and-play animated SVG icons for Laravel Blade: hover, click, auto and on-v… |
| 2026-10-26 08:48:01 | [yuriitatur/nested-data](https://www.nuget.org/packages/yuriitatur%2Fnested-data) | v0.1.0 | Yurii Tatur | Nested data storage-agnostic library |
| 2026-10-26 09:06:46 | [cabuz/laravel-db-safe-mode](https://www.nuget.org/packages/cabuz%2Flaravel-db-safe-mode) | v1.1.0 | Florin Cabuz | Work with production data locally without fear: block outbound email, notificat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
