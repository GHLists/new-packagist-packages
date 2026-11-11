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

## Latest list — 2026-11-11 17:19 UTC

New packages created between 2026-11-11 16:20 UTC and 2026-11-11 17:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T17-19-34-699139Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 16:30:38 | [stackradar/php](https://www.nuget.org/packages/stackradar%2Fphp) | v0.1.0 |  | Report installed Composer dependencies and PHP runtime information to StackRada… |
| 2026-11-11 16:33:43 | [karaodin/filament-dynamic-tables](https://www.nuget.org/packages/karaodin%2Ffilament-dynamic-tables) | v1.0.0 | karaOdin | Supercharge Filament tables with user views, preset views, a favorites bar, qui… |
| 2026-11-11 16:38:32 | [juaniquillo/base-backend-component](https://www.nuget.org/packages/juaniquillo%2Fbase-backend-component) | v0.1.0 | Victor Sánchez | Framework-agnostic base state for backend components: attributes, contents, set… |
| 2026-11-11 17:04:08 | [light8749/recoverkit](https://www.nuget.org/packages/light8749%2Frecoverkit) | v1.0.0 |  | RecoverKit PHP SDK and read-only connector: record real sales and bring in past… |
| 2026-11-11 17:12:05 | [pasak-dev/pasak-secure-monitor-laravel](https://www.nuget.org/packages/pasak-dev%2Fpasak-secure-monitor-laravel) | v1.0.0 | Roby; pasak-dev | Pasak - enterprise-grade headless self-hosted WAF, threat detection engine, zer… |
| 2026-11-11 17:15:01 | [lara-igniter/laraigniter-qrcode](https://www.nuget.org/packages/lara-igniter%2Flaraigniter-qrcode) | v1.0.0 |  | Fluent QR codes for Laraigniter. The QrCode facade builds a code through BaconQ… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
