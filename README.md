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

## Latest list — 2026-10-27 23:20 UTC

New packages created between 2026-10-27 22:21 UTC and 2026-10-27 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T23-20-48-729215Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 22:22:40 | [jkudish/librarium-spec](https://www.nuget.org/packages/jkudish%2Flibrarium-spec) | v1.0.0 |  | Shared Librarium contract: request/Run schemas, source catalog, and conformance… |
| 2026-10-27 22:30:03 | [floriankraemer/php-aop-extension](https://www.nuget.org/packages/floriankraemer%2Fphp-aop-extension) | v0.1.0 | Florian Krämer | Native aspect-oriented programming for PHP: a Zend engine extension that weaves… |
| 2026-10-27 22:36:18 | [mapsight/pulp-pdo](https://www.nuget.org/packages/mapsight%2Fpulp-pdo) | v1.0.0 | Paul Golmann | Database source and destination handlers for Pulp pipelines, via PDO. |
| 2026-10-27 22:36:18 | [mapsight/pulp-search-index](https://www.nuget.org/packages/mapsight%2Fpulp-search-index) | v1.0.0 | Paul Golmann | Search index of GeoJSON features for Pulp pipelines: build it, store it in a da… |
| 2026-10-27 22:37:44 | [hostily/captcha](https://www.nuget.org/packages/hostily%2Fcaptcha) | v0.1.0 | connect - Media & Teledienst | Server-side client for hostily Captcha (captcha.hostily.de): verify the token o… |
| 2026-10-27 22:59:25 | [jkudish/laravel-ai-librarium](https://www.nuget.org/packages/jkudish%2Flaravel-ai-librarium) | v1.0.0 | Joey Kudish | A Laravel-native research query abstraction built on the Laravel AI SDK. |
| 2026-10-27 23:00:57 | [jkudish/laravel-ai-librarium-firecrawl](https://www.nuget.org/packages/jkudish%2Flaravel-ai-librarium-firecrawl) | v1.0.0 |  | Optional Firecrawl surface-collection adapter for Laravel AI Librarium. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
