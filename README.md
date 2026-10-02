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

## Latest list — 2026-10-02 16:21 UTC

New packages created between 2026-10-02 15:19 UTC and 2026-10-02 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T16-21-46-714946Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 15:25:07 | [ligorikus/h3-php](https://www.nuget.org/packages/ligorikus%2Fh3-php) | 1.0.0 |  | Pure PHP implementation of H3 geospatial indexing system |
| 2026-10-02 15:34:10 | [lucajackal85/pii-sanitizer-php](https://www.nuget.org/packages/lucajackal85%2Fpii-sanitizer-php) | v0.1.0 | Luca Giacalone | Monolog processor and Unix-socket client that scrub PII and secrets via the loc… |
| 2026-10-02 15:42:56 | [hydrakit/seo](https://www.nuget.org/packages/hydrakit%2Fseo) | v0.24.0 | William Hleucka | Meta tags, sitemaps and Atom feeds for Hydra: built from plain values, escaped… |
| 2026-10-02 15:51:24 | [lucajackal85/pii-sanitizer-symfony](https://www.nuget.org/packages/lucajackal85%2Fpii-sanitizer-symfony) | v0.1.1 | Luca Giacalone | Symfony bundle that scrubs PII and secrets from Monolog records via the local P… |
| 2026-10-02 15:53:07 | [lts/php-qa-ci](https://www.nuget.org/packages/lts%2Fphp-qa-ci) | 84.0.0 |  |  |
| 2026-10-02 15:54:34 | [openexit/openexit](https://www.nuget.org/packages/openexit%2Fopenexit) | v0.1.0 |  | OpenExit SDK for the Portable Application State Protocol (PASP) |
| 2026-10-02 15:55:37 | [lenorix/laravel-datadis-client](https://www.nuget.org/packages/lenorix%2Flaravel-datadis-client) | v0.1.0 | Jesus Hernandez | Laravel integration for lenorix/datadis-client: Datadis electricity data on Lar… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
