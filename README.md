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

## Latest list — 2026-11-26 16:19 UTC

New packages created between 2026-11-26 15:20 UTC and 2026-11-26 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T16-19-46-585021Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 15:20:39 | [alexandrebulete/ddd-comment-bundle](https://www.nuget.org/packages/alexandrebulete%2Fddd-comment-bundle) | 1.0.0 | Alexandre Bulete | Comments under any content as a reusable DDD Bounded Context: manual or automat… |
| 2026-11-26 15:32:37 | [byte5/whereabouts](https://www.nuget.org/packages/byte5%2Fwhereabouts) | v0.1.1 | byte5 GmbH | Shows where an asset is used and warns before one in use is deleted. |
| 2026-11-26 15:34:31 | [myleapp/myle](https://www.nuget.org/packages/myleapp%2Fmyle) | v0.1.0 | Myle | The official PHP SDK of the Myle API (https://api.myleapp.fr) |
| 2026-11-26 15:47:04 | [alexandrebulete/ddd-seo-bundle](https://www.nuget.org/packages/alexandrebulete%2Fddd-seo-bundle) | 1.0.0 | Alexandre Bulete | SEO as a reusable DDD Bounded Context: titles, descriptions, canonical and shar… |
| 2026-11-26 15:49:49 | [qmgateway/qmgateway-php](https://www.nuget.org/packages/qmgateway%2Fqmgateway-php) | v0.1.0 |  | The official PHP SDK for the QMGateway API: send SMS and one-time passwords, fo… |
| 2026-11-26 16:10:38 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.50.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-26 16:13:32 | [indual-web/swiss-parks-php-sdk](https://www.nuget.org/packages/indual-web%2Fswiss-parks-php-sdk) | v22.0 | indual | PHP SDK that imports Swiss Parks offers into a local SQLite database and render… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
