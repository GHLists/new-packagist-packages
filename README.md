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

## Latest list — 2026-10-11 18:21 UTC

New packages created between 2026-10-11 17:20 UTC and 2026-10-11 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T18-21-14-40714Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 17:20:10 | [tenma/psr](https://www.nuget.org/packages/tenma%2Fpsr) | v0.1.1 |  | Runs any PSR-15 app under Tenma: PSR-7 requests in, Tenma responses out, WebSoc… |
| 2026-10-11 17:21:53 | [taldres/laravel-waitlist](https://www.nuget.org/packages/taldres%2Flaravel-waitlist) | v0.1.0 | Dennis Petersmann | Privacy-first, headless waitlist package for Laravel: subscription cycles with… |
| 2026-10-11 17:34:05 | [tmonier/sylius-admin-order-creation-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-admin-order-creation-plugin) | v1.0.0 | Thibaut Monier | Create orders on behalf of customers (phone and back-office orders) from the Sy… |
| 2026-10-11 17:41:13 | [dockcodes/dock-ray-magento](https://www.nuget.org/packages/dockcodes%2Fdock-ray-magento) | 1.0.0 | Jacek Sultan | Magento 2 / Adobe Commerce module reporting PHP errors, exceptions, request tim… |
| 2026-10-11 17:44:13 | [systonia/waypoint-export](https://www.nuget.org/packages/systonia%2Fwaypoint-export) | v1.0.0 |  | Table downloads for Waypoint: return a Sheet from a route and get CSV, JSON Lin… |
| 2026-10-11 17:45:09 | [systonia/waypoint-export-fixed](https://www.nuget.org/packages/systonia%2Fwaypoint-export-fixed) | v1.0.0 |  | Fixed-width record files for waypoint-export: #[Fixed] column layouts, Windows-… |
| 2026-10-11 17:46:13 | [se7enxweb/expqueue](https://www.nuget.org/packages/se7enxweb%2Fexpqueue) | v0.1.0 | 7x | The Exponential job queue: a generic, database-backed job queue with priority c… |
| 2026-10-11 17:47:09 | [systonia/waypoint-live](https://www.nuget.org/packages/systonia%2Fwaypoint-live) | v0.1.0 |  | Live components for Waypoint under Tenma: server-side PHP components, events an… |
| 2026-10-11 17:50:10 | [tmonier/sylius-ai-catalog-copilot-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-ai-catalog-copilot-plugin) | v1.0.0 | Thibaut Monier | AI catalog copilot for the Sylius 2 admin: reviewable product description, meta… |
| 2026-10-11 17:51:30 | [systonia/waypoint-charts](https://www.nuget.org/packages/systonia%2Fwaypoint-charts) | v1.0.0 |  | Server-rendered SVG charts for Waypoint: bar and line charts with a data table,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
