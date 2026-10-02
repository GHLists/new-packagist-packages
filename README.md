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

## Latest list — 2026-10-02 15:19 UTC

New packages created between 2026-10-02 14:19 UTC and 2026-10-02 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T15-19-45-073755Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 14:27:34 | [clicalmani/metrics](https://www.nuget.org/packages/clicalmani%2Fmetrics) | v1.0.0-alpha | clicalmani | A metrics package for Tonka |
| 2026-10-02 14:28:25 | [vortechron/filament-block-editor](https://www.nuget.org/packages/vortechron%2Ffilament-block-editor) | v0.1.0 | Vortechron | A Notion-style block editor and page builder for Filament 5: BlockNote content,… |
| 2026-10-02 14:58:18 | [alexhackney/laravel-ntfy](https://www.nuget.org/packages/alexhackney%2Flaravel-ntfy) | v0.1.0 | Alex Hackney | ntfy notifications channel and client for Laravel |
| 2026-10-02 15:01:11 | [nordwerk/contao-teasers-bundle](https://www.nuget.org/packages/nordwerk%2Fcontao-teasers-bundle) | v0.1.0 |  | Source-driven Twig teaser cards for Contao |
| 2026-10-02 15:01:11 | [nordwerk/contao-testimonials-bundle](https://www.nuget.org/packages/nordwerk%2Fcontao-testimonials-bundle) | v0.1.0 |  | Moderated customer testimonials and submissions for Contao |
| 2026-10-02 15:16:35 | [asignua/filament-seo-files](https://www.nuget.org/packages/asignua%2Ffilament-seo-files) | v1.0.0 | Mykhailo Hladchenko | sitemap.xml, robots.txt, llms.txt and llms-full.txt for Filament panels: plugga… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
