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

## Latest list — 2026-11-23 23:20 UTC

New packages created between 2026-11-23 22:20 UTC and 2026-11-23 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T23-20-08-373812Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 22:25:59 | [hnooz/filament-zone-map](https://www.nuget.org/packages/hnooz%2Ffilament-zone-map) | v1.0.0 | Mohamed Idris | Draw, edit and display geographic zones on Google Maps in Filament. |
| 2026-11-23 22:32:59 | [sliusardev/hata](https://www.nuget.org/packages/sliusardev%2Fhata) | v0.1.3 |  | Hata: an admin panel and CMS for Laravel (users, roles, site settings, media li… |
| 2026-11-23 23:10:02 | [juaniquillo/backend-design-system](https://www.nuget.org/packages/juaniquillo%2Fbackend-design-system) | v0.1.0 | Victor Sánchez | Laravel design system: PHP components, Tailwind theme files, config-driven desi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
