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

## Latest list — 2026-11-05 03:20 UTC

New packages created between 2026-11-05 02:19 UTC and 2026-11-05 03:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T03-20-20-132212Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 02:33:17 | [mathsgod/light-entity](https://www.nuget.org/packages/mathsgod%2Flight-entity) | v1.0.0 |  | A PDO-based entity ORM built on light-linq |
| 2026-11-05 02:35:14 | [boysfromthefactory/laravel-archivable](https://www.nuget.org/packages/boysfromthefactory%2Flaravel-archivable) | v0.2.0 | Boys From The Factory | Move old Eloquent records to a separate archive database, the Prunable way. |
| 2026-11-05 02:51:34 | [eii/filament-turnstile](https://www.nuget.org/packages/eii%2Ffilament-turnstile) | v1.0.0 |  | Cloudflare Turnstile integration for Filament 5 forms. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
