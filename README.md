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

## Latest list — 2026-10-31 09:21 UTC

New packages created between 2026-10-31 08:20 UTC and 2026-10-31 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T09-21-38-263237Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 08:29:27 | [wu/giorgio-im-socket](https://www.nuget.org/packages/wu%2Fgiorgio-im-socket) | 1.0.0 |  | Laravel backend integration for Giorgio IM, powered by Giorgio Socket. |
| 2026-10-31 08:30:20 | [kkxdev/laravel-collective-html-spatie-html-bridge](https://www.nuget.org/packages/kkxdev%2Flaravel-collective-html-spatie-html-bridge) | v1.0.0 | kkxdev | LaravelCollective/HTML compatibility wrapper backed by Spatie Laravel HTML — pr… |
| 2026-10-31 08:57:10 | [kipchak/driver-clickhouse](https://www.nuget.org/packages/kipchak%2Fdriver-clickhouse) | 1.0 |  | A ClickHouse driver for analytics queries and high-volume inserts from the Kipc… |
| 2026-10-31 08:57:12 | [kipchak/driver-vector](https://www.nuget.org/packages/kipchak%2Fdriver-vector) | 1.0 |  | A vector database driver for semantic search and RAG with Qdrant, pgvector or O… |
| 2026-10-31 08:57:15 | [kipchak/middleware-response-cache](https://www.nuget.org/packages/kipchak%2Fmiddleware-response-cache) | 1.0 |  | Response Cache Middleware for the Kipchak API Development Kit (ADK). A shared H… |
| 2026-10-31 08:57:17 | [kipchak/middleware-feature-flags](https://www.nuget.org/packages/kipchak%2Fmiddleware-feature-flags) | 1.0 |  | Feature Flag Middleware for the Kipchak API Development Kit (ADK). Gates routes… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
