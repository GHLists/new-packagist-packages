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

## Latest list — 2026-11-16 18:20 UTC

New packages created between 2026-11-16 17:20 UTC and 2026-11-16 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T18-20-02-726272Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 17:32:43 | [ercikktm/numero-a-letras-mx](https://www.nuget.org/packages/ercikktm%2Fnumero-a-letras-mx) | v1.0.0 | ErcikKtm | Convierte números en formato mexicano a letras, con soporte para modo moneda |
| 2026-11-16 17:48:35 | [starbug/emails-admin](https://www.nuget.org/packages/starbug%2Femails-admin) | v0.9.0 | Ali Gangji | Admin screens for email templates. |
| 2026-11-16 17:54:21 | [matheel/matheel-php](https://www.nuget.org/packages/matheel%2Fmatheel-php) | v0.1.0 | Matheel | Official client for the Matheel ZATCA Phase 2 e-invoicing API (Saudi Arabia, Fa… |
| 2026-11-16 18:02:22 | [starbug/log-admin](https://www.nuget.org/packages/starbug%2Flog-admin) | v0.9.0 | Ali Gangji | Admin screens for the error log. |
| 2026-11-16 18:05:28 | [jeffersongoncalves/laravel-lgpd](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-lgpd) | 1.0.0 | Jefferson Gonçalves | LGPD toolkit core for Laravel: declare personal data on Eloquent models, build… |
| 2026-11-16 18:17:07 | [starbug/files-admin](https://www.nuget.org/packages/starbug%2Ffiles-admin) | v0.9.0 | Ali Gangji | Admin screens for the media library. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
