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

## Latest list — 2026-10-21 12:20 UTC

New packages created between 2026-10-21 11:20 UTC and 2026-10-21 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T12-20-19-218998Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 11:21:29 | [amanuellegese/omnipay-chapa](https://www.nuget.org/packages/amanuellegese%2Fomnipay-chapa) | v0.1.0 | Amanuel Legese | Chapa driver for the Omnipay PHP payment processing library |
| 2026-10-21 11:25:20 | [t-labs-co/laravel-cleanup-data](https://www.nuget.org/packages/t-labs-co%2Flaravel-cleanup-data) | 1.0.0 | Ty Huynh | Centralized data-retention and cleanup framework for Laravel — prune Eloquent m… |
| 2026-10-21 11:35:06 | [shoplygg/shoply-php](https://www.nuget.org/packages/shoplygg%2Fshoply-php) | v0.1.0 |  | Shoply's API from your own server: every route as a method, safe retries, pages… |
| 2026-10-21 11:38:42 | [sidus/doctrine-filter-bundle](https://www.nuget.org/packages/sidus%2Fdoctrine-filter-bundle) | v1.0.0 | Vincent Chalnot | Doctrine ORM provider for sidus/filter-bundle: criteria compiled to determinist… |
| 2026-10-21 11:40:51 | [hankchen/php-canvas-pdf-renderer](https://www.nuget.org/packages/hankchen%2Fphp-canvas-pdf-renderer) | v1.0.0 | HankChen | tFPDF-based PDF renderer backend for hankchen/php-canvas-next |
| 2026-10-21 11:43:55 | [amjadiqbal/laravel-media-viewer](https://www.nuget.org/packages/amjadiqbal%2Flaravel-media-viewer) | v0.1.0 | Amjad Iqbal | Show PDFs, video and audio from any Laravel disk without leaking private files:… |
| 2026-10-21 11:44:00 | [amjadiqbal/laravel-swiper](https://www.nuget.org/packages/amjadiqbal%2Flaravel-swiper) | v1.0.0 | Amjad Iqbal | Swiper sliders and carousels for Laravel: Blade components with typed props for… |
| 2026-10-21 11:44:53 | [ixbox/php-superjson](https://www.nuget.org/packages/ixbox%2Fphp-superjson) | v0.1.0 |  | PHP implementation of superjson with compatibility for Node.js superjson |
| 2026-10-21 11:57:06 | [theaaronlawrence/laravel-culprit](https://www.nuget.org/packages/theaaronlawrence%2Flaravel-culprit) | v0.1.0 | Aaron Lawrence | Report exceptions from your Laravel app to Culprit. |
| 2026-10-21 12:04:55 | [limegreentangerine/lgt-concrete](https://www.nuget.org/packages/limegreentangerine%2Flgt-concrete) | 1.0.0-rc.1 |  | A fully featured skeleton for a composer managed Concrete site |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
