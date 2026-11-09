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

## Latest list — 2026-11-09 07:18 UTC

New packages created between 2026-11-09 06:21 UTC and 2026-11-09 07:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T07-18-53-412038Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 07:04:15 | [yassrzg/ckeditor-dsfr-bundle](https://www.nuget.org/packages/yassrzg%2Fckeditor-dsfr-bundle) | v1.2.1 | yassine REZGUI | Éditeur CKEditor 5 à composants DSFR (cartes, tuiles, boutons, accordéons, ongl… |
| 2026-11-09 07:04:16 | [yassrzg/dsfr-card-image-bundle](https://www.nuget.org/packages/yassrzg%2Fdsfr-card-image-bundle) | v1.0.2 | yassine REZGUI | Images adaptées aux cartes du Système de Design de l'État (DSFR) pour Symfony :… |
| 2026-11-09 07:04:18 | [yassrzg/matomo-reporting-bundle](https://www.nuget.org/packages/yassrzg%2Fmatomo-reporting-bundle) | v1.0.2 | yassine REZGUI | Statistiques de fréquentation Matomo dans une application Symfony : client de l… |
| 2026-11-09 07:09:54 | [hadiabedzadeh/laravel-journey-builder](https://www.nuget.org/packages/hadiabedzadeh%2Flaravel-journey-builder) | v0.3.4-beta.1 |  | Reusable drag-and-drop journey orchestration for Laravel with SMS and configura… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
