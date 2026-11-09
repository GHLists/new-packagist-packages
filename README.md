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

## Latest list — 2026-11-09 16:21 UTC

New packages created between 2026-11-09 15:19 UTC and 2026-11-09 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T16-21-49-942342Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 15:28:32 | [tyhp/ext-tyhp](https://www.nuget.org/packages/tyhp%2Fext-tyhp) | 0.1.0 |  | Optional PHP extension for the Tyhp runtime. |
| 2026-11-09 15:35:01 | [lloc/seo](https://www.nuget.org/packages/lloc%2Fseo) | 1.0.0 | Dennis Ploetner | Library for SEO related scripts & functionalities in WordPress websites |
| 2026-11-09 15:48:03 | [ympact/laravel-icon-registry](https://www.nuget.org/packages/ympact%2Flaravel-icon-registry) | v1.0.0 | Maurits | A searchable catalogue of the icons a Laravel app can draw, across Flux, Blade… |
| 2026-11-09 16:10:25 | [semhoun/slim-session](https://www.nuget.org/packages/semhoun%2Fslim-session) | 1.0.0 |  | Server-backed sessions with atomic lifecycle guarantees |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
