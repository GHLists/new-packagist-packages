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

## Latest list — 2026-10-28 18:21 UTC

New packages created between 2026-10-28 17:21 UTC and 2026-10-28 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T18-21-25-68541Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 17:30:03 | [tmwk/pdf-section-splitter-bundle](https://www.nuget.org/packages/tmwk%2Fpdf-section-splitter-bundle) | v1.0.0 | Mario Figueroa | Bundle desacoplado para Symfony 5.4+ / PHP 8.1+ que segmenta determinísticament… |
| 2026-10-28 17:38:23 | [jumphp/jumphp](https://www.nuget.org/packages/jumphp%2Fjumphp) | v0.1.0 |  | JumPHP: write retro 2D / 3D games in PHP that run on the desktop and in the bro… |
| 2026-10-28 17:41:16 | [cordbolte/statamic-alpine](https://www.nuget.org/packages/cordbolte%2Fstatamic-alpine) | v1.0.0 | Cord Bolte | Pass Statamic data to Alpine.js (or any JavaScript) as JSON: select fields, joi… |
| 2026-10-28 18:01:24 | [anghelutav/laravel-pdf-templates](https://www.nuget.org/packages/anghelutav%2Flaravel-pdf-templates) | v0.1.1 | AnghelutaV | PDF templates for Laravel: visual designer (pdfme) or HTML/CSS with placeholder… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
